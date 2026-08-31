# 📝 To-Do List CLI

Aplikasi manajemen tugas berbasis **Command Line Interface (CLI)** yang dibangun menggunakan Python dan library [`rich`](https://github.com/Textualize/rich) untuk tampilan tabel dan teks berwarna. Aplikasi ini memungkinkan pengguna untuk melihat, menambah, menandai selesai, dan menghapus tugas secara interaktif melalui terminal.

## ✨ Fitur

- **Lihat Semua Tugas** — Menampilkan seluruh tugas dalam bentuk tabel rapi dengan kolom ID, Judul, Deskripsi, Status, dan Estimasi Waktu.
- **Tambah Tugas** — Menambahkan tugas baru dengan ID yang di-generate otomatis (increment dari ID terbesar).
- **Tandai Tugas Selesai** — Mengubah status tugas dari `Belum Selesai` menjadi `Selesai`.
- **Hapus Tugas** — Menghapus tugas dari daftar dengan konfirmasi (`y/n`) untuk mencegah penghapusan tidak sengaja.
- **Validasi Input** — Menangani input tidak valid (bukan angka, angka negatif, atau nol) tanpa membuat program crash.

## 📂 Struktur Proyek

```
.
├── main.py                    # Kode utama aplikasi (logika & menu CLI)
├── test_todo.py                # Unit test untuk fitur lihat semua tugas
├── test_tambah_tugas.py        # Unit test untuk fitur tambah tugas
├── test_tandai_selesai.py      # Unit test untuk fitur tandai tugas selesai
├── test_hapus_tugas.py         # Unit test untuk fitur hapus tugas
└── README.md                   # Dokumentasi proyek
```

## 🔧 Requirement

- Python 3.10+ (karena menggunakan type hint `int | None`)
- Library [`rich`](https://pypi.org/project/rich/)

## 🚀 Instalasi

1. Clone atau unduh proyek ini.
2. Buat virtual environment (opsional, tapi disarankan):
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```
3. Install dependency:
   ```bash
   pip install rich
   ```

## ▶️ Cara Menjalankan

```bash
python main.py
```

Setelah dijalankan, akan muncul menu interaktif:

```
=== Selamat Datang di Aplikasi To-Do List ===
1. Lihat Semua Tugas
2. Tambah Tugas
3. Tandai Tugas Selesai
4. Hapus Tugas
5. Keluar

Masukkan pilihan Anda (1-5):
```

Masukkan angka `1`–`5` sesuai fitur yang ingin digunakan.

## 🧩 Struktur Data Tugas

Setiap tugas disimpan sebagai `dictionary` dengan struktur berikut:

```python
{
    "id": 1,
    "title": "Judul Tugas",
    "description": "Deskripsi Tugas",
    "status": "Belum Selesai",  # atau "Selesai"
    "estimasi_waktu_pengerjaan": 30  # dalam menit
}
```

Seluruh tugas disimpan sementara (in-memory) dalam list `dummy_tasks` — data akan hilang setiap kali program ditutup (belum ada persistensi ke file/database).

## 📖 Dokumentasi Fungsi

### Fungsi Pembantu

| Fungsi | Deskripsi |
|---|---|
| `input_angka(prompt)` | Meminta input dan memvalidasi bahwa input berupa angka bulat. Mengembalikan `None` jika input tidak valid. |
| `cari_tugas_by_id(id_target)` | Mencari tugas berdasarkan ID, mengembalikan `(index, task)` atau `(None, None)` jika tidak ditemukan. |

### Fungsi Utama

| Fungsi | Deskripsi |
|---|---|
| `lihat_semua_tugas()` | Menampilkan seluruh tugas dalam tabel berwarna. |
| `tambah_tugas()` | Menambahkan tugas baru dengan validasi estimasi waktu (> 0). |
| `tandai_selesai()` | Mengubah status tugas menjadi `Selesai` berdasarkan ID. |
| `hapus_tugas()` | Menghapus tugas berdasarkan ID dengan konfirmasi pengguna. |
| `menu()` | Loop utama aplikasi yang menampilkan menu dan mengarahkan ke fungsi terkait. |

## 🧪 Testing

Proyek ini dilengkapi unit test menggunakan `unittest` dan `unittest.mock` untuk mensimulasikan input/output konsol.

Jalankan semua test dengan:

```bash
python -m unittest discover
```

Atau jalankan test per file, contoh:

```bash
python -m unittest test_tambah_tugas.py
python -m unittest test_tandai_selesai.py
python -m unittest test_hapus_tugas.py
python -m unittest test_todo.py
```

### Cakupan Skenario Test

- **test_todo.py** — Menampilkan tabel saat daftar kosong, 1 item, dan banyak item.
- **test_tambah_tugas.py** — Penambahan tugas pada daftar kosong, auto-increment ID, dan validasi estimasi waktu.
- **test_tandai_selesai.py** — Daftar kosong, input non-angka, ID tidak ditemukan, berhasil ditandai, dan tugas yang sudah selesai sebelumnya.
- **test_hapus_tugas.py** — Daftar kosong, input non-angka, ID tidak ditemukan, berhasil dihapus, dan pembatalan penghapusan.

## ⚠️ Batasan (Known Limitations)

- Data tidak disimpan secara permanen (tidak ada file JSON/database), sehingga akan reset setiap program dijalankan ulang.
- Belum ada fitur edit/update judul, deskripsi, atau estimasi waktu tugas yang sudah ada.

## 👤 Author

Dibuat sebagai proyek latihan Python CLI dengan fokus pada penggunaan `rich`, validasi input, dan unit testing.
