# 🎵 YouTube to MP3 Downloader + AI Lyrics (Whisper) 🤖

เว็บแอปพลิเคชันดาวน์โหลดเพลงจาก YouTube ที่ถูกอัปเกรดด้วยสมองกล AI จาก OpenAI (Whisper) โปรแกรมจะทำการดาวน์โหลดไฟล์เสียง พร้อมทั้งให้ AI ฟังและถอดเนื้อเพลงภาษาไทย/อังกฤษ แล้วฝังเข้าไปในไฟล์ MP3 ให้แบบวิ่งตามจังหวะ (Synchronized) ได้ไฟล์ก้อนเดียวจบ!

## 🌟 คุณสมบัติเด่น (Features)
*   **Everything in Main:** รวมความสามารถทั้งหมดจากเวอร์ชัน Stable (โหลด MP3, ฝังปก JPG, ID3v2.3)
*   **AI Auto-Transcription:** ใช้โมเดล Whisper (ตั้งค่าเริ่มต้นที่รุ่น `small` เพื่อให้สอดคล้องกับ VRAM ของการ์ดจอระดับ 4GB) ในการแกะเนื้อร้องอย่างแม่นยำ
*   **Synchronized Lyrics (SYLT):** ฝังเนื้อเพลงแบบจับเวลาเสี้ยววินาทีลงใน MP3 ทำให้แอปเล่นเพลงระดับโปร (เช่น Musicolet หรือ MusicBee) สามารถแสดงเนื้อร้องแบบคาราโอเกะได้ทันที
*   **GPU Acceleration:** รองรับการประมวลผลผ่านการ์ดจอ NVIDIA (CUDA) เพื่อความเร็วในการถอดเนื้อเพลงระดับสูงสุด

## 🛠️ สิ่งที่ต้องเตรียม (Prerequisites)
1. ติดตั้ง Python 3.8 ขึ้นไป
2. ไฟล์ `ffmpeg.exe`, `ffplay.exe`, และ `ffprobe.exe` ในโฟลเดอร์โปรเจกต์
3. **(แนะนำอย่างยิ่ง)** การ์ดจอ NVIDIA พร้อมติดตั้งระบบ CUDA เพื่อให้ AI ทำงานได้รวดเร็วขึ้น

## 🚀 วิธีติดตั้งและรันโปรแกรม

1. ติดตั้งไลบรารีพื้นฐานของโปรเจกต์:
   ```bash
   pip install -r requirements.txt
   
2. (สำคัญมาก) ติดตั้ง PyTorch เวอร์ชันรองรับการ์ดจอ (CUDA 12.1) เพื่อเร่งสปีด AI:
   ```bash
    pip install torch torchvision torchaudio --index-url [https://download.pytorch.org/whl/cu121](https://download.pytorch.org/whl/cu121)

3. สั่งรันแอปพลิเคชัน: 
   ```bash
      py app.py

5. เปิดเบราว์เซอร์แล้วเข้าไปที่: `http://127.0.0.1:5000`

## ⚙️ การตั้งค่า AI (Configuration)
หากคอมพิวเตอร์ของคุณมีการ์ดจอที่ VRAM สูงกว่า 4GB หรือต้องการความแม่นยำของภาษาไทยระดับสูงสุด สามารถเข้าไปปรับแก้โมเดล AI ในไฟล์ `app.py` ได้:
*   ค้นหาฟังก์ชัน `get_whisper_model()`
*   เปลี่ยนคำว่า `"small"` เป็น `"medium"` หรือ `"large"`
