import unittest
from unittest.mock import patch
import main  # Meng-import file main.py Anda


class TestLihatSemuaTugas(unittest.TestCase):

    @patch("main.console.print")
    def test_daftar_kosong(self, mock_print):
        """Skenario 1: Membandingkan output saat daftar tugas kosong ([])"""
        # 1. Arrange (Kosongkan daftar tugas)
        main.dummy_tasks = []

        # 2. Act (Jalankan fungsi)
        main.lihat_semua_tugas()

        # 3. Assert (Cek pemanggilan console.print)
        mock_print.assert_called_once()
        output_aktual = mock_print.call_args[0][0]
        output_diharapkan = "Tidak ada tugas saat ini"

        self.assertIn(output_diharapkan, output_aktual)

    @patch("main.console.print")
    def test_daftar_satu_item(self, mock_print):
        """Skenario 2: Membandingkan jumlah baris output saat ada 1 tugas"""
        # 1. Arrange
        main.dummy_tasks = [
            {
                "id": 1,
                "title": "Tugas 1",
                "description": "Deskripsi 1",
                "status": "Belum Selesai",
                "estimasi_waktu_pengerjaan": 30,
            }
        ]

        # 2. Act
        main.lihat_semua_tugas()

        # 3. Assert
        tabel_hasil = mock_print.call_args[0][0]
        jumlah_baris_aktual = len(tabel_hasil.rows)
        jumlah_baris_diharapkan = 1

        self.assertEqual(jumlah_baris_aktual, jumlah_baris_diharapkan)

    @patch("main.console.print")
    def test_daftar_banyak_item(self, mock_print):
        """Skenario 3: Membandingkan jumlah baris output saat ada 3 tugas"""
        # 1. Arrange
        main.dummy_tasks = [
            {
                "id": 1,
                "title": "Tugas 1",
                "description": "Desk 1",
                "status": "Belum Selesai",
                "estimasi_waktu_pengerjaan": 30,
            },
            {
                "id": 2,
                "title": "Tugas 2",
                "description": "Desk 2",
                "status": "Selesai",
                "estimasi_waktu_pengerjaan": 45,
            },
            {
                "id": 3,
                "title": "Tugas 3",
                "description": "Desk 3",
                "status": "Belum Selesai",
                "estimasi_waktu_pengerjaan": 60,
            },
        ]

        # 2. Act
        main.lihat_semua_tugas()

        # 3. Assert
        tabel_hasil = mock_print.call_args[0][0]
        jumlah_baris_aktual = len(tabel_hasil.rows)
        jumlah_baris_diharapkan = 3

        self.assertEqual(jumlah_baris_aktual, jumlah_baris_diharapkan)


if __name__ == "__main__":
    unittest.main()