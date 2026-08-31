import unittest
from unittest.mock import patch
import main  # Import file main.py Anda


class TestTandaiSelesai(unittest.TestCase):

    @patch("main.console.print")
    def test_daftar_kosong(self, mock_print):
        """Skenario 1: Menguji respon saat daftar tugas kosong"""
        # Arrange
        main.dummy_tasks = []

        # Act
        main.tandai_selesai()

        # Assert
        cetakan = [call[0][0] for call in mock_print.call_args_list]
        self.assertTrue(any("Tidak ada tugas saat ini" in teks for teks in cetakan))

    @patch("main.console.print")
    @patch("main.console.input")
    def test_input_id_bukan_angka(self, mock_input, mock_print):
        """Skenario 2: User menginputkan ID berupa teks/karakter (bukan angka)"""
        # Arrange
        main.dummy_tasks = [
            {"id": 1, "title": "Tugas 1", "description": "Desk 1", "status": "Belum Selesai", "estimasi_waktu_pengerjaan": 30}
        ]
        mock_input.return_value = "abc"

        # Act
        main.tandai_selesai()

        # Assert: Memastikan validasi input_angka berjalan
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
        main.tandai_selesai()

        # Assert: Pesan tidak ditemukan muncul
        cetakan = [call[0][0] for call in mock_print.call_args_list]
        self.assertTrue(any("Tugas dengan ID 99 tidak ditemukan" in teks for teks in cetakan))

    @patch("main.console.print")
    @patch("main.console.input")
    def test_berhasil_tandai_selesai(self, mock_input, mock_print):
        """Skenario 4: Berhasil mengubah status dari 'Belum Selesai' menjadi 'Selesai'"""
        # Arrange
        main.dummy_tasks = [
            {"id": 1, "title": "Tugas 1", "description": "Desk 1", "status": "Belum Selesai", "estimasi_waktu_pengerjaan": 30}
        ]
        mock_input.return_value = "1"

        # Act
        main.tandai_selesai()

        # Assert 1: Status di dummy_tasks berubah
        self.assertEqual(main.dummy_tasks[0]["status"], "Selesai")

        # Assert 2: Pesan berhasil muncul
        cetakan = [call[0][0] for call in mock_print.call_args_list]
        self.assertTrue(any("telah ditandai sebagai Selesai" in teks for teks in cetakan))

    @patch("main.console.print")
    @patch("main.console.input")
    def test_tugas_sudah_selesai_sebelumnya(self, mock_input, mock_print):
        """Skenario 5: Menguji tugas yang memang sudah berstatus 'Selesai'"""
        # Arrange
        main.dummy_tasks = [
            {"id": 1, "title": "Tugas 1", "description": "Desk 1", "status": "Selesai", "estimasi_waktu_pengerjaan": 30}
        ]
        mock_input.return_value = "1"

        # Act
        main.tandai_selesai()

        # Assert 1: Status tetap 'Selesai'
        self.assertEqual(main.dummy_tasks[0]["status"], "Selesai")

        # Assert 2: Pesan peringatan bahwa tugas sudah selesai muncul
        cetakan = [call[0][0] for call in mock_print.call_args_list]
        self.assertTrue(any("sudah berstatus Selesai sebelumnya" in teks for teks in cetakan))


if __name__ == "__main__":
    unittest.main()