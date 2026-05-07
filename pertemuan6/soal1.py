'''
#Soal 1. Menampilkan Menu Warung

Topik: For Loop, If-Else | Estimasi waktu: 15 menit

Deskripsi:
Buat program untuk menampilkan daftar menu warung dan meminta pelanggan memilih
satu menu.
Ketentuan Program:
1. Buat list menu berisi 5 item makanan/minuman beserta harganya, contoh: [["Nasi
Goreng", 15000], ["Es Teh", 5000], ...].
2. Tampilkan seluruh menu beserta harga menggunakan for loop dengan penomoran.
3. Minta pengguna memasukkan nomor menu yang dipilih.
4. Gunakan if-else untuk memvalidasi input: jika nomor tidak valid, tampilkan pesan
error; jika valid, tampilkan nama dan harga menu yang dipilih.

'''

menu = [["Nasi Uduk", 13000], 
        ["Ayam Geprek", 12000], 
        ["Teh Es", 5000], 
        ["Ikan Bakar", 13000],
        ["Telur Sambal", 12000]]

for i in range(len(menu)):
    print(f"{i+1}. {menu[i][0]} - Rp{menu[i][1]}")
    


no_order = int(input("Masukkan nomor menu: "))

if no_order == 1:
    print("Nasi Uduk", 13000) 
elif no_order == 2:
    print("Ayam Geprek", 12000)
elif no_order == 3:
    print("Teh Es", 5000)
elif no_order == 4:
    print("Ikan Bakar", 13000)
elif no_order == 5:
    print("Telur Sambal", 12000)
else:
    print("Error! Nomor menu tidak tersedia!")

