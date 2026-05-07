print("Soal 1 — Daftar Antrean Klinik (Linear Search)")

'''
Cerita
Puskesmas Sehat Bersama menggunakan sistem pencatatan manual berbasis
Python. Setiap pagi, petugas memasukkan nama-nama pasien yang mendaftar
secara berurutan ke dalam sebuah list. Urutan dalam list mencerminkan urutan
kedatangan pasien.
Pada suatu hari, seorang dokter ingin mengetahui apakah pasien bernama
tertentu sudah mendaftar atau belum, sekaligus ingin tahu pasien tersebut
berada di urutan keberapa.
Berikut adalah data pasien yang mendaftar hari ini:
pasien = [
"Budi Santoso", "Siti Rahayu", "Ahmad Fauzi", "Dewi Les
tari",
"Eko Prasetyo", "Fitri Handayani", "Gilang Ramadan", "H
ana Pertiwi",
"Irfan Maulana", "Joko Susilo"
]

Pertanyaan
Buatlah program Python yang:
1. Menggunakan linear search untuk mencari nama pasien
2. Jika pasien ditemukan, tampilkan pesan: "[Nama] ditemukan di urutan ke-[N]."
3. Jika pasien tidak ditemukan, tampilkan pesan: "[Nama] tidak ada dalam daftar
hari ini."
4. Program harus bisa menerima input nama dari pengguna

'''


def linearSearch(arr, targetVal):
  for i in range(len(arr)):
    if arr[i].lower() == targetVal:
      return i
  return -1

pasien = [
"Budi Santoso", "Siti Rahayu", "Ahmad Fauzi", "Dewi Lestari",
"Eko Prasetyo", "Fitri Handayani", "Gilang Ramadan", "Hana Pertiwi",
"Irfan Maulana", "Joko Susilo"
]

nama_pasien = input("Masukkan nama pasien yang dicari : ")

result = linearSearch(pasien, nama_pasien.lower())

if result != -1:
  print(f"{nama_pasien} ditemukan di urutan ke-{result + 1}.")
else:
  print(f"{nama_pasien} tidak ada dalam daftar hari ini.")




print("Soal 2 — Pencarian Nomor Karyawan (BinarySearch)")

'''
Cerita
PT. Maju Bersama memiliki ribuan karyawan. Bagian HRD menyimpan daftar
nomor ID karyawan yang sudah diurutkan dari kecil ke besar dalam sebuah
sistem. Setiap kali ada tamu atau keperluan administratif, petugas perlu
mengecek apakah nomor ID tertentu terdaftar di perusahaan.
Karena datanya sangat banyak, atasan meminta agar pencarian dilakukan
dengan binary search supaya lebih cepat.
Data ID karyawan yang tersimpan:
id_karyawan = [
1021, 1045, 1089, 1102, 1157, 1203, 1245, 1312,
1378, 1401, 1456, 1502, 1567, 1634, 1700
]

Pertanyaan
Buatlah program Python yang:
1. Menggunakan binary search secara manual (tanpa menggunakan fungsi
bawaan seperti bisect )
2. Menerima input berupa nomor ID dari pengguna
3. Jika ID ditemukan, tampilkan: "ID [N] ditemukan! Posisi ke-[P] dalam daftar."
4. Jika ID tidak ditemukan, tampilkan: "ID [N] tidak terdaftar sebagai karyawan."
5. Tampilkan juga berapa kali proses perbandingan dilakukan sebelum
menemukan hasil
'''


def binarySearch(arr, targetVal):
  left = 0
  right = len(arr) - 1
  perbandingan = 0

  while left <= right:
    mid = (left + right) // 2

    perbandingan += 1

    if arr[mid] == targetVal:
      return [mid, perbandingan]

    if arr[mid] < targetVal:
      left = mid + 1
    else:
      right = mid - 1

  return [-1, perbandingan]

id_karyawan = [
1021, 1045, 1089, 1102, 1157, 1203, 1245, 1312,
1378, 1401, 1456, 1502, 1567, 1634, 1700
]

no_id = int(input("Masukkan ID karyawan yang dicari:"))

result = binarySearch(id_karyawan, no_id)

if result[0] != -1:
  print(f" Proses perbandingan : {result[1]} kali")
  print(f" ID {no_id} ditemukan! Posisi ke-{result[0] + 1} dalam daftar.")
else:
  print(f"ID {no_id} tidak terdaftar sebagai karyawan.")





print("Soal 3 — Sistem Rekomendasi Buku Perpustakaan (Gabungan + Analisis)")

'''
Cerita
Perpustakaan Kota Digital memiliki koleksi buku yang disimpan dalam dua
kategori:
Rak A — Buku disimpan tidak berurutan (sesuai urutan masuk)
Rak B — Buku disimpan berurutan berdasarkan kode buku (sudah
diurutkan)
Seorang pengunjung ingin mencari buku dengan kode tertentu. Sistem harus
menentukan algoritma mana yang tepat untuk setiap rak, dan memberikan
hasil pencarian.
rak_a = ["BK-045", "BK-012", "BK-078", "BK-033", "BK-091",
"BK-027", "BK-056"]
rak_b = ["BK-011", "BK-023", "BK-035", "BK-047", "BK-059",
"BK-071", "BK-083", "BK-095"]

Pertanyaan
Buatlah program Python yang:

1. Mencari kode buku di Rak A menggunakan linear search
2. Mencari kode buku yang sama di Rak B menggunakan binary search
3. Tampilkan hasil pencarian dari kedua rak
4. Tampilkan kesimpulan: di rak mana buku ditemukan (jika ada)
Setelah membuat program, jawab pertanyaan analisis di bawah ini (tulis
sebagai komentar # di dalam kode):
a) Mengapa binary search tidak bisa langsung digunakan di Rak A?
b) Jika Rak B memiliki 1.000 buku, berapa maksimal langkah yang
dibutuhkan binary search?
c) Jika Rak A memiliki 1.000 buku, berapa maksimal langkah yang
dibutuhkan linear search?
'''

rak_a = ["BK-045", "BK-012", "BK-078", "BK-033", "BK-091",
"BK-027", "BK-056"]
rak_b = ["BK-011", "BK-023", "BK-035", "BK-047", "BK-059",
"BK-071", "BK-083", "BK-095"]

kode_buku = input("Masukkan kode buku yang dicari: ")


def linearSearch(arr, targetVal):
  print("Mencari di Rak A (Linear Search)...")
  for i in range(len(arr)):
    if arr[i] == targetVal:
      return i
  return -1

result_a = linearSearch(rak_a, kode_buku)

if result_a != -1:
  print(f"{kode_buku} ditemukan di Rak A pada posisi ke-{result_a + 1}.")
  print("Kesimpulan: Buku ditemukan di Rak A.")
else:
  print(f"{kode_buku} tidak ditemukan di Rak A.")
  print("Kesimpulan: Buku tidak ditemukan di Rak A.")



def binarySearch(arr, targetVal):
  print("Mencari di Rak B (Binary Search)...")
  left = 0
  right = len(arr) - 1

  while left <= right:
    mid = (left + right) // 2

    if arr[mid] == targetVal:
      return mid

    if arr[mid] < targetVal:
      left = mid + 1
    else:
      right = mid - 1

  return -1


result_b = binarySearch(rak_b, kode_buku)

if result_b != -1:
  print(f"{kode_buku} ditemukan di Rak B pada posisi ke-{result_b + 1}.")
  print("Kesimpulan: Buku ditemukan di Rak B.")
else:
  print(f"{kode_buku} tidak ditemukan di Rak B.")
  print("Kesimpulan: Buku tidak ditemukan di Rak B.")

