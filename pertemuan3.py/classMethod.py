#class method
class Friends:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Haaloo " + self.name)

p1 = Friends("Maren")
p1.greet()


#with parameters
class Calculator:
    def add(self, x, y):
        return x + y
 
    def multiply(self, x, y):
        return x * y

calc = Calculator()
print(calc.add(7, 9))
print(calc.multiply(6, 8))


#accessing
class Friends:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f"{self.name} is {self.age} years old"

p1 = Friends("Maren", 19)
print(p1.get_info())


#modify properties
class Friends:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def celebrate_birthday(self):
        self.age += 1
        print(f"Happy birthdayy! You are now {self.age}")

p1 = Friends("Maren", 19)
p1.celebrate_birthday()
p1.celebrate_birthday()


#metode __str__()
class Friends:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"

p1 = Friends("Maren", 19)
print(p1)


#multiple methods
class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)
        print(f"Added: {song}")

    def remove_song(self, song):
        if song in self.songs:
          self.songs.remove(song)
          print(f"Removed: {song}")

    def show_songs(self):
        print(f"Playlist '{self.name}':")
        for song in self.songs:
          print(f"- {song}")

my_playlist = Playlist("Favorites")
my_playlist.add_song("Sandiwara Semu")
my_playlist.add_song("Kalibata,13")
my_playlist.show_songs()

