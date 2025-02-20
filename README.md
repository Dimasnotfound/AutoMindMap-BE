# AutoMindMap Backend 🚀

Backend canggih berbasis FastAPI & NLP yang mengubah teks menjadi mind map interaktif. Ideal untuk brainstorming dinamis dan visualisasi ide secara instan. 🤖💡

## Fitur
- **Input Teks & Proses NLP**: Menerima teks dan mengubahnya menjadi struktur mind map.
- **Ekstraksi Entitas & Konsep**: Menggunakan model NLP (spaCy) untuk mendeteksi entitas seperti ORG, PERSON, dan lainnya.
- **API Cepat & Asynchronous**: Dibangun dengan FastAPI untuk performa tinggi dan dokumentasi API otomatis.
- **Mudah Diintegrasikan**: Endpoint RESTful yang siap dikonsumsi oleh frontend.

## Teknologi
- **FastAPI** – Framework backend modern.
- **spaCy** – Library NLP untuk ekstraksi informasi.
- **Uvicorn** – Server ASGI untuk menjalankan FastAPI.

## Instalasi
### Clone repository:
```bash
git clone https://github.com/username/AutoMindMap-BE.git
cd AutoMindMap-BE
```

### Buat virtual environment & aktifkan:
```bash
python -m venv venv
# Linux/Mac
source venv/bin/activate
# Windows
venv\Scripts\activate
```

### Instal dependensi:
```bash
pip install -r requirements.txt
```

### Download model spaCy (misalnya model bahasa Inggris):
```bash
python -m spacy download en_core_web_sm
```

## Menjalankan Aplikasi
Jalankan server dengan:
```bash
uvicorn app.main:app --reload
```

Server akan berjalan pada [http://localhost:8000](http://localhost:8000).

## Struktur Proyek
```
AutoMindMap-BE/
├── app/
│   ├── __init__.py
│   ├── main.py          # File utama API FastAPI
│   ├── nlp.py           # Modul untuk pemrosesan teks menggunakan spaCy
│   └── data/            # Folder untuk dataset & script training (misal: train_data.py)
├── requirements.txt
└── README.md
```

## Kontribusi
1. Fork repositori ini.
2. Buat branch baru untuk fitur/perbaikan.
3. Lakukan pull request dengan deskripsi perubahan.

## Lisensi
Proyek ini dilisensikan di bawah **MIT License**.