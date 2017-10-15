import os

class Superclass(object):
    def __init__(self,name,age,education):
        self.__name = name
        self.__age = age
        self.__education = education

    def printname(self):
        print ("HELLO Mr. ",self.__name)

    def set_age(self,age):
        self.__age = age

    def get_age(self):
        return self.__age

    def education(self):
        return self.__education

class baseclass(Superclass):
    def __init__(self,name,age,education):
       super().__init__(name,age,education)

    def printname1(self):
        super(baseclass, self).printname()
        Age = super().get_age()
        Education = super().education()
        print ("AGE IS: ",Age)
        print ("EDUCATION IS: ",Education)

check = False
while check==False:
 try:
    name = input("ENTER YOUR NAME: ")
    age = int(input("ENTER YOUR AGE: "))
    if (type(age)!=int):
        raise NameError

    education = input("Enter Your Education Level Degree: ")
    obj = baseclass(name, age, education)
    print ("\n" * 50)
    obj.printname1()
    check = True
 except NameError:
    print ("\n AGE CAN'T BE IN STRING, IT SHOULD ALWAYS A NUMBER!\n")
 except ValueError:
    print("\n AGE CAN'T BE IN STRING, IT SHOULD ALWAYS A NUMBER!\n")

