from flask import Flask, render_template, request, Response, stream_with_context
import yt_dlp
import os
import threading
import queue
import time

app = Flask(__name__)
msg_queue = queue.Queue()

class MyLogger:
    def debug(self, msg):
        if not msg.startswith('[debug] '):
            msg_queue.put(msg)
    def info(self, msg):
        msg_queue.put(msg)
    def warning(self, msg):
        msg_queue.put(f"WARNING: {msg}")
    def error(self, msg):
        msg_queue.put(f"ERROR: {msg}")

def run_download_thread(video_url, save_path):
    try:
        msg_queue.put(f"🚀 เริ่มต้นการดาวน์โหลด: {video_url}")
        
        if not os.path.exists(save_path):
            os.makedirs(save_path)

        ydl_opts = {
            'format': 'bestaudio/best',
            'writethumbnail': True, 
            
            'postprocessors': [
                {
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                },
                {
                    'key': 'FFmpegThumbnailsConvertor',
                    'format': 'jpg',
                },
                {
                    'key': 'EmbedThumbnail', 
                },
                {
                    'key': 'FFmpegMetadata', 
                    'add_metadata': True,
                }
            ],
            
            'postprocessor_args': {
                'ffmpeg': ['-id3v2_version', '3']
            },
            
            'outtmpl': os.path.join(save_path, '%(playlist_index)s - %(title)s.%(ext)s'),
            'keepvideo': False,
            'noplaylist': False, 
            'ignoreerrors': True, 
            'logger': MyLogger(), 
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
            
        msg_queue.put("✅✅ ดาวน์โหลดและแปลงไฟล์ พร้อมฝังปกเสร็จสมบูรณ์! ✅✅")
        msg_queue.put("DONE") 
        
    except Exception as e:
        msg_queue.put(f"❌ เกิดข้อผิดพลาด: {str(e)}")
        msg_queue.put("DONE")

@app.route('/')
def index():
    default_path = os.path.join(os.path.expanduser("~"), "Downloads")
    return render_template('index.html', default_path=default_path)

@app.route('/start_download', methods=['POST'])
def start_download():
    url = request.form.get('url')
    save_path = request.form.get('save_path')
    
    with msg_queue.mutex:
        msg_queue.queue.clear()

    t = threading.Thread(target=run_download_thread, args=(url, save_path))
    t.daemon = True 
    t.start()
    
    return "Started"

@app.route('/stream')
def stream():
    def generate():
        while True:
            msg = msg_queue.get()
            if msg == "DONE":
                yield f"data: {msg}\n\n"
                break
            yield f"data: {msg}\n\n"
            time.sleep(0.05)
            
    return Response(stream_with_context(generate()), mimetype='text/event-stream')

if __name__ == "__main__":
    app.run(debug=True, port=5000, threaded=True)