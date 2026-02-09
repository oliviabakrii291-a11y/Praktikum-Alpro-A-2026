#penggunaan if

a = 21
b = 27
if b > a:
  print("b lebih besar dari a")



number = 15
if number > 20:
  print("Angka cukup!")


#beberapa pernyataan dalam satu if

umur = 20
if umur >= 18:
  print("Kamu sudah legal")
  print("Kamu sudah bisa bekerja")
  print("Kamu sudah bisa vote")


#elif

a = 99
b = 99
if b > a:
  print("nilai b lebih tinggi dari a")
elif a == b:
  print("nilai a dan b sama")


#multiple elif

nilai = 65

if nilai >= 90:
  print("Nilai: A")
elif nilai >= 80:
  print("Nilai: B")
elif nilai >= 70:
  print("Nilai: C")
elif nilai >= 60:
  print("Nilai: D")



cuaca = 3

if cuaca == 1:
  print("Cerah")
elif cuaca == 2:
  print("Berawan")
elif cuaca == 3:
  print("Mendung")
elif cuaca == 4:
  print("Hujan")
elif cuaca == 5:
  print("Panas")
elif cuaca == 6:
  print("Berangin")
elif cuaca == 7:
  print("Badai")



#else

yoyo = 20
ocen = 22
if ocen > yoyo:
  print("ocen lebih tua dari yoyo")
elif yoyo == ocen:
  print("umur yoyo sama dengan ocen")
else:
  print("umur yoyo lebih tua dari ocen")


yoyo = 20
ocen = 22
if ocen > yoyo:
  print("ocen lebih tua dari yoyo")
else:
  print("umur yoyo lebih tua dari ocen")


username = "pia"

if (username) == "Olivia":
  print(f"Welcome, {username}!")
else:
  print("Error: Username tidak ada")

#shorthand if

a = 100
b = 1000
if a < b: print("a lebih sedikit")


#shorthand if...else

a = 100
b = 1000
print("sedikit") if a > b else print("banyak")



a = 2
b = 3
bigger = a if a > b else b
print("lebih besar", bigger)



a = 500
b = 505
print("A") if a > b else print("=") if a == b else print("B")

#and operator

a = 15
b = 30
c = 45
if a < b and c > a:
  print("kedua kondisi benar")

#or operator

a = 15
b = 30
c = 45
if a > b or b < c:
  print("Setidaknya satu pernyataan benar")

#not operator

a = 33
b = 99
if not a > b:
  print("a tidak sebanyak b")

#gabungan

umur = 20
mahasiswa = True
ada_diskon = True

if (umur < 18 or umur > 65) and not mahasiswa or ada_diskon:
  print("Diskon ada!")



#nested if

x = 29

if x > 10:
  print("diatas 10")
  if x > 20:
    print("diatas 20")
  else:
    print("tidak lebih dari 20")




usia = 25
mahasiswa = False

if usia >= 18:
  if mahasiswa:
    print("Kamu boleh masuk")
  else:
    print("Mana ktp kamu?")
else:
  print("Maaf, kamu tidak bisa masuk")


#pass statement
a = 222
b = 333

if b > a:
  pass

