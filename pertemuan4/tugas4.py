#TUGAS 4 ALPRO
#Sistem Regristrasi Peserta Event


#nama
class Nama_Error(Exception) :
    def __init__ (self, nama):
        self.nama = nama
        super().__init__(f"Nama {nama} terlalu pendek! Minimal 3 karakter ")

#umur
class Umur_Error(Exception):
    def __init__ (self, umur):
        self.umur = umur
        super().__init__(f"Umur {umur} tidak memenuhi syarat (17-60 tahun).")

#email
class Email_Error(Exception) :
    def __init__ (self, email):
        self.email = email
        super().__init__(f"email {email} tidak valid! Harus mengandung '@' dan '.'.")

#nomor hp
class Nomor_Error(Exception) :
    def __init__ (self, nomor):
        self.nomor = nomor
        super().__init__(f"No HP tidak valid! Harus 10-13 digit angka.")


#validasi

#validasi nama
def cek_nama(nama):
        if len(nama) < 3 :
            raise Nama_Error(nama)
        return True

#validasi umur def cek_umur(umur):
def cek_umur(umur):
        if umur < 17 or umur > 60 :
            raise Umur_Error(umur)
        return True

#validasi email
def cek_email(email):
        if '@' in email :
            pass
        else :
            raise Email_Error(email)
        return True

#validasi nomor hp
def cek_nomor(nomor):
        if 10 <= len(nomor) <=13 :
            pass
        else : 
            raise Nomor_Error(nomor)
        return True



print("=== REGISTRASI PESERTA SEMINAR ===")

#pengecekan input
try:
    while True :
        try :
            nama = input("Nama lengkap : ")
            namaValid = cek_nama(nama)

        except Nama_Error as e :
            print (F"[ERROR] {e}" ) 
        else : 
            break

    while True :
        try :
            umur = int(input("Umur : "))
            umurValid = cek_umur(umur)

        except ValueError :
            print("masukkan bilangan bulat")
        except Umur_Error as e :
            print (F"[ERROR] {e}" ) 
        else : 
            break

    while True :
        try :
            email = input("Email : ")
            emailValid = cek_email(email)

        except Email_Error as e :
            print (F"[ERROR] {e}" ) 
        else : 
            break

    while True :
        try :
            nomor = input("Nomor : ")
            nomorValid = cek_nomor(nomor)

        except Nomor_Error as e :
            print (F"[ERROR] {e}" ) 
        else : 
            break

finally:
    print("Proses input selesai.")


print(f"""
=== DATA PESERTA ===
Nama    : {nama}
Umur    : {umur}
Email   : {email}
No HP   : {nomor}
Status  : TERDAFTAR
""")




