#class properties
'''
class Animals:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Animals("Yoyo", 3)

print(p1.name)
print(p1.age)
'''

#access
'''
class Animals:
  def __init__(self, name, type):
    self.name = name
    self.type = type

a1 = Animals("Yoyo", "Cat")

print(a1.name)
print(a1.type)
'''

#modify
'''
class Animals:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
       print("haloo ini kucingku " + self.name)

a1 = Animals("Yoyo", 3)
a1.age = 2.5

print(a1.age)
'''
'''
class Animals:
  species = "Cat"  # Class property

  def __init__(self, name):
    self.name = name  # Instance property

p1 = Animals("Yoyo")
p2 = Animals("Cimol")

print(p1.name)
print(p2.name)
print(p1.species)
print(p2.species)
'''

#modify class
'''
class Animals:
    cat = ""

    def __init__(self, name):
        self.name = name

p1 = Animals("Yoyo")
p2 = Animals("Moli")

Animals.cat = "Anggora"

print(p1.cat)
print(p2.cat)
'''

#add properties
class Animals:
  def __init__(self, name):
    self.name = name

p1 = Animals("Yoyo")

p1.age = 2
p1.colour = "Yellow"

print(p1.name)
print(p1.age)
print(p1.colour)
