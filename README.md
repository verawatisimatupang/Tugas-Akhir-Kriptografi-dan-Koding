# Tugas-Akhir-Kriptografi-dan-Koding
<br />

<a name="readme-top"></a>
<!-- TABLE OF CONTENTS -->
Daftar Isi
  <ol>
    <li><a href="#nama">Nama</a></li>
    <li><a href="#spesifikasi">Spesifikasi</a></li>
    <li><a href="#cara-menjalankan-aplikasi">Cara Menjalankan Aplikasi</a></li>
  </ol>
 
 <!-- Nama -->
## Nama
18220002 - Verawati Esteria S. Simatupang

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Spesifikasi -->
## Spesifikasi
Aplikasi desktop mobile banking sederhana dengan mengimplementasikan SHA-3 untuk autentikasi One Time Password pada saat melakukan registrasi akun dan penarikan tunai
<!-- Cara Menjalankan Aplikasi -->

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Cara Menjalankan Aplikasi
1. Buat database datapengguna
```sh
  CREATE DATABASE datapengguna;
  ```
3. Buat tabel datalogin, datapengguna, dan datatransaksi
```sh
  CREATE TABLE datapengguna (
  nomor_rekening VARCHAR(355),
  email VARCHAR(355),
  username VARCHAR(355),
  password VARCHAR(355),
  pin VARCHAR(50),
  otp VARCHAR(50),
  register_time TIMESTAMP
);
  ```
  
```sh
  CREATE TABLE datalogin (
  username VARCHAR(355),
  password VARCHAR(355),
  login_time TIMESTAMP
);
  ```

```sh
  CREATE TABLE datatransaksi (
  username VARCHAR(355),
  nomor_rekening VARCHAR(355),
  jalur_tarik_tunai VARCHAR(355),
  nominal VARCHAR(355),
  pin VARCHAR(355),
  otp VARCHAR(355),
  cashwithdrawal_time TIMESTAMP
);
  ```
3. Dijalankan melalui file Main.py atau run di cmd yaitu
```sh
  python Main.py
  ```
<p align="right">(<a href="#readme-top">back to top</a>)</p>
