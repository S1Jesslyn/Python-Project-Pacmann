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


<img width="236" alt="Screenshot 2023-11-13 at 12 24 04 PM" src="https://github.com/S1Jesslyn/Python-Project-Pacmann/assets/132558743/156d3ab1-4bc8-4bdb-8737-cebbced2b298">


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

2. add_item(self, nama, jumlah, harga):
Deskripsi: Metode untuk menambahkan barang ke dalam transaksi.
	•	Parameter:
	⁃	`nama` (string): Nama item.
	⁃	`jumlah` (int): Jumlah item.
	⁃	`harga` (int/float): Harga per item.
	•	Fungsi: Menghitung total harga untuk barang dan menyimpannya di dalam kamus `data_belanja`.

3. update_item_name(self, nama, nama_baru):
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

5. update_item_price(self, nama, harga_baru):
	•	Deskripsi: Metode untuk memperbarui harga dari sebuah item dalam transaksi.
	•	Parameter:
	⁃	`nama` (string): Nama item yang akan diperbarui.
	⁃	`harga_baru` (int/float): Harga baru untuk item tersebut.
	•	Fungsi: Memperbarui harga dan total harga barang dalam kamus `data_belanja`.

6. delete_item(self, nama):
	•	Deskripsi: Metode untuk menghapus item dari transaksi.
	•	Parameter: `nama` (string): Nama item yang akan dihapus.
	•	Fungsi: Menghapus item dari kamus `data_belanja`.

7. reset_transaction (self):
	•	Deskripsi: Metode untuk menghapus seluruh transaksi, menghapus semua item dari kamus `data_belanja`.
	•	Parameter: Tidak ada
	•	Fungsi: Mengatur ulang transaksi ke kondisi awal.

8. check_order(self):
	•	Deskripsi: Metode untuk memeriksa detail transaksi, memastikan keakuratan pesanan.
	•	Parameter: Tidak ada
	•	Fungsi: Jika ada item dalam transaksi, maka akan menampilkan tabel item, jumlah, harga, dan total harga, serta memberikan umpan balik tentang kebenaran pesanan.

9. total_price(self):
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

<img width="516" alt="Screenshot 2023-11-13 at 12 25 52 PM" src="https://github.com/S1Jesslyn/Python-Project-Pacmann/assets/132558743/736f4b0c-4362-4137-8264-6df7463503be">

￼
Test case 2
Ternyata Customer salah membeli salah satu item dari belanjaan yang sudah ditambahkan, maka Customer menggunakan method delete _item () untuk menghapus item. Item yang. ingin dihapuskan adalah Pasta Gigi.
Expected Output:

<img width="531" alt="Screenshot 2023-11-13 at 12 24 55 PM" src="https://github.com/S1Jesslyn/Python-Project-Pacmann/assets/132558743/76e0b94f-f13b-4155-b696-299553570c8d">


Test case 3 
Ternyata setelah dipikir-pikir Customer salah memasukkan item yang ingin dibelanjakan! Daripada menghapusnya satu satu, maka Customer cukup menggunakan method reset_transaction() untuk menghapus semua item yang sudah ditambahkan. 
Expected Output:

<img width="336" alt="Screenshot 2023-11-13 at 12 26 45 PM" src="https://github.com/S1Jesslyn/Python-Project-Pacmann/assets/132558743/a9b73fd2-9826-49c7-af48-783e72357065">

￼
Test case 4 
Setelah Customer selesai berbelanja, akan menghitung total belanja yang harus dibayarkan menggunakan method total_price(). Sebelum mengeluarkan Ouput total belanja akan menampilkan item item yang dibeli. 
Expected Output:

<img width="534" alt="Screenshot 2023-11-13 at 12 27 24 PM" src="https://github.com/S1Jesslyn/Python-Project-Pacmann/assets/132558743/0e73685f-729c-4084-ba35-afc17f265171">

<img width="462" alt="Screenshot 2023-11-13 at 12 27 29 PM" src="https://github.com/S1Jesslyn/Python-Project-Pacmann/assets/132558743/c4b81136-d210-4433-bcec-e5730416034d">


Kesimpulan
Kesimpulannya, proyek kasir-mandiri ini bertujuan untuk menyediakan solusi berbasis Python untuk supermarket untuk meningkatkan pengalaman berbelanja. Proyek ini terdiri dari kelas Transaction yang menawarkan beberapa fitur dan fungsi untuk menangani transaksi pelanggan. Fitur-fitur ini termasuk menambah, memperbarui, dan menghapus barang, memeriksa pesanan, dan menghitung total harga dengan diskon. Proyek ini juga menggunakan library Pandas untuk menampilkan detail barang dalam format tabel.
