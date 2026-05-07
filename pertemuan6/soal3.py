'''
Soal 3. Proses Pembayaran dan Kembalian

Topik: While Loop, If-Else | Estimasi waktu: 20 menit

Deskripsi:
Setelah total belanja diketahui, kasir perlu memproses pembayaran dari pelanggan dan
memberikan kembalian.
Ketentuan Program:
1. Minta pengguna menginput total belanja, kemudian masukkan jumlah uang yang
dibayarkan.
2. Gunakan while loop untuk memastikan uang yang dibayarkan tidak kurang dari total
belanja. Tampilkan pesan error dan minta input ulang jika kurang.
3. Hitung kembalian dan tampilkan ringkasan transaksi: total belanja, uang dibayar, dan
kembalian.
4. Gunakan if-else untuk menampilkan pesan: "Uang pas, tidak ada kembalian" jika
kembalian = 0, atau "Kembalian Anda: Rp ..." jika ada kembalian.
'''

total = int(input("Masukkan total belanja: "))
byr = int(input("Masukkan uang: "))

while byr < total:
    print("Error! Uang tidak cukup!")