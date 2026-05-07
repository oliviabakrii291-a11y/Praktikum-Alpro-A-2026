'''
#Soal 2. Menghitung Total Belanja

Topik: While Loop, For Loop | Estimasi waktu: 20 menit

Deskripsi:
Kembangkan program Soal 1 agar pelanggan dapat memesan lebih dari satu item dan
program menghitung total harga seluruh pesanan.
Ketentuan Program:
1. Gunakan while loop agar pelanggan dapat terus menambah pesanan. Loop berhenti
ketika pelanggan memasukkan angka 0.
2. Simpan setiap pesanan ke dalam sebuah list berisi nama menu dan jumlah porsi.
3. Setelah selesai memesan, tampilkan daftar pesanan menggunakan for loop beserta
subtotal tiap item.
4. Tampilkan total harga keseluruhan di bagian akhir.
'''


menu = [["Nasi Uduk", 13000], 
        ["Ayam Geprek", 12000], 
        ["Teh Es", 5000], 
        ["Ikan Bakar", 13000],
        ["Telur Sambal", 12000]]

for i in range(len(menu)):
    print(f"{i+1}. {menu[i][0]} - Rp{menu[i][1]}")


pesanan = []
total_harga = 0


while True:

    no_order = int(input("Masukkan nomor menu (0 untuk selesai): "))

    if no_order == 0:
        break
    elif no_order <= len(menu):
        jumlah_porsi = int(input("Masukkan jumlah porsi: "))
        nama_menu = menu[no_order - 1][0]
        harga_menu = menu[no_order - 1][1]
        subtotal = harga_menu * jumlah_porsi
        pesanan.append((nama_menu, jumlah_porsi, subtotal))
        total_harga += subtotal
    else:
        print("Error! Nomor menu tidak tersedia!")

print("\nDaftar Pesanan:")
for item in pesanan:
    print(f"{item[0]} x {item[1]} = Rp{item[2]}")

