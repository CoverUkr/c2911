#print(f"NameError - {type(NameError)} - {issubclass(NameError,BaseException)}")
#try:
    #print("start code")
    #print(error)
    #print("no error")
#except NameError:
    #print("we have an errors")
#print("after capsule")

#a=int(input())
#b=int(input())
#c=int(input())
#d=a+b+c
#print(d)

class BildingError(Exception):
    def __str__(self):
        return f"З цих матеріалів ми не можемо будувати будинок"
def check_material(amount_of_material, limit_value):
    if amount_of_material > limit_value:
        return "матеріалів достатньо"
    else:
        raise BildingError(amount_of_material)
material=123
check_material(material,300)