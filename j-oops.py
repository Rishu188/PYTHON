"""OOPS (Object-oriented programming system)"""
# OOPS is a programmming paradigm based on the concept of "objects", which can contain data(attributes) and code (methods).


# Classes
 # A class is like a blueprint or template for creating objects.

# class Factory:
#     a=12 #attribute

#     def hello(self):  #method
#         print("how are you")

#     print("hello how are you i am getting initialized")
# print(Factory().a)
# Factory().hello()


# """"OBJECT"""
# # object creation is easy we just have to call the class inside a variable nd that var becomes an object..
# class Factory:
#     a=12 #attribute

#     def hello(self):  #method
#         print("how are you")

#     print("hello how are you i am getting initialized")

# obj= Factory()
# obj1= Factory()
# obj1.hello()

""""CONSTRUCTOR"""
# A constructor is a method that runs automatically when we call a class and this constructor function will target the objects location...


# class Factory:
#     def __init__(self,material,zips,pockets):
#         self.material = material
#         self.zips = zips
#         self.pockets = pockets
    
#     def show(self):
#         print(f"your object details are {self.material}, {self.pockets},{self.zips} ")
# reebok = Factory("leather",3,2)
# campus = Factory("nylon",3,3)
# campus.show()


"""ATTRIBUTES AND METHODS"""
# Class attribute: A normal variable created inside a class is  class attribute and thats it...

class Animal:
    name = "lion" #class attribute

# Instance attribute: A attribute created using an instance like self.name, self.age etc. it is known as instance attribute...
class Animal:
    name = "lion" #class attribute
    def __init__(self,age):
        self.age = age #instance attribute

 #Instance method: works with instance of the class. can access and modify instance attributes..
    def show(self): #instance method
        print(f"how are you your agger is {self.age}")
    

# Class Method: works with the class itself it will not target the instance(object)
    @classmethod
    def hello(cls):
        print(f"how are you brother {cls.age}")


# Static method: doesn't access class or instance directly it also uses a decorartor @staticmethod...
    @staticmethod
    def static():
        print("how are you")

obj = Animal(12)


"""INHERITENCE"""
# class Factorymumbai: #parent class / superclass
#     a = "I am an attribute mentioned inside Factory"
#     def hello(self):
#         print("hello I am a method mentioned inside Factory")

# class Factorypune(Factorymumbai):   #child class /subclass
#     pass

# obj = Factorymumbai()
# obj2 = Factorypune()
# obj2.hello()



# class Animal:
#     def __init__(self,name):
#         self.name = name
    
#     def show(self):
#         print(f"hello your name is {self.name}")

# class Human(Animal):
#     def __init__(self, name,age):
#         super().__init__(name)
#         self.age = age
    
#     def show(self):
#         print(f"hello your name is {self.name},{self.age}")

# animal1 = Animal("lion")
# person1 = Human("akarsh",23)
# animal1.show()


# class Animal:
#     def __init__(self,name):
#         pass

# class Human:
#     def __init__(self,name,age):
#         pass

# class Robots(Human,Animal):
#     name3 = "charli123"

# obj = Robots()

# class Factory:
#     def __init__(self,material,zips):
#         self.material = material
#         self.zips = zips 
    

# class BhopalFactory(Factory):
#     def __init__(self, material, zips,color):
#         super().__init__(material, zips)
#         self.color = color
    
# class Punefactory(BhopalFactory):
#     def __init__(self, material, zips, color,pockets):
#         super().__init__(material, zips, color)
#         self.pockets = pockets


# class Animal:
#     def show(self):
#         print("hello I am akarsh")
    


# class Human(Animal):
#     def show(self):
#         print("how are you")

# obj = Human()
# obj.show()


# class Animal:
#     def show(self):
#         print("I am showing ")

# class Human:
#     def show(self):
#         print("hello I am also showing ")

# obj = Animal()
# obj2 = Human()

# obj.show()
# obj2.show()


# class Factory:
#     __a = "pune"

#     def show(self):
#         print(Factory.__a)


# obj = Factory()

# obj.show()


# from abc import ABC, abstractmethod

# class abstract(ABC):
#     @abstractmethod
#     def perimeter(self):
#         pass 
    
#     @abstractmethod
#     def area(self):
#         pass

# class Square(abstract):
#     def __init__(self,side):
#         self.side = side

#     def perimeter(self):
#         print("i have created")
    
#     def area(self):
#         print("I have created this ")



# class Circle(abstract):
#     def __init__(self,radius):
#         self.radius = radius
    
#     def perimeter(self):
#         print("i have created")
    
#     def area(self):
#         print("I have created this ")

# obj = Circle(7)
# obj2 = Square(12)


# class Animal:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
    
#     def __str__(self):
#         return f"hello how are you and your name is {self.name}"

#     def __add__(self,other):
#         sum = 0
#         for i in other:
#             sum = sum + i.age

#         return f"your sum of ages are {self.age + sum}"

# obj = Animal("lion",12)
# obj2 = Animal("dolphin",14)
# obj3 = Animal("tiger",34)

# print(obj + (obj2,obj3))


# class Animal:
#     @property
#     def show(self):
#         print("hello how are you")
    
# obj = Animal()

# obj.show



# def decorate(func):
#     def wrapper(*args,**kwargs):
#         print("the addition to your numbers are ")
#         func(*args,**kwargs)
#         print("thankyou I hope you liked it ")
#     return wrapper


# @decorate
# def addition(a,b):
#     print(f"your total is {a + b} ")

# addition(12,67)


# def information(**kwargs):
#     print("your information is\n\n ")
#     for i in kwargs:
#         print(f"{i} : {kwargs[i]}")
    



# information(name = "Akarsh", age = 23, designation = "AI/ML")

# l = {i : i**2 for i in range(1,10)}

# print(l)

# a = [1,2,3,4,5]

# def double(x):
#     return x *2

# result = map(double,a)

# print(list(result))

# from modelss.model import hello,maths

# a = int(input("how many rows you  want "))

# for i in range(1,a + 1):
#     for j in range(i):
#         print("* ",end = "")
#     print()

# n = int(input("tell how many rows you want"))

# for i in range(1,n+1):
#     for j in range(n-i):
#         print("  ",end = "")
#     for k in range(i):
#         print("* ",end = "")
#     print()



# n = int(input("tell how many rows you want"))

# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end = "")
#     for k in range(i):
#         print("* ",end = "")
#     print()


# for i in range(n-1,0,-1):
#     for j in range(n-i):
#         print(" ",end = "")
#     for k in range(i):
#         print("* ",end = "")
#     print()

# a = 1234
# copy = a
# sum = 0

# while a > 0:
#     z = a %10
#     fact = 1 
#     for i in range(1,z+1):
#         fact = fact * i
    
#     sum = sum + fact
#     a = a//10 

# if sum == copy:
#     print("this is a strong number ")
# else:
#     print("not a strong number")


# for j in range(2,21):
#     a = j

#     for i in range(2,(a//2)+1):
#         if a % i == 0:
#             break

#     else:
#         print(a)



# a = [1,1,1,2,2,2,3,3,3,3,3,3,3,3,4,4,4,4,4,5,5,5]
# count = 0
# dict = {}
# for i in a:
#     if i in dict.keys():
#         dict[i] +=1 
#     else:
#         dict[i] = 1
# max = 0
# for i in dict.values():
#     if i > max:
#         max = i
# for i in dict:
#     if dict[i] == max:
#         print(f"{i} occured {max} times and that is largest occurence")
#         break