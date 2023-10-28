# Python-Project-Pacmann
Self-service Cashier
Program ini dirancang untuk membantu Andi, pemilik sebuah supermarket besar di Indonesia, dalam meningkatkan proses bisnis dengan mengimplementasikan sistem kasir self-service. Berikut adalah ringkasan singkat dari poin-poin penting dalam projek. 

Latar Belakang Projek:
Andi memiliki sebuah supermarket besar dan berencana untuk meningkatkan proses bisnisnya dengan memperkenalkan sistem kasir self-service.
Sistem ini memungkinkan pelanggan untuk memasukkan barang yang ingin mereka beli, termasuk nama barang, jumlah, dan harga.
Sistem ini memungkinkan pelanggan untuk berbelanja secara online, meskipun mereka tidak berada di toko secara fisik.

Persyaratan:
	•	Program ini bersifat modular, dengan kode yang disimpan dalam sebuah file bernama "SelfServiceCashier.py", dan eksekusi ditangani oleh file "main.py" yang terpisah.
	•	Program ini menggunakan pustaka Pandas untuk visualisasi data dalam format tabel.
	•	Data disimpan dalam bentuk dictionary.
	•	Program ini terdiri dari 9 metode untuk menangani berbagai operasi.

<img width="253" alt="Screenshot 2023-10-28 at 11 48 56 PM" src="https://github.com/S1Jesslyn/Python-Project-Pacmann/assets/132558743/847d4c78-39bf-4a8e-993e-ccbfcb02e854">

Structure
Class: Transaksi

Atribut:
- data_belanja (kamus): Struktur data untuk menyimpan item-item dalam transaksi pelanggan. Setiap item diasosiasikan dengan namanya sebagai kunci, dan nilainya berupa daftar yang berisi:
  - Jumlah barang
  - Harga per item
  - Total harga untuk barang tersebut (kuantitas * harga)

Metode:
1. __init__(self):
	•	Deskripsi: Metode konstruktor untuk menginisialisasi kelas `Transaction`.
	•	Parameter: Tidak ada
	•	Fungsi: Menginisialisasi kamus `data_belanja` yang kosong.

2. tambah_barang(diri, nama, jumlah, harga):
Deskripsi: Metode untuk menambahkan barang ke dalam transaksi.
	•	Parameter:
	⁃	`nama` (string): Nama item.
	⁃	`jumlah` (int): Jumlah item.
	⁃	`harga` (int/float): Harga per item.
	•	Fungsi: Menghitung total harga untuk barang dan menyimpannya di dalam kamus `data_belanja`.

3. update_nama_barang(self, nama, nama_baru):
	•	Deskripsi: Metode untuk memperbarui nama barang dalam transaksi.
	•	Parameter:
	⁃	`nama` (string): Nama item saat ini.
	⁃	`nama_baru` (string): Nama baru untuk item tersebut.
	•	Fungsi: Memperbarui nama barang di dalam kamus `data_belanja`.

4. update_item_qty(self, nama, jumlah_baru):
	•	Deskripsi: Metode untuk memperbarui jumlah item dalam transaksi.
	•	Parameter:
	⁃	`nama` (string): Nama item yang akan diperbarui.
	⁃	`jumlah_baru` (int): Jumlah baru untuk item tersebut.
	•	Fungsi: Memperbarui kuantitas dan total harga untuk item dalam kamus `data_belanja`.

5. update_harga_barang(self, nama, harga_baru):
	•	Deskripsi: Metode untuk memperbarui harga dari sebuah item dalam transaksi.
	•	Parameter:
	⁃	`nama` (string): Nama item yang akan diperbarui.
	⁃	`harga_baru` (int/float): Harga baru untuk item tersebut.
	•	Fungsi: Memperbarui harga dan total harga barang dalam kamus `data_belanja`.

6. hapus_barang(self, nama):
	•	Deskripsi: Metode untuk menghapus item dari transaksi.
	•	Parameter: `nama` (string): Nama item yang akan dihapus.
	•	Fungsi: Menghapus item dari kamus `data_belanja`.

7. setel ulang_transaksi (self):
	•	Deskripsi: Metode untuk menghapus seluruh transaksi, menghapus semua item dari kamus `data_belanja`.
	•	Parameter: Tidak ada
	•	Fungsi: Mengatur ulang transaksi ke kondisi awal.

8. check_order(self):
	•	Deskripsi: Metode untuk memeriksa detail transaksi, memastikan keakuratan pesanan.
	•	Parameter: Tidak ada
	•	Fungsi: Jika ada item dalam transaksi, maka akan menampilkan tabel item, jumlah, harga, dan total harga, serta memberikan umpan balik tentang kebenaran pesanan.

9. total_harga(self):
	•	Deskripsi: Metode untuk menghitung harga total transaksi.
	•	Parameter: Tidak ada
	•	Fungsi: Mengulangi item-item dalam kamus `data_belanja`, menghitung jumlah total pembelian, menerapkan diskon berdasarkan jumlah total, dan mengembalikan pesan dengan harga total akhir, termasuk diskon yang berlaku.

Representasi ini memberikan struktur yang jelas dari kelas 'Transaction', atribut-atributnya, dan tujuan serta fungsionalitas setiap metode.


Test Case
Test 1:
Customer ingin menambahkan dua item baru menggunakan method add item (). Item yang ditambahkan adalah sebagai berikut:
1. Nama Item: Ayam Goreng, Qty: 2, Harga: 20000
2. Nama Item: Pasta Gigi, Qty: 3, Harga: 15000
Expected Output:

<img width="525" alt="Screenshot 2023-10-28 at 11 19 04 PM" src="https://github.com/S1Jesslyn/Python-Project-Pacmann/assets/132558743/ddab3180-ae03-4f4d-a7b3-8b19770176da">
￼
Test case 2
Ternyata Customer salah membeli salah satu item dari belanjaan yang sudah ditambahkan, maka Customer menggunakan method delete _item () untuk menghapus item. Item yang. ingin dihapuskan adalah Pasta Gigi.
Expected Output:

<img width="532" alt="Screenshot 2023-10-28 at 11 21 21 PM" src="https://github.com/S1Jesslyn/Python-Project-Pacmann/assets/132558743/df59ee99-b3fc-441c-83f1-189ea967663e">


Test case 3 
Ternyata setelah dipikir-pikir Customer salah memasukkan item yang ingin dibelanjakan! Daripada menghapusnya satu satu, maka Customer cukup menggunakan method reset_transaction() untuk menghapus semua item yang sudah ditambahkan. 
Expected Output:

<img width="339" alt="Screenshot 2023-10-28 at 11 25 25 PM" src="https://github.com/S1Jesslyn/Python-Project-Pacmann/assets/132558743/46e90106-a25a-4450-82e4-4252ff97be34">
￼
Test case 4 
Setelah Customer selesai berbelanja, akan menghitung total belanja yang harus dibayarkan menggunakan method total_price(). Sebelum mengeluarkan Ouput total belanja akan menampilkan item item yang dibeli. 
Expected Output:

<img width="540" alt="Screenshot 2023-10-28 at 11 28 05 PM" src="https://github.com/S1Jesslyn/Python-Project-Pacmann/assets/132558743/aaf5b3bc-7044-4bdb-80a8-efbce7b0e9f6">

<img width="469" alt="Screenshot 2023-10-28 at 11 37 35 PM" src="https://github.com/S1Jesslyn/Python-Project-Pacmann/assets/132558743/d3a5ee8b-fc90-46b2-86a7-e1e0d03c54e5">


Kesimpulan
Kesimpulannya, proyek kasir-mandiri ini bertujuan untuk menyediakan solusi berbasis Python untuk supermarket untuk meningkatkan pengalaman berbelanja. Proyek ini terdiri dari kelas Transaction yang menawarkan beberapa fitur dan fungsi untuk menangani transaksi pelanggan. Fitur-fitur ini termasuk menambah, memperbarui, dan menghapus barang, memeriksa pesanan, dan menghitung total harga dengan diskon. Proyek ini juga menggunakan library Pandas untuk menampilkan detail barang dalam format tabel.
