#While Loop

i = 3
while i < 9:
  print(i)
  i += 1


#penggunaan break statement

i = 2
while i < 12:    #menghentikan loop ketika suatu kondisi terpenuhi
  print(i)
  if i == 8:
    break
  i += 2


#penggunaan continue statement

i = 0
while i < 15:
  i += 3
  if i == 9:
    continue
  print(i)


#the Else statement
i = 1
while i <= 5:
  print(i)
  i += 1
else:
  print("kuota sudah penuh")