#gabisa bilangan desimal dan bilangan negatif


mylist = [170, 45, 75, 90, 802, 24, 2, 66]
print("Original array:", mylist)
radixArray = [[], [], [], [], [], [], [], [], [], []]
maxVal = max(mylist)
exp = 1

while maxVal // exp > 0:

  while len(mylist) > 0:
    val = mylist.pop()
    radixIndex = (val // exp) % 10    #gunanya untuk menentukan index pada radixArray, misal 170 // 1 % 10 = 0, 170 // 10 % 10 = 7, 170 // 100 % 10 = 1
    radixArray[radixIndex].append(val)

  for bucket in radixArray:
    while len(bucket) > 0:
      val = bucket.pop()
      mylist.append(val)

  exp *= 10

print(mylist)

#append tu nambah paling belakang, pop tu ngambil paling belakang
#radix tu ga comparison based sorting, jadi ga perlu dibandingin satu sama lain,
#tapi berdasarkan digitnya
