# Dokumentasi Aplikasi To-Do List CLI & Unit Testing

Dokumentasi lengkap untuk aplikasi **To-Do List CLI** berbasis Python dan framework pengujian **`unittest`**. Aplikasi ini dirancang untuk mengelola daftar tugas harian menggunakan tampilan terminal interaktif yang dipercantik dengan modul `rich`.

---

## 📋 Daftar Isi
1. [Struktur Proyek](#-struktur-proyek)
2. [Prasyarat & Instalasi](#-prasyarat--instalasi)
3. [Penjelasan Kode Utama (`main.py`)](#-penjelasan-kode-utama-mainpy)
4. [Penjelasan Script Pengujian (Unit Test)](#-penjelasan-script-pengujian-unit-test)
   - [Pengujian `lihat_semua_tugas()`](#1-pengujian-lihat_semua_tugas)
   - [Pengujian `tambah_tugas()`](#2-pengujian-tambah_tugas)
   - [Pengujian `tandai_selesai()`](#3-pengujian-tandai_selesai)
   - [Pengujian `hapus_tugas()`](#4-pengujian-hapus_tugas)
5. [Cara Menjalankan Aplikasi dan Test Script](#-cara-menjalankan-aplikasi-dan-test-script)

---

## 📁 Struktur Proyek

```text
todo-app/
│
├── main.py                     # Source code utama aplikasi To-Do List
├── test_lihat_semua_tugas.py   # Test script untuk fitur lihat semua tugas
├── test_tambah_tugas.py        # Test script untuk fitur tambah tugas
├── test_tandai_selesai.py      # Test script untuk fitur tandai selesai
└── test_hapus_tugas.py         # Test script untuk fitur hapus tugas
