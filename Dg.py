import random
class Student:
    def __init__(self, name):
        self.name=name
        self.water=50
        self.dish=50
        self.alive=True
        self.walk=0

    def water(self):
        print("Час Попити")
        self.walk+=5
        self.dish-=5
        self.water+=10

    def dish(self):
        print("Час поїсти")
        self.water-=5
        self.walk+=5
        self.dish+=10

    def walk(self):
        print("Час гуляти")
        self.water-=5
        self.dish-=5
        self.walk-=10

    def is_alive(self):
        if self.water>=50:
            print("Напився води")
            self.alive=False
        elif self.dish>=50:
            print("Наївся")
            self.alive=False
        elif self.walk>=15:
            print("Закінчив універсетет")
            self.alive=False
        elif self.dish<=35:
            print("Ожиріння")
            self.alive = False
        elif self.water<=35:
            print("Став бідним")
            self.alive = False

    def end_of_day(self):
        print(f"Gladness - {self.water}")
        print(f"Progress - {round(self.dish, 2)}")

    def live(self, day):
        day = "Day" + str(day) + "of" + self.name + "litle"
        print(f"{day:=^50}")
        cube = random.randint(1, 3)
        if cube==1:
            self.water()
        elif cube==2:
            self.dish()
        elif cube==3:
            self.walk()

        self.end_of_day()
        self.is_alive()

nick=Student(name="Maks")
for day in range(365):
    if nick.alive==False:
        break
nick.live(day)

