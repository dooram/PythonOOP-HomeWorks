from random import *

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.money = 100
        self.alive = True

    def toStudy(self):
        print("Time to Study! :(")
        self.progress += 0.12
        self.gladness -= 3
        self.money -= 5

    def toSleep(self):
        print("I want sleep")
        self.gladness += 3

    def toChill(self):
        print("Time to chill! :)")
        self.progress -= 0.1
        self.gladness += 5
        self.money -= 15

    def toWork(self):
        print("Time to work! :(")
        self.progress += 0.04
        self.gladness -= 3
        self.money += 20

    def isAlive(self):
        if self.progress < -0.5:
            print("Cast out!")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression is my profession!")
            self.alive = False
        elif self.progress > 5:
            print("Passed externally!")
            self.alive = False
        elif self.money <= 0:
            print("I'm homeless!")
            self.alive = False

    def endOfDay(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {self.progress}")
        print(f"Money = {self.money}\n")

    def live(self, day):
        print(f"Day - {day} of {self.name}")

        liveCube = randint(1, 2)

        if liveCube == 1:
            if self.progress < 0.5:
                self.toStudy()
            elif self.gladness < 5 and self.money <= 50:
                self.toSleep()
            elif self.gladness < 5 and self.money > 50:
                self.toChill()
            elif self.money < 20:
                self.toWork()
        else:
            liveCube = randint(1, 4)
            if liveCube == 1:
                self.toStudy()
            elif liveCube == 2:
                self.toSleep()
            elif liveCube == 3:
                self.toChill()
            elif liveCube == 4:
                self.toWork()



        self.endOfDay()
        self.isAlive()

Nazar = Student("Nazar Sigma")
for day in range(365):
    if Nazar.alive == False:
        break

    Nazar.live(day)