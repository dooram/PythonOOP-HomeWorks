from random import *

listOfBreeds = {"British":{"weight":5, "height":40, "length":60, "gladnessLess":10, "satietyLess":5, "sleepLess":10},
                "Maine Coon":{"weight":7, "height":30, "length":70, "gladnessLess":5, "satietyLess":10, "sleepLess":5},
                "Sphynx":{"weight":5, "height":25, "length":35, "gladnessLess":5, "satietyLess":5, "sleepLess":5}}

class Breed:
    def __init__(self, listOfBreeds):
        self.breed = choice(list(listOfBreeds.values()))
        self.weight = self.breed["weight"]
        self.height = self.breed["weight"]
        self.length = self.breed["length"]
        self.gladnessLess = self.breed["gladnessLess"]
        self.satietyLess = self.breed["satietyLess"]
        self.sleepLess = self.breed["sleepLess"]

class Cat:
    def __init__(self, name, breed=Breed(listOfBreeds), weight=None, height=None, length=None):
        self.name = name
        self.breed = breed
        self.weight = weight
        self.height = height
        self.length = length
        self.gladness = 50
        self.sleep = 50
        self.satiety = 50

    def toPlay(self):
        self.gladness += 50
        self.sleep -= 10
        self.satiety -= 10

    def toSleep(self):
        self.sleep += 50
        self.gladness += 30
        self.satiety -= 10

    def toEat(self):
        self.sleep -= 10
        self.satiety += 50
        self.gladness += 10

    def isAlive(self):
        if self.gladness <= 0:
            print("MEOW! :(")
            self.isAlive = False
        elif self.satiety <= 0:
            print("Meow... :(")
            self.isAlive = False
        elif self.sleep <= 0:
            print("Meow :(")
            self.isAlive = False

    def endOfDay(self):
        print(f"Gladness = {self.gladness}")
        print(f"Satiety = {self.satiety}")
        print(f"Sleep = {self.sleep}\n")

    def live(self, day):
        print(f"Day - {day} of {self.name}")
        self.sleep -= self.breed.sleepLess
        self.satiety -= self.breed.satietyLess
        self.gladness -= self.breed.gladnessLess

        liveCube = randint(1, 2)

        if liveCube == 1:
            if self.satiety < 20:
                self.toEat()
            elif self.gladness < 20:
                self.toPlay()
            elif self.sleep < 20:
                self.toSleep()
        else:
            liveCube = randint(1, 3)
            if liveCube == 1:
                self.toEat()
            elif liveCube == 2:
                self.toPlay()
            elif liveCube == 3:
                self.toSleep()

        self.endOfDay()
        self.isAlive()

Nazar = Cat("Sigma")
for day in range(365):
    if Nazar.isAlive == False:
        break

    Nazar.live(day)