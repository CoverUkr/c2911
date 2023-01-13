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