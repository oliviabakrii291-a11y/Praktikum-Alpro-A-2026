def fizzbuzz_plus(n):
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print ("FizzBuzz")
        elif i % 3 == 0:
            print ("Fizz")
        elif i % 5 == 0:
            print ("Buzz")
        elif i % 7 == 0:
            print ("Seven")
        else:
            print (str(i))
    return result
    
fizzbuzz_plus(15)


def is_password_valid(password):
    if len(password) <= 8:
        return True
    



def hitung_nilai(tugas, uts, uas):
    nilai_akhir = (0.3 * tugas) + (0.3 * uts) + (0.4 * uas)
    return nilai_akhir


