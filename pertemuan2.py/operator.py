#operator
#digunakan untuk melakukan operasi pada nilai variabel

print(3+7)
sum1 = 25 + 25       # 50 (25 + 25)
print(sum1)
sum2 = sum1 + 150    # 200 (50 + 150)
print(sum2)
sum3 = sum1 + sum2   # 250 (50 + 200)
print(sum3)



#Arithmetic Operators
x = 12
y = 3

print(x + y)    #tambah
print(x - y)    #kurang
print(x * y)    #kali
print(x / y)    #pembagian yang menghasilkan nilai float
print(x % y)    #sisa bagi(modulus)
print(x ** y)   #eksponen
print(x // y)   #pembagian yang manghasilkan nilai int


#Assignment Operators
#digunakan untuk menetapkan nilai ke variabel
x = 6           #x = 6

print(x)       
x += 2	        #x = x + 2  	   
print(x)      
x -= 2	        #x = x - 2	
print(x) 
x *= 2	        #x = x * 2	
print(x) 
x /= 2	        #x = x / 2	
print(x) 
x %= 2	        #x = x % 2	
print(x) 
x //= 2	        #x = x // 2	
print(x) 
x **= 2     	#x = x ** 2	
print(x) 



x = 2           #x = 2

x &= 2	        #x = x & 2	
print(x) 
x |= 2	        #x = x | 2	
print(x) 
x ^= 2	        #x = x ^ 2	
print(x) 
x >>= 2	        #x = x >> 2	
print(x) 
x <<= 2	        #x = x << 2	
print(x) 



#operator walrus
#menetapkan variabel sekaligus

numbers = [4, 5, 6, 7, 8, 9]

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")


#Python Comparison Operators

x = 6
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

#bisa menggabung operator
x = 9

print(1 < x < 10)
print(1 > x > 10)



#Python Logical Operators
x = 6
print(1 < x and x < 10)

print(x > 0 and x < 10)

print(x < 5 or x > 10)

print(not(x > 3 and x < 10))


#Python Identity Operators

'''Operator identitas digunakan untuk membandingkan objek, 
bukan apakah objek tersebut sama, 
tetapi apakah objek tersebut benar-benar objek yang sama,
dengan lokasi memori yang sama
'''



x = ["cherry", "kiwi"]
y = ["cherry", "kiwi"]
z = x

print(x is z)
print(x is y)
print(x == y)


x = ["cherry", "kiwi"]
y = ["cherry", "kiwi"]
print(x is not y)


#perbedaan is dengan ==
x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)
print(x is y)


#Membership Operators
#Operator keanggotaan digunakan untuk menguji 
#apakah suatu urutan terdapat dalam suatu objek
fruits = ["cherry", "kiwi", "mango"]

print("kiwi" in fruits)
print("apple" in fruits)


fruits = ["cherry", "kiwi", "mango"]

print("pineapple" not in fruits)


#Membership in Strings
text = "Halo teman-teman..."

print("H" in text)
print("teman" in text)
print("teman" not in text)
print("hai" not in text)


#bitwise operators
#bandingkan bilangan biner(0 dan 1)

#operator & (AND)

print(9 & 5)


#operator | (OR)

print(9 | 5)



#operator ^ (XOR)

print(9 ^ 5)



print((6 + 3) - (6 + 3))

print(100 + 5 * 3)

print(5 + 4 - 7 + 3)

