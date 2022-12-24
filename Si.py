import random
class Student:
    def __init__(self, name):
        self.name=name
        self.gladness=50
        self.progress=0
        self.alive=True
        self.dish=25
        self.money=100

    def study(self):
        print("Час навчатись")
        self.progress+=0.9
        self.gladness-=10
        self.dish-=4
        self.money-=5
    def sleep(self):
        print("Час спати")
        self.gladness+=4
    def chill(self):
        print("Час відпочинку")
        self.progress-=0.2
        self.gladness+=7
        self.dish+=2
        self.money-=7
    def dish(self):
        print("Час їсти")
        self.dish+=5
    def money(self):
        print("Час підробітки")
        self.money+=32
    def is_alive(self):
        if self.progress<-0.5:
            print("Відрахували...")
            self.alive=False
        elif self.gladness<=0:
            print("Дипресія")
            self.alive=False
        elif self.progress>=5:
            print("Закінчив універсетет")
            self.alive=False
        elif self.dish>=32:
            print("Ожиріння")
            self.alive = False
        elif self.money<=10:
            print("Став бідним")
            self.alive = False

    def end_of_day(self):
        print(f"Gladness - {self.gladness}")
        print(f"Progress - {round(self.progress,2)}")

    def live(self, day):
        day="Day" + str(day) + "of" + self.name + "litle"
        print(f"{day:=^50}")
        cube=random.randint(1,3)
        if cube==1:
            self.study()
        elif cube==2:
            self.sleep()
        elif cube==3:
            self.chill()
        elif cube==4:
            self.dish()
        elif cube==5:
            self.money()

        self.end_of_day()
        self.is_alive()

nick=Student(name="Maks")
for day in range(365):
    if nick.alive==False:
        break
    nick.live(day)