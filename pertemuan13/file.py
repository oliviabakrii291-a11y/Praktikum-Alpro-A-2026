
'''
import time
f = open("contoh.txt", "rt")  #r = read, t = text

print(f.read())

#f.close() #menutup file setelah selesai digunakan


with open("contoh.txt", "rt") as f:
    print(f.read())

with open("contoh.txt", "rt") as f:
    print(f.read(2))


with open("contoh.txt", "rt") as f:
    print(f.readline(2))




with open("contoh.txt", "a") as f:
  f.write("\nNIM : 25071103083")

time.sleep(1)

with open("contoh.txt") as f:
  print(f.read())

'''

'''
with open("contoh.txt", "x") as f:
    pass
'''    


import os
'''
os.remove("file_baru.txt")
'''

if os.path.exists("file_baru.txt"):
  os.remove("file_baru.txt")
else:
  print("The file does not exist")

