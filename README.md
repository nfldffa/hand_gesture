Hand Gesture Recognition dengan OpenCV & Mediapipe

Proyek ini adalah implementasi pengenalan gesture tangan menggunakan OpenCV dan Mediapipe. Sistem dapat mendeteksi bentuk tangan seperti "Thumbs Up", "Peace", dan "Metal" berdasarkan landmark tangan yang terdeteksi.

📌 Fitur

Mendeteksi tangan menggunakan Mediapipe

Mengenali beberapa gesture tangan

Menampilkan hasil deteksi secara real-time dengan OpenCV

🛠️ Persyaratan

Sebelum menjalankan proyek ini, pastikan Anda telah menginstal dependensi berikut:

Python 3.x

OpenCV (cv2)

Mediapipe

🚀 Instalasi

Clone repository ini:

git clone https://github.com/nfldffa/hand_gesture.git
cd hand_gesture

Buat virtual environment (opsional tetapi disarankan):

python -m venv venv
source venv/bin/activate  # Untuk macOS/Linux
venv\Scripts\activate     # Untuk Windows

Instal dependensi dari requirements.txt:

pip install -r requirements.txt

🎯 Cara Menjalankan

Jalankan skrip utama dengan perintah berikut:

python main.py

Setelah dijalankan, kamera akan aktif dan mulai mendeteksi gesture tangan secara real-time.

📂 Struktur Proyek

hand_gesture/
│── main.py             # File utama untuk menjalankan deteksi tangan
│── requirements.txt    # Daftar dependensi
│── .gitignore          # Mengabaikan file yang tidak perlu
│── README.md           # Dokumentasi proyek

📝 Catatan

Jika kamera tidak berfungsi, pastikan webcam terhubung dan tidak digunakan oleh aplikasi lain.

Jika performa lambat, coba kurangi resolusi frame dalam kode OpenCV.

🤝 Kontribusi

Jika Anda ingin berkontribusi, silakan fork repository ini dan buat pull request dengan perbaikan atau fitur tambahan.

📜 Lisensi

Proyek ini dilisensikan di bawah MIT License.

✨ Dibuat dengan ❤️ oleh Naufal Daffa Erlangga
