from rich.console import Console
from rich.table import Table

# Inisialisasi console untuk mencetak teks berwarna dan tabel bertema
console = Console()

# Data awal berupa list of dictionaries untuk menyimpan daftar tugas
dummy_tasks = [
    {"id": 1, "title": "Mempelajari Variabel dan Tipe Data", "description": "Membaca dokumentasi Python mengenai tipe data dasar.", "status": "Belum Selesai", "estimasi_waktu_pengerjaan": 30},
    {"id": 2, "title": "Membuat Fungsi Kalkulator", "description": "Menulis fungsi untuk operasi matematika sederhana.", "status": "Selesai", "estimasi_waktu_pengerjaan": 60},
    {"id": 3, "title": "Setup Virtual Environment", "description": "Menginisialisasi venv untuk proyek CLI.", "status": "Selesai", "estimasi_waktu_pengerjaan": 60},
    {"id": 4, "title": "Menulis Dokumentasi Kode", "description": "Menambahkan docstring pada setiap fungsi yang telah dibuat.", "status": "Belum Selesai", "estimasi_waktu_pengerjaan": 45},
    {"id": 5, "title": "Menerapkan Library Rich", "description": "Mengubah tampilan CLI menggunakan warna utama dan aksen.", "status": "Selesai", "estimasi_waktu_pengerjaan": 60},
    {"id": 6, "title": "Membuat Fitur Hapus Tugas", "description": "Mengimplementasikan fungsi list.pop() berdasarkan input pengguna.", "status": "Belum Selesai", "estimasi_waktu_pengerjaan": 45},
    {"id": 7, "title": "Menyimpan Data ke JSON", "description": "Menulis fungsi save_data untuk persistensi file.", "status": "Selesai", "estimasi_waktu_pengerjaan": 60},
    {"id": 8, "title": "Memperbaiki Bug Input", "description": "Menambahkan try-except block agar program tidak crash saat input salah.", "status": "Belum Selesai", "estimasi_waktu_pengerjaan": 45},
    {"id": 9, "title": "Membaca Artikel Algoritma", "description": "Mempelajari optimasi pencarian data pada list.", "status": "Belum Selesai", "estimasi_waktu_pengerjaan": 30},
    {"id": 10, "title": "Push Kode ke Repositori", "description": "Melakukan commit dan push ke GitHub.", "status": "Belum Selesai", "estimasi_waktu_pengerjaan": 45}
]

# ==========================================
# FUNGSI PEMBANTU (HELPER FUNCTIONS)
# ==========================================

def input_angka(prompt: str) -> int | None:
    """Meminta input dari pengguna dan memvalidasi agar berupa angka bulat (integer).

    Fungsi ini memanfaatkan penanganan eksepsi (try-except) untuk mencegah program 
    mengalami error (crash) jika pengguna secara tidak sengaja memasukkan teks atau simbol.

    Args:
        prompt (str): Teks instruksi yang akan ditampilkan kepada pengguna saat meminta input.

    Returns:
        int | None: Mengembalikan nilai integer jika input valid, 
                    atau None jika pengguna memasukkan data non-angka.
    """
    input_str = console.input(prompt).strip()
    try:
        return int(input_str)
    except ValueError:
        console.print("[!] Input tidak valid! Harap masukkan berupa angka.", style="bold #FFB800")
        return None


def cari_tugas_by_id(id_target: int):
    """Mencari objek tugas tertentu di dalam list `dummy_tasks` berdasarkan nilai ID-nya.

    Fungsi ini melakukan perulangan (looping) pada `dummy_tasks` menggunakan `enumerate()` 
    untuk melacak index posisi sekaligus data dict tugas tersebut.

    Args:
        id_target (int): ID dari tugas yang ingin dicari.

    Returns:
        tuple[int, dict] | tuple[None, None]: 
            - Pasangan (index, task) jika tugas dengan ID tersebut ditemukan.
            - Pasangan (None, None) jika tugas tidak ada dalam daftar.
    """
    for index, task in enumerate(dummy_tasks):
        if task["id"] == id_target:
            return index, task
    return None, None

# ==========================================
# FUNGSI UTAMA FITUR
# ==========================================

def lihat_semua_tugas():
    """Menampilkan seluruh daftar tugas dalam bentuk tabel interaktif menggunakan library Rich.

    Fungsi ini akan:
    1. Memeriksa apakah daftar tugas kosong (`dummy_tasks`).
    2. Jika ada data, membuat komponen `Table` dari modul `rich.table`.
    3. Mengatur tata letak kolom (ID, Judul, Deskripsi, Status, Estimasi Waktu).
    4. Memberikan pewarnaan khusus pada kolom 'Status' (Kuning untuk Selesai, Biru untuk Belum Selesai).
    """
    if not dummy_tasks:
        console.print("\n[!] Tidak ada tugas saat ini. Silakan tambah tugas baru.", style="bold #FFB800")
        return

    tabel = Table(title="\n=== DAFTAR TUGAS ===", title_style="bold #2D74FF", border_style="#2D74FF")
    tabel.add_column("ID", justify="center", style="bold #FFB800")
    tabel.add_column("Judul Tugas", style="#2D74FF")
    tabel.add_column("Deskripsi", style="#2D74FF")
    tabel.add_column("Status", justify="center")
    tabel.add_column("Waktu (Menit)", justify="center", style="#2D74FF")

    for task in dummy_tasks:
        status_warna = (
            f"[bold #FFB800]{task['status']}[/bold #FFB800]"
            if task["status"] == "Selesai"
            else f"[#2D74FF]{task['status']}[/#2D74FF]"
        )
        tabel.add_row(
            str(task["id"]),
            task["title"],
            task["description"],
            status_warna,
            str(task["estimasi_waktu_pengerjaan"])
        )

    console.print(tabel)


def tambah_tugas():
    """Membuat tugas baru dari input pengguna dan memasukkannya ke dalam daftar `dummy_tasks`.

    Alur kerja fungsi ini:
    1. Meminta input string berupa judul dan deskripsi tugas.
    2. Melakukan perulangan (while-loop) sampai pengguna menginputkan estimasi waktu 
       berupa angka bernilai positif (> 0).
    3. Menentukan ID baru secara otomatis:
       - Bernilai 1 jika list tugas masih kosong.
       - Mengambil `ID terbesar + 1` jika list sudah berisi data (menghindari penumpukan ID).
    4. Mengemas data ke dalam struktur dictionary dan menambahkan (append) ke `dummy_tasks`.
    """
    console.print("\n=== TAMBAH TUGAS BARU ===", style="bold #2D74FF")
    
    judul = console.input("[#2D74FF]Masukkan Judul Tugas: [/#2D74FF]").strip()
    deskripsi = console.input("[#2D74FF]Masukkan Deskripsi Tugas: [/#2D74FF]").strip()
    
    estimasi_waktu = None
    while estimasi_waktu is None or estimasi_waktu <= 0:
        estimasi_waktu = input_angka("[#2D74FF]Masukkan Estimasi Waktu (menit): [/#2D74FF]")
        if estimasi_waktu is not None and estimasi_waktu <= 0:
            console.print("[!] Estimasi waktu harus lebih dari 0 menit.", style="bold #FFB800")

    new_id = 1 if not dummy_tasks else max(task["id"] for task in dummy_tasks) + 1
    
    tugas_baru = {
        "id": new_id,
        "title": judul,
        "description": deskripsi,
        "status": "Belum Selesai",
        "estimasi_waktu_pengerjaan": estimasi_waktu
    }
    
    dummy_tasks.append(tugas_baru)
    console.print(f"\n[!] Berhasil! Tugas '{judul}' (ID: {new_id}) telah ditambahkan.", style="bold #FFB800")


def tandai_selesai():
    """Mengubah nilai atribut status tugas dari 'Belum Selesai' menjadi 'Selesai'.

    Alur kerja fungsi ini:
    1. Memeriksa keberadaan data pada `dummy_tasks`.
    2. Meminta masukkan ID tugas yang ingin diubah statusnya.
    3. Memanggil fungsi `cari_tugas_by_id()` untuk memvalidasi keberadaan tugas.
    4. Memeriksa status saat ini:
       - Jika sudah 'Selesai', menampilkan pesan pemberitahuan.
       - Jika 'Belum Selesai', mengubah nilai kunci `"status"` menjadi `"Selesai"`.
    """
    console.print("\n=== TANDAI TUGAS SELESAI ===", style="bold #2D74FF")
    
    if not dummy_tasks:
        console.print("[!] Tidak ada tugas saat ini.", style="bold #FFB800")
        return

    id_target = input_angka("[#2D74FF]Masukkan ID Tugas yang sudah selesai: [/#2D74FF]")
    if id_target is None:
        return

    _, task = cari_tugas_by_id(id_target)
    
    if task is None:
        console.print(f"[!] Tugas dengan ID {id_target} tidak ditemukan dalam daftar.", style="bold #FFB800")
        return

    if task["status"] == "Selesai":
        console.print(f"[*] Tugas '{task['title']}' sudah berstatus Selesai sebelumnya.", style="italic #FFB800")
    else:
        task["status"] = "Selesai"
        console.print(f"[!] Berhasil! Tugas '{task['title']}' (ID: {id_target}) telah ditandai sebagai Selesai.", style="bold #FFB800")


def hapus_tugas():
    """Menghapus data tugas dari list `dummy_tasks` berdasarkan ID tugas.

    Fungsi ini dilengkapi dengan fitur konfirmasi tindakan (y/n) untuk mencegah 
    terjadinya penghapusan data secara tidak sengaja oleh pengguna.

    Alur kerja fungsi ini:
    1. Memeriksa apakah `dummy_tasks` berisi tugas.
    2. Meminta masukkan ID tugas dan melakukan pencarian indeks menggunakan `cari_tugas_by_id()`.
    3. Menampilkan dialog konfirmasi penghapusan.
    4. Menghapus item dari list menggunakan statemen `del dummy_tasks[index]` jika pengguna memilih 'y'.
    """
    console.print("\n=== HAPUS TUGAS ===", style="bold #2D74FF")
    
    if not dummy_tasks:
        console.print("[!] Tidak ada tugas saat ini. Daftar kosong.", style="bold #FFB800")
        return

    id_target = input_angka("[#2D74FF]Masukkan ID Tugas yang ingin dihapus: [/#2D74FF]")
    if id_target is None:
        return

    index, task = cari_tugas_by_id(id_target)

    if index is None or task is None:
        console.print(f"[!] Tugas dengan ID {id_target} tidak ditemukan dalam daftar.", style="bold #FFB800")
        return

    console.print(f"[*] Anda akan menghapus tugas: '{task['title']}'", style="italic #FFB800")
    konfirmasi = console.input("[bold #FFB800]Apakah Anda yakin ingin menghapus tugas ini? (y/n): [/bold #FFB800]").strip().lower()

    if konfirmasi == 'y':
        del dummy_tasks[index]
        console.print(f"[!] Berhasil! Tugas '{task['title']}' (ID: {id_target}) telah dihapus.", style="bold #FFB800")
    else:
        console.print("[*] Penghapusan dibatalkan.", style="italic #2D74FF")


def menu():
    """Menjalankan siklus utama aplikasi (main loop) berbasis menu interaktif CLI.

    Fungsi ini menggunakan perulangan tak terbatas (`while True`) untuk terus menampilkan 
    pilihan menu (1-5) hingga pengguna memilih opsi 5 untuk menghentikan program (`break`).
    """
    while True:
        console.print("\n=== Selamat Datang di Aplikasi To-Do List ===", style="bold #2D74FF")
        console.print("1. Lihat Semua Tugas", style="#2D74FF")
        console.print("2. Tambah Tugas", style="#2D74FF")
        console.print("3. Tandai Tugas Selesai", style="#2D74FF")
        console.print("4. Hapus Tugas", style="#2D74FF")
        console.print("5. Keluar", style="#2D74FF")
        
        pilihan = console.input("\n[bold #FFB800]Masukkan pilihan Anda (1-5): [/bold #FFB800]").strip()

        if pilihan == '1':
            lihat_semua_tugas()
        elif pilihan == '2':
            tambah_tugas()
        elif pilihan == '3':
            tandai_selesai()
        elif pilihan == '4':
            hapus_tugas()
        elif pilihan == '5':
            console.print("\nTerima kasih telah menggunakan aplikasi ini. Sampai jumpa!", style="bold #2D74FF")
            break
        else:
            console.print("\n[!] Pilihan tidak valid. Silakan masukkan angka 1-5.", style="bold red")

if __name__ == "__main__":
    menu()
