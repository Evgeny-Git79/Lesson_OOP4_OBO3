#Дополнительно:
#Попробуйте добавить дополнительные функции в вашу программу, такие как сохранение информации
#о зоопарке в файл и возможность её загрузки, чтобы у вашего зоопарка было "постоянное состояние"
#между запусками программы.

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def make_sound (self):
        pass
    def make_eat (self):
        print (f"{self.name} кушает")

class Bird(Animal):
    def make_sound(self):
        print ("Chik chirik")


class Mammal(Animal):
   def make_sound(self):
        print("Moo")


class Reptile(Animal):
    def make_sound(self):
        print("Shhh")

class ZooKeeper():
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        print (f"Сотрудник кормит {animal.name}")

class Veterinarian():
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        print (f"Сотрудник лечит {animal.name}")

class Zoo:
    def __init__(self, name):
        self.zoo_name = name
        print(self.zoo_name)
        self.animal_list = []
        self.sotrudniki_list = []

    def add_animal(self, animal):
        self.animal_list.append(animal)
        print(f"Животное {animal.name} добавлено")

    def add_sotrudnik(self, sotrudnik):
        self.sotrudniki_list.append(sotrudnik)
        print(f"Сотрудник {sotrudnik.name} добавлен")


def sound (animals):
    for animal in animals:
        animal.make_sound()


zoopark = Zoo("Moscow_Zoo")
mamal1 = Mammal("Moo", 5)
zoopark.add_animal(mamal1)

reptile1 = Reptile("Croco", 4)
zoopark.add_animal(reptile1)

bird1 = Bird("Petya", 2)
zoopark.add_animal(bird1)

zoo_keeper = ZooKeeper("Vasya")
zoopark.add_sotrudnik(zoo_keeper)

veterinarian = Veterinarian("Kolya")
zoopark.add_sotrudnik(veterinarian)

sound(zoopark.animal_list)

zoo_keeper.feed_animal(mamal1)
veterinarian.heal_animal(bird1)





