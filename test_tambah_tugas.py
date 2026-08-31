import unittest
from unittest.mock import patch
import main  # Import file main.py Anda


class TestTambahTugas(unittest.TestCase):

    @patch("main.console.print")
    @patch("main.console.input")
    def test_tambah_tugas_list_kosong(self, mock_input, mock_print):
        """Skenario 1: Tambah tugas saat daftar kosong (ID otomatis menjadi 1)"""
        # Arrange
        main.dummy_tasks = []
        # Simulasi input pengguna secara berurutan: Judul, Deskripsi, Estimasi Waktu
        mock_input.side_effect = ["Tugas Pertama", "Deskripsi Tugas 1", "30"]

        # Act
        main.tambah_tugas()

        # Assert 1: Cek isi list dummy_tasks
        self.assertEqual(len(main.dummy_tasks), 1)
        self.assertEqual(main.dummy_tasks[0]["id"], 1)
        self.assertEqual(main.dummy_tasks[0]["title"], "Tugas Pertama")
        self.assertEqual(main.dummy_tasks[0]["status"], "Belum Selesai")
        self.assertEqual(main.dummy_tasks[0]["estimasi_waktu_pengerjaan"], 30)

        # Assert 2: Cek pesan output konsol
        output_terakhir = mock_print.call_args[0][0]
        self.assertIn("Berhasil! Tugas 'Tugas Pertama' (ID: 1) telah ditambahkan.", output_terakhir)

    @patch("main.console.print")
    @patch("main.console.input")
    def test_tambah_tugas_auto_increment_id(self, mock_input, mock_print):
        """Skenario 2: Tambah tugas saat daftar berisi data (ID otomatis bertambah dari ID terbesar)"""
        # Arrange
        main.dummy_tasks = [
            {"id": 5, "title": "Tugas Lama", "description": "Deskripsi", "status": "Belum Selesai", "estimasi_waktu_pengerjaan": 20}
        ]
        mock_input.side_effect = ["Tugas Baru", "Deskripsi Baru", "45"]

        # Act
        main.tambah_tugas()

        # Assert 1: Cek jumlah data dan ID tugas baru (ID harus 6)
        self.assertEqual(len(main.dummy_tasks), 2)
        self.assertEqual(main.dummy_tasks[1]["id"], 6)
        self.assertEqual(main.dummy_tasks[1]["title"], "Tugas Baru")

        # Assert 2: Cek pesan output konsol
        output_terakhir = mock_print.call_args[0][0]
        self.assertIn("ID: 6", output_terakhir)

    @patch("main.console.print")
    @patch("main.console.input")
    def test_tambah_tugas_validasi_estimasi_waktu(self, mock_input, mock_print):
        """Skenario 3: Penanganan input estimasi waktu invalid (bukan angka / <= 0) sebelum input valid"""
        # Arrange
        main.dummy_tasks = []
        # Input: Judul, Deskripsi, teks (salah), angka negatif (salah), angka 0 (salah), angka 25 (benar)
        mock_input.side_effect = [
            "Tugas Validasi",
            "Deskripsi Validasi",
            "bukan_angka",
            "-10",
            "0",
            "25"
        ]

        # Act
        main.tambah_tugas()

        # Assert 1: Pastikan tugas tetap berhasil ditambahkan dengan angka valid (25)
        self.assertEqual(len(main.dummy_tasks), 1)
        self.assertEqual(main.dummy_tasks[0]["estimasi_waktu_pengerjaan"], 25)

        # Assert 2: Pastikan pesan error input dipanggil saat input invalid
        cetakan_panggilan = [call[0][0] for call in mock_print.call_args_list]
        
        # Cek pesan error input bukan angka
        self.assertTrue(any("Input tidak valid! Harap masukkan berupa angka." in teks for teks in cetakan_panggilan))
        # Cek pesan error angka <= 0
        self.assertTrue(any("Estimasi waktu harus lebih dari 0 menit." in teks for teks in cetakan_panggilan))


if __name__ == "__main__":
    unittest.main()