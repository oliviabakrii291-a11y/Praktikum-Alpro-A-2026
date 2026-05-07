'''
Buat sebuah program Python bernama file_manager.py yang berjalan di terminal dan menampilkan
menu utama untuk mengelola file teks (.txt). Program harus bisa membaca, menulis, dan menghapus
file secara interaktif.
'''
import os

'''
#menambah file txt

f = open("catatan.txt", "x")

with open("tugas.txt", "x") as f:
    f.write("\n Belajar Python hari ini ... ")

f = open("jadwal.txt", "x")
'''

#tampilan menu
def tampilkan_menu():
    print("============================") 
    print("PYTHON FILE MANAGER v1.0")
    print("============================")

    print("[1] Read file")
    print("[2] Write file")
    print("[3] Delete file")
    print("[0] Exit")

    pilihan = int(input("Pilih menu: "))
    return pilihan



def tampilkan_file():
    print("------------------------------")
    print("File tersedia:")
    print("[1] catatan.txt")
    print("[2] tugas.txt")
    print("[3] jadwal.txt")

def pilih_file():
    print("------------------------------")
    print("File tersedia:")
    print("[1] catatan.txt")
    print("[2] tugas.txt")
    print("[3] jadwal.txt")

    pilihan = int(input("Pilih file (nomor): "))
    return pilihan


def baca_file(file):
    print(f"--- Isi {file} ---")
    with open(file ) as f :
        print(f.read())


def tulis_file(file):
    with open(file, "a") as f :
        f.write(input(f"masukkan tulisan :"))


def hapus_file(file):

    if os.path.exists ("file_baru.txt"):
        yakin = input("yakin mau hapus?? (y/n)")
        if yakin.lower() == "y" :
            os.remove("file_baru.txt")
    else: 
        print("file tidak ada")



def main():
    while True :
        pilihMenu = tampilkan_menu()
        match pilihMenu :
            case 1 :
                pilihanFile_R =  pilih_file()

                match pilihanFile_R :
                    case 1 :
                        baca_file("catatan.txt")
                    case 2 : 
                        baca_file("tugas.txt")
                    case 3 :
                        baca_file("jadwal.txt")


            case 2 :
                pilihanFile_W =  pilih_file()
           
                match pilihanFile_W :
                    case 1 :
                        tulis_file("catatan.txt")
                    case 2 : 
                        tulis_file("tugas.txt")
                    case 3 :
                        tulis_file("jadwal.txt")
        

            case 3 :
                pilihanFile_D =  pilih_file()

                match pilihanFile_D : 
                
                    case 1 :
                        hapus_file("catatan.txt")
                    case 2 : 
                        hapus_file("tugas.txt")
                    case 3 :
                        hapus_file("jadwal.txt")
            case 0 :
                break
        print("------------------------------")


main()








