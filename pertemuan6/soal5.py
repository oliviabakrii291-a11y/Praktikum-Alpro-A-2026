'''
Soal 5. Class Menu dan Transaksi

Topik: OOP | Estimasi waktu: 20 menit

Deskripsi:
Buat versi OOP dari sistem kasir warung menggunakan dua class sederhana.
Ketentuan Program:
1. Buat class Menu dengan atribut nama dan harga, serta method tampilkan() yang
mencetak informasi menu dalam format: "Nama Menu - Rp harga".
2. Buat class Transaksi dengan atribut total (awalnya 0) dan method tambah(menu,
jumlah) yang menambahkan harga ke total, serta method struk() yang menampilkan
total belanja.
3. Pada program utama, buat minimal 3 objek Menu dan tampilkan semuanya
menggunakan for loop.
4. Buat satu objek Transaksi, minta pengguna memilih menu dan jumlahnya, lalu
panggil method tambah() dan tampilkan struk akhir dengan method struk().
'''

class Menu:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

    def tampilkan(self):
        print(f"{Menu[i][0]} - Rp{Menu[i][1]}")


class Transaksi:
    def __init__(self, total()):
        self.total = total

    def tambah(self, menu, jumlah):
        return self.total
    
    def struk(self):
        print("Struk Harga")

m1 = Menu("Ayam Goreng", 13000)
m2 = Menu("Ayam Saos", 13000)
m3 = Menu("Ayam Bumbu", 13000)