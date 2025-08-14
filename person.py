class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def great(self):
        print(f"I'm {self.name} and I'm {self.age} years old")

person1 = person("denis",19)
person2 = person("shema",18)
person3 = person("john",20)
person4 = person("marry",15)

person1.great()
person2.great()
person3.great()
person4.great()

def is_udult(self,age):
    if age > 18:
        return True
    else:
        return False
    print(f"{self.age}")
