#the self parameter
class Cakes:
  def __init__(self, name, price):
    self.name = name
    self.price = price

  def taste(self):
    print("haloo", self.name + " enak sekali")  

p1 = Cakes("Cupcakes", 3000)
p1.taste()


#bisa juga tidak menggunakan self
class Cakes:
  def __init__(myCakes, name, price):
    myCakes.name = name
    myCakes.price = price

  def taste(myCakes):
    print("haloo", myCakes.name + " enak sekali")  

p1 = Cakes("Cupcakes", 3000)
p1.taste()


#calling methods with myself
class Cakes:
    def __init__(self, name):
        self.name = name 
    
    def taste(self):
        return "haloo "  + self.name + " ini enak sekali"
 
    def greet(self):
        massage = self.taste()
        print(massage + " Selamat menikmati.")

p1 = Cakes("Cupcakes")
p1.greet()






