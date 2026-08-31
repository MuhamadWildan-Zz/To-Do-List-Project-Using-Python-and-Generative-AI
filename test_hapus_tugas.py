import unittest
from unittest.mock import patch
import main  # Import file main.py Anda


class TestHapusTugas(unittest.TestCase):

    @patch("main.console.print")
    def test_daftar_kosong(self, mock_print):
        """Skenario 1: Menguji respon saat daftar tugas kosong ([])"""
        # Arrange
        main.dummy_tasks = []

        # Act
        main.hapus_tugas()

        # Assert: Memastikan pesan daftar kosong muncul
        cetakan = [call[0][0] for call in mock_print.call_args_list]
        self.assertTrue(any("Tidak ada tugas saat ini" in teks for teks in cetakan))

    @patch("main.console.print")
    @patch("main.console.input")
    def test_input_id_bukan_angka(self, mock_input, mock_print):
        """Skenario 2: User menginputkan ID berupa karakter/teks (bukan angka)"""
        # Arrange
        main.dummy_tasks = [
            {"id": 1, "title": "Tugas 1", "description": "Desk 1", "status": "Belum Selesai", "estimasi_waktu_pengerjaan": 30}
        ]
        mock_input.return_value = "xyz"

        # Act
        main.hapus_tugas()

        # Assert: Memastikan validasi angka berjalan
        cetakan = [call[0][0] for call in mock_print.call_args_list]
        self.assertTrue(any("Input tidak valid! Harap masukkan berupa angka." in teks for teks in cetakan))

    @patch("main.console.print")
    @patch("main.console.input")
    def test_id_tidak_ditemukan(self, mock_input, mock_print):
        """Skenario 3: User menginputkan ID angka yang tidak ada dalam daftar"""
        # Arrange
        main.dummy_tasks = [
            {"id": 1, "title": "Tugas 1", "description": "Desk 1", "status": "Belum Selesai", "estimasi_waktu_pengerjaan": 30}
        ]
        mock_input.return_value = "99"

        # Act
        main.hapus_tugas()

        # Assert: Memastikan pesan ID tidak ditemukan muncul
        cetakan = [call[0][0] for call in mock_print.call_args_list]
        self.assertTrue(any("Tugas dengan ID 99 tidak ditemukan" in teks for teks in cetakan))

    @patch("main.console.print")
    @patch("main.console.input")
    def test_berhasil_hapus_tugas(self, mock_input, mock_print):
        """Skenario 4: Berhasil menghapus tugas saat dikonfirmasi 'y'"""
        # Arrange
        main.dummy_tasks = [
            {"id": 1, "title": "Tugas Hapus", "description": "Desk 1", "status": "Belum Selesai", "estimasi_waktu_pengerjaan": 30},
            {"id": 2, "title": "Tugas Lain", "description": "Desk 2", "status": "Selesai", "estimasi_waktu_pengerjaan": 45}
        ]
        # Input 1: ID tugas yang dihapus ("1"), Input 2: Konfirmasi penghapusan ("y")
        mock_input.side_effect = ["1", "y"]

        # Act
        main.hapus_tugas()

        # Assert 1: Jumlah tugas berkurang menjadi 1
        self.assertEqual(len(main.dummy_tasks), 1)
        # Assert 2: Tugas ID 1 sudah tidak ada dalam list
        self.assertFalse(any(task["id"] == 1 for task in main.dummy_tasks))

        # Assert 3: Pesan berhasil muncul
        cetakan = [call[0][0] for call in mock_print.call_args_list]
        self.assertTrue(any("telah dihapus" in teks for teks in cetakan))

    @patch("main.console.print")
    @patch("main.console.input")
    def test_batal_hapus_tugas(self, mock_input, mock_print):
        """Skenario 5: Membatalkan penghapusan tugas saat menjawab selain 'y' (misal 'n')"""
        # Arrange
        main.dummy_tasks = [
            {"id": 1, "title": "Tugas Aman", "description": "Desk 1", "status": "Belum Selesai", "estimasi_waktu_pengerjaan": 30}
        ]
        # Input 1: ID tugas ("1"), Input 2: Konfirmasi pembatalan ("n")
        mock_input.side_effect = ["1", "n"]

        # Act
        main.hapus_tugas()

        # Assert 1: Tugas tetap ada dalam list (tidak terhapus)
        self.assertEqual(len(main.dummy_tasks), 1)
        self.assertEqual(main.dummy_tasks[0]["id"], 1)

        # Assert 2: Pesan pembatalan muncul
        cetakan = [call[0][0] for call in mock_print.call_args_list]
        self.assertTrue(any("Penghapusan dibatalkan." in teks for teks in cetakan))


if __name__ == "__main__":
    unittest.main()