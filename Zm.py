#class Human:
    #height=180

#class Student(Human):
    #satiety=0

#class Worker(Human):
    #satiety=100

#mark=Student()
#nick=Worker()
#print(nark.satiety)
#print(nick.satiety)

#class Granparents:
    #height=170
    #age=60
    #satiety=100
#class Parents(Granparents):
    #age=40
#class Child(Parents):
    #height = 50
    #def __init__(self):
        #print(self.height)
        #print(self.satiety)
        #print(self.age)

#nick=Child()

#class Grandparents:
    #def __init__(self):
        #print("Hello")

#class Parents(Grandparents):
    #def __init__(self):
        #super().__init__()
        #print("World")
#nick=Parents()

class Computer:
    def calculate(self):
        print("Очислення...")

class Display:
    def display(self):
        print("Я показую інформацію на дисплеї")

class SmartPhone(Display, Computer):
    pass
iphone=SmartPhone()
iphone.calculate()
iphone.display()
