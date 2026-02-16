#__init__() method
class Cakes:
  def __init__(self, name, price):
    self.name = name
    self.price = price

p1 = Cakes("Cupcakes", 3000)

print(p1.name)
print(p1.price)


#Devault Values
class Cakes:
  def __init__(self, name, price=3000):
    self.name = name
    self.price = price

p1 = Cakes("Cupcakes")
p2 = Cakes("Lapis Legit", 5000)

print(p1.name, p1.price)
print(p2.name, p2.price)


#multiple parameters
class Cakes:
  def __init__(self, name, price, colour, size):
    self.name = name
    self.price = price
    self.colour = colour
    self.size = size

p1 = Cakes("Cupcakes", 3000, "Brown", "Medium")

print(p1.name)
print(p1.price)
print(p1.colour)
print(p1.size)
