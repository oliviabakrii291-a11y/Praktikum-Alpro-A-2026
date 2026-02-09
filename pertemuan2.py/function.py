#membuat  fungsi

def sapaan():
  print("Halo, Pia! Selamat Pagi!")

#memanggil fungsi

def sapaan():
  print("Halo, Pia! Selamat Pagi!")

sapaan()
sapaan()
sapaan()

#return

def sapaan():
  return "Halo,Pia!"

message = sapaan()
print(message)


#return langsung\

def sapaan():
  return "Halo,Pia!"

print(sapaan())

#arguments

def sapaan(fname):
  print(fname + " haiii")

sapaan("pia")
sapaan("sobri")
sapaan("bila")


def sapaan(name): # name adalah parameter
  print("Haloo", name)

sapaan("Pia")   # "Pia" adalah argument


#jumlah argumment

def sapaan(fname, lname):
  print(fname + " " + lname)

sapaan("Olivia", "Bakri")

#nilai parameter default

def nama_teman(name = "friend"):
  print("Haloo", name)

nama_teman("Tipa")
nama_teman("Hera")
nama_teman()
nama_teman("Nadit")


#Keyword Arguments

def hewanKu(animal, name):
  print("aku punya peliharaan", animal)
  print("peliharaan ku", animal + " namanya", name)

hewanKu(animal = "kucing", name = "yoyo")

def hewanKu(animal, name):
  print("aku punya peliharaan", animal)
  print("peliharaan ku", animal + " namanya", name)

hewanKu(name = "yoyo", animal = "kucing")


#argumen posisional

def hewanKu(animal, name):
  print("aku punya peliharaan", animal)
  print("peliharaan ku", animal + " namanya", name)

hewanKu("kucing","yoyo")


#gabungan

def hewanKu(animal, name, age):
  print("aku punya peliharaan", age, "tahun", animal, "namanya", name)

hewanKu("kucing", name = "yoyo", age = 2)

#Passing Different Data Types

def buah_ku(fruits):
  for fruit in fruits:
    print(fruit)

buah_buah = ["cherry", "apple", "kiwi"]
buah_ku(buah_buah)


def my_function(person):
  print("Name:", person["name"])
  print("Age:", person["age"])
  print("Job:", person["job"])

my_person = {"name": "Olivia Bakri", "age": 25, "job": "engineer"}
my_function(my_person)


#return values

def hitungAngka(x, y):
  return x + y

result = hitungAngka(25, 23)
print(result)


#mengembalikan tipe data

def buah_buah():
  return ["kiwi", "mango", "strawberry"]

fruits = buah_buah()
print(fruits[0])
print(fruits[1])
print(fruits[2])


#hanya argumen posisional

def sapaan(name, /):
  print("Halooo", name)

sapaan("oceeennn")

#hanya argumen kata kunci

def sapaan(*, name):
  print("Halooo", name)

sapaan(name = "yoyooo")


#gabungan
def angka(a, b, /, *, c, d):
  return a + b + c + d

result = angka(2, 6, c = 4, d = 10)
print(result)
