import random
class Student:
    def __init__(self, name):
        self.name=name
        self.water=40
        self.dish=40
        self.alive=True
        self.walk=1

    def drink(self):
        print("Час Попити")
        self.walk+=2
        self.dish-=2
        self.water=+5

    def eat(self):
        print("Час поїсти")
        self.water-=2
        self.walk+=2
        self.dish+=5

    def walking(self):
        print("Час гуляти")
        self.water-=2
        self.dish-=2
        self.walk-=5

    def is_alive(self):
        if self.water>=50:
            print("Напився води")
            self.alive=False
        elif self.dish>=50:
            print("Наївся")
            self.alive=False


    def end_of_day(self):
        print(f"Water - {self.water}")
        print(f"Dish - {round(self.dish)}")
        print(f"Walk - {round(self.walk)}")

    def live(self, day):
        day = "Day" + str(day) + "of" + self.name + "litle"
        print(f"{day:=^50}")
        cube = random.randint(1,3)
        if cube==1:
            self.drink()
        elif cube==2:
            self.eat()
        elif cube==3:
            self.walking()

        self.end_of_day()
        self.is_alive()

nick=Student(name="Maks")
for day in range(365):
    if nick.alive==False:
        break
nick.live(day)

