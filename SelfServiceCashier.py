import pandas as pd

class Transaction:
    def __init__(self):
        self.data_belanja = dict()

    def add_item(self, nama, jumlah, harga):
        try:
           self.data_belanja.update({nama: [jumlah, harga, jumlah * harga]})
        except ValueError:
            print("Ada keselahan pada input!")

    def update_item_name(self,nama, nama_baru):
        try:
            updated_name = self.data_belanja[nama] # membuat variabel sederhana
            self.data_belanja.pop(nama)
            self.data_belanja.update({nama_baru: updated_name})
        except KeyError:
            print("Nama item yang dimasukkan tidak sesuai!")        
    
    def update_item_qty(self, nama, jumlah_baru):
        self.data_belanja[nama][0] = jumlah_baru
        self.data_belanja[nama][2] = jumlah_baru * self.data_belanja[nama][1]

    def update_item_price(self, nama, harga_baru):
        self.data_belanja[nama][1] = harga_baru
        self.data_belanja[nama][2] = harga_baru * self.data_belanja[nama][0]

    def delete_item(self,nama):
        self.nama = nama
        if nama == nama:
            self.data_belanja.pop(nama)

    def reset_transaction(self):
        self.data_belanja.clear()
        print("Semua item berhasil di delete!")

    def check_order(self):
        if(len(self.data_belanja) == 0):
            print("Terdapat Kesalahan Input Data!")
        else:
            data = pd.DataFrame(self.data_belanja).T
            data.columns = [ "Jumlah item", "Harga per item", "Total Harga"]
            data["Total Harga"] = data["Jumlah item"] * data["Harga per item"]
            print(data.to_markdown())

    def total_price(self):
        total = 0
        for i in self.data_belanja.values():
            total += i[2]

        
        if total > 500000:
            total *= 0.9
        elif total > 300000:
            total *= 0.92
        elif total > 200000:
            total *= 0.95

        return f"Total belanja yang harus dibayarkan adalah Rp. {format(total, ',')}"
