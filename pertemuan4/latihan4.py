#Soal 1

angka_list = [10, 20, 30]
try:
    idx = int(input('Masukkan index (0-2): '))
    print(f'Nilai: {angka_list[idx]}')
except ValueError:
    print('Harus berupa angka bulat!')
except IndexError:
    print('Index di luar jangkauan!')
finally:
    print('Selesai.')

'''
a. angka nol
Output:
Masukkan index (0-2): 0
Nilai: 10
Selesai.

b. huruf
Output:
Masukkan index (0-2): A
Harus berupa angka bulat!
Selesai.

c. angka negatif
Output:
Masukkan index (0-2): -2
Nilai: 20
Selesai.
'''

#Soal 2

try:
    number1 = int(input('Masukkan angka ke-1: '))
    number2 = int(input('Masukkan angka ke-2: '))
    print(f'Hasil pembagian: {number1 / number2}')

except ValueError:
    print('Harus berupa angka bulat!')
except ZeroDivisionError:
    print('Tidak bisa dibagi dengan nol!')
finally:   
    print('Selesai.')

'''
a. angka sesuai
Output:
Masukkan angka ke-1: 4
Masukkan angka ke-2: 8
Hasil pembagian: 0.5
Selesai.

b. bukan bilangan bulat/ ValueError
Output:
Masukkan angka ke-1: 2.5
Harus berupa angka bulat!
Selesai.

c. angka nol/ ZeroDivisionError:
Output:
Masukkan angka ke-1: 2
Masukkan angka ke-2: 0
Tidak bisa dibagi dengan nol!
Selesai.

'''