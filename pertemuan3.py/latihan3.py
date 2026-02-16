class Cake:
    def __init__(self, name, colour, prize):
        self.name = name
        self.colour = colour
        self.prize = prize

    def Texture(self):
        print(self.name + "sangat lembut")

    def Taste(self):
        print(self.name + "sangat enak")

p1 = Cake("Nastar", "Kuning", 5000)
p2 = Cake("Donat", "Coklat", 2000)
p3 = Cake("Brownis", "Merah", 7000)

(p1.Texture())
(p1.Taste())
p1.name = "tar"

(p2.Texture())
(p2.Taste())                                                                                                    
(p3.Texture())
(p3.Taste())

