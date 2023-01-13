class Granparents:
    iq=85
    beauty=60
    age=85
class Parents(Granparents):
    iq = 110
    beauty = 80
    age = 40
class Child(Parents):
    iq = 100
    beauty = 85
    age = 13
    def __init__(self):
        print(self.iq)
        print(self.beauty)
        print(self.age)

nick=Child()
