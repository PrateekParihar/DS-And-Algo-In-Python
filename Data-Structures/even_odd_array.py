from datetime import date
class Animal:
    sound = 'uuuuffffff'
    
    def __init__(self,name,age):
        self.name = name
        self.age = age

    @staticmethod
    def from_fathers_Age(name, father_age, father_person_age_diff):
        return Animal(name,date.today().year - father_age + father_person_age_diff)

    @classmethod
    def from_birth_year(cls,name,birth_year):
        return cls(name,date.today().year - birth_year)

    def display(self):
        print(self.name +" age is - "+str(self.age))

class Man(Animal):
    sex = 'Male'

person = Man('Adam',19)
person.display()

person1 = person.from_birth_year('John',1948)
person1.display()

person2 = person.from_fathers_Age('Ben',1956, 20)
person2.display()

print(isinstance(person1,Man))
print(isinstance(person2,Man))

help(isinstance)