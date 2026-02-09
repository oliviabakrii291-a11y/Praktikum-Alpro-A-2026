#for loop

colour = ["red", "black", "purple"]
for x in colour:
  print(x)

#in string

for x in "beautiful":
  print(x)


#break

colour = ["red", "black", "purple"]
for x in colour:
  print(x)
  if x == "black":
    break

#continue

colour = ["red", "black", "purple"]
for x in colour:
  if x == "red":
    continue
  print(x)


#range()

for x in range(5):
  print(x)


#pakai angka di range()

for x in range(2, 10):
  print(x)

#tambah parameter ketiga

for x in range(2, 20, 2):
  print(x)


#else
for x in range(8):
  print(x)
else:
  print("SELESAI!")

