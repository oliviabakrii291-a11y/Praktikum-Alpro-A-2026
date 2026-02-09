#python match
'''
match digunakan untuk menjalankan tindakan yang berbeda 
berdasarkan nilai atau kondisi yang berbeda
dengan cara mencocokkan nilai tersebut ke dalam beberapa pola menggunakan case
'''

'''
match expression:
  case x:
    code block
  case y:
    code block
  case z:
    code block
    '''


name = 4
match name:
  case 1:
    print("Cemon")
  case 2:
    print("Ciki")
  case 3:
    print("Cemon")
  case 4:
    print("Yoyo")
  case 5:
    print("Moli")
  case 6:
    print("Ciko")
  case 7:
    print("Bams")


name = 4
match name:
  case 6:
    print("ada yoyo")
  case 7:
    print("ada ocen")
  case _:
    print("dimana cemon?")



month = 5
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")
    