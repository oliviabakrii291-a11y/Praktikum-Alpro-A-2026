'''
Struktur folder skripsimu direpresentasikan sebagai dictionary bertingkat
(nested dict). Setiap key adalah nama item:
Jika value-nya dict → itu adalah folder
Jika value-nya int → itu adalah file dengan ukuran dalam KB



'''

'''
struktur = {
    "Skripsi_Aqil": {
        "Bab_1": {
            "pendahuluan.docx": 45,
            "latar_belakang.docx": 62
    },

    "Bab_2": {
        "landasan_teori.docx": 118,
        "referensi": {
            "paper_A.pdf": 340,
            "paper_B.pdf": 210
        }
    },

    "Bab_3": {
        "metodologi.docx": 89,
        "diagram": {
            "flowchart.png": 512,
            "erd.png": 278,
            "arsitektur": {
                "sistem.png": 430
            }
        }
    },
    "sidang": {
        "presentasi.pptx": 2048,
        "catatan_revisi.txt": 15    
    },
    "README.txt": 8
    }
}
'''


'''
Tugas A — Hitung Total Ukuran
Kamu ingin tahu berapa total ukuran (KB) seluruh file dalam folder skripsimu,
termasuk file yang ada di dalam subfolder manapun.
Buat fungsi:
def total_ukuran(folder: dict) -> int:
...
Contoh output yang diharapkan:
Total ukuran skripsi: 4155 KB

💡 Pikirkan: Apa yang kamu lakukan saat menemukan sebuah folder? Apa
yang kamu lakukan saat menemukan sebuah file?
'''

struktur = {
    "Skripsi_Aqil" : {
        "Bab_1": {
            "pendahuluan.docx": 45,
            "latar_belakang.docx": 62
        },
        "Bab_2": {
            "landasan_teori.docx": 118,
            "referensi": {
                "paper_A.pdf": 340,
                "paper_B.pdf": 210
            }
        }, 
        "Bab_3": {
            "metodologi.docx": 89,
            "diagram": {
                "flowchart.png": 512,
                "erd.png": 278,
                "arsitektur": {
                    "sistem.png": 430
                }
            }
        },
        "sidang": {
            "presentasi.pptx": 2048,
            "catatan_revisi.txt": 15
        },
        "README.txt": 8
    }
}


def total_ukuran(folder: dict) -> int:
    total = 0
    for key, value in folder.items():
        if isinstance(value, dict):
            total += total_ukuran(value)
        else:
            total += value
    return total

print("Total ukuran file dalam struktur skripsi:", total_ukuran(struktur), "KB")


'''
Tugas B — Hitung Jumlah File
Kamu penasaran, ada berapa file di seluruh folder skripsimu?
Buat fungsi:

Latihan Praktikum 12 - Algoritma Pemrograman 2

def hitung_file(folder: dict) -> int:
...

Contoh output yang diharapkan:
Jumlah file: 12 file

💡 Pikirkan: Kapan kamu menambah 1 ke hitungan? Kapan kamu menelusuri
lebih dalam?
'''


def hitung_file(folder: dict) -> int:
    count = 0
    for key, value in folder.items():
        if isinstance(value, dict):
            count += hitung_file(value)
        else:
            count += 1
    return count

print("Jumlah file:", hitung_file(struktur))


'''
Tugas C — Cari File Terbesar (30 poin)
Kamu curiga ada satu file yang ukurannya sangat besar dan memakan storage.
Buat fungsi yang mencari nama file dengan ukuran terbesar beserta
ukurannya.
Buat fungsi:
def cari_terbesar(folder: dict) -> tuple:
# Kembalikan (nama_file, ukuran_kb)
...
Contoh output yang diharapkan:
File terbesar: presentasi.pptx (2048 KB)

💡 Tantangan: Bagaimana cara membandingkan file di level yang berbeda-
beda? Kamu perlu membawa informasi "kandidat terbaik" selama rekursi

berlangsung.
'''



def cari_terbesar(folder: dict) -> tuple:

    terbesar = ("", 0)
    for key, value in folder.items():
        if isinstance(value, dict):
            kandidat = cari_terbesar(value)
            if kandidat[1] > terbesar[1]:
                terbesar = kandidat
        else:
            if value > terbesar[1]:
                terbesar = (key, value)
    return terbesar

print("File terbesar:", cari_terbesar(struktur))


'''
Tugas D — Cetak Struktur Folder
Kamu ingin mencetak seluruh isi folder seperti tampilan tree di terminal —
dengan indentasi yang menunjukkan kedalaman setiap item.
Buat fungsi:

Latihan Praktikum 12 - Algoritma Pemrograman 3

def tampilkan_tree(folder: dict, nama: str = "root", level:
int = 0):
...
'''



def tampilkan_tree(folder: dict, level: int = 0):
    indent = "    " * level
    
    for key, value in folder.items():
        if isinstance(value, dict):
            print(f"{indent}📁 {key}")
            tampilkan_tree(value, level + 1)
        else:
            print(f"{indent}📄 {key} ({value} KB)")


tampilkan_tree(struktur)


'''
Contoh output yang diharapkan:
📁 Skripsi_Aqil
📁 Bab_1
📄 pendahuluan.docx (45 KB)
📄 latar_belakang.docx (62 KB)
📁 Bab_2
📄 landasan_teori.docx (118 KB)
📁 referensi
📄 paper_A.pdf (340 KB)
📄 paper_B.pdf (210 KB)
...
📄 README.txt (8 KB)
'''
