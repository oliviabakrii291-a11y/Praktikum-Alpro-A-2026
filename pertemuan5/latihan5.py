#MATRIKS
'''
A = [[5, 3, 1],
    [2, 8, 4],
    [6, 0, 7]]

B = [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]
'''


'''
a. Menjumlahkan matriks A dan B, simpan hasilnya dalam variabel C_tambah
'''
print("\nsoal nomor 1")
def tambah_matriks(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        print('Error: ukuran matriks tidak sama')
        return None

    baris, kolom = len(A), len(A[0])
    hasil = [[A[i][j] + B[i][j] for j in range(kolom)] for i in
range(baris)]
    return hasil

A = [[5, 3, 1],
    [2, 8, 4],
    [6, 0, 7]]

B = [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]
c_tambah = tambah_matriks(A, B)
for baris in c_tambah:
    print(baris)




'''
b. Mengurangkan matriks A dikurangi B, simpan dalam variabel C_kurang
'''
print("\nsoal nomor 2")
def kurang_matriks(A, B):
    baris, kolom = len(A), len(A[0])
    hasil = [[A[i][j] - B[i][j] for j in range(kolom)] for i in
range(baris)]
    return hasil

A = [[5, 3, 1],
    [2, 8, 4],
    [6, 0, 7]]

B = [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]
c_kurang = kurang_matriks(A, B)
for baris in c_kurang:
    print(baris)


'''
c. Mengalikan setiap elemen matriks A dengan skalar k = 4 , simpan dalam
C_skalar
'''
print("\nsoal nomor 3")
def kali_skalar(matriks, k):
    hasil = []
    for baris in matriks:
        baris_baru = [elemen * k for elemen in baris]
        hasil.append(baris_baru)
    return hasil

A = [[5, 3, 1],
    [2, 8, 4],
    [6, 0, 7]]

B = [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]
c_skalar = kali_skalar(A, 4)
for baris in c_skalar:
    print(baris)



'''
d. Menampilkan ketiga hasil dengan format rapi baris per baris
'''
'''
soal nomor 1
[6, 5, 4]
[6, 13, 10]
[13, 8, 16]

soal nomor 2
[4, 1, -2]
[-2, 3, -2]
[-1, -8, -2]

soal nomor 3
[20, 12, 4]
[8, 32, 16]
[24, 0, 28]
'''