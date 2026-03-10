# class car:
#     def __init__(self, window, door, enginetype):
#         self.windows=window
#         self.doors=door
#         self.enginetype=enginetype

#     def self_driving(self):
#         return "this is a {} car".format(self.enginetype)
    

# car1=car(4,5,"Petrol")
# print(car1.self_driving())

# car2=car(3,5,"Diesel")
# print(car2.windows)

# print(car2.self_driving())


# class car:
#     def __init__(self,window,door,enginetype):
#         self.windows=window
#         self.doors=door
#         self.enginetype=enginetype

#     def drive(self):
#         print("This is a self driving car")

# car1=car(4,4,"Diesel")
# print(car1.windows)

# class Audi(car):
#     def __init__(self, window, door, enginetype, enableAI):
#         super().__init__(window, door, enginetype)
#         self.enableAI=enableAI

#     def selfdriving(self):
#         print("Audi supports self driving")

# AudiQ7=Audi(4,5,"Diesel", True)
# print(AudiQ7.enginetype)



# class BankAccount():
#     def __init__(self, owner, balance=0):
#         self.owner=owner
#         self.balance=balance

#     def deposit(self, amount):
#         self.balance+=amount
#         print(f"{amount} is deposited. The new balance is {self.balance}")

#     def withdraw(self, amount):
#         if amount>self.balance:
#             print("Insufficient balance")
#         else:
#             self.balance-=amount
#             print(f"{amount} is withdrawn. The new balance is {self.balance}")

#     def get_balance(self):
#         return self.balance
    
# account=BankAccount("Aman", 5000)
# print(account.balance)

# print(account.deposit(500))

# print(account.withdraw(100))
# print(account.get_balance())
        


# class Animal:
#     def speak(self):
#         return "Sound of the Animal"
    
    
# class Dog(Animal):
#     def speak(self):
#         return "woof"
    
# class Cat(Animal):
#     def speak(self):
#         return "Meow"
    
# def animal_speak(animal):
#     print(animal.speak())

# dog=Dog()
# cat=Cat()
# print(dog.speak())
# print(cat.speak())
# animal_speak(dog)


# class Shape:
#     def area(self):
#         return "The area of the figure"
    
# class Rectangle (Shape):
#     def __init__(self, width, height):
#         self.width=width
#         self.height=height

#     def area(self):
#         return self.width*self.height
    
# class Circle(Shape):
#     def __init__(self,radius):
#         self.radius=radius

#     def area(self):
#         return 3.14*self.radius*self.radius
    
# def print_area(shape):
#     print(f"The area is {shape.area()}")

# rectangle=Rectangle(4,5)
# circle=Circle(3)

# print_area(rectangle)
# print_area(circle)

## Abstraction
# from abc import ABC, abstractmethod

# class Vehicle(ABC):
#     @abstractmethod
#     def start_engine(self):
#         pass

# class Car(Vehicle):
#     def start_engine(self):
#         return "Car engine started"
    
# class Motorbike(Vehicle):
#     def start_engine(self):
#         return "Bike engine started"
    
# def start_engine(vehicle):
#     print(vehicle.start_engine())

# car=Car()
# motorbike=Motorbike()

# start_engine(motorbike)


## Encapsulation 

# class Person:
#     def __init__(self, name, age):
#         self.name=name
#         self.age=age

# def get_name(person):
#         return person.name
    
# person=Person("Aman", 28)
# print(get_name(person))


# class Person:
#     def __init__(self, name, age, gender):
#         self._name=name
#         self._age=age
#         self._gender=gender

# class Employee(Person):
#     def __init__(self, name, age, gender):
#         super().__init__(name, age, gender)

# employee=Employee("Aman", 28,"Male")
# print(employee._name)


class Person:
    def __init__(self, name, age):
        self.__name=name
        self.__age=age

    def get_name(self):
        return self.__name
    
    def set_name(self,name):
        self.__name=name

    def get_age(self):
        return self.__age
    
    def set_age(self,age):
        if age>0:
            self.__age=age
        else:
            print("Age cannot be negative")

person=Person("Aman", 28)
print(person.get_name())
print(person.get_age())

person.set_age(35)
print(person.get_age())

person.set_age(-5)


