#Inheritance : super class and sub class, parent class and child class, base class and derived class
#parent class properties can be used or accessed by child class
#child class can have its own properties and methods
#reusability


# class Vehicle:     #Parent class
#     brand = None
#     model = None
#     color = None
    
#     def get_info(self,brand,model,color):
#         self.brand = brand
#         self.model = model
#         self.color = color
        
#     def intro(self):
#         print(f"""Brand: {self.brand}
# Model: {self.model}
# Color: {self.color}""")
        
# class EV(Vehicle):   #Child class
#     capacity = None
# def get_capacity(self, cap):
#         self.capacity = cap
        
#         def intro (self):
#             print(f"""Brand: {self.brand}
# Model: {self.model}
# Color: {self.color}
# Capacity: {self.capacity}""")
            
# ev1 = EV()
# ev1.get_info("Brand","Model","Color")
# ev1.get_capacity("6")
# ev1.intro()

# todo :
# create animal class, attributes: eyes, ears, legs, ....
# methods:get_info(), show_info()
# child class
# create dog class, attributes: name, method : move(), sound()
# create cat class, attributes: name, method : move(), sound()

class Animal:               # Parent class
    eyes = None
    ears = None
    legs = None

    def get_info(self, eyes, ears, legs):
        self.eyes = eyes
        self.ears = ears
        self.legs = legs

    def show_info(self):
        print(f"""Eyes: {self.eyes}
Ears: {self.ears}
Legs: {self.legs}""")


class Dog(Animal):          # Child class
    name = None

    def get_name(self, name):
        self.name = name

    def move(self):
        print(f"{self.name} runs on 4 legs.")

    def sound(self):
        print(f"{self.name} says: woof")

    def show_info(self):
        print(f"""Name: {self.name}
Eyes: {self.eyes}
Ears: {self.ears}
Legs: {self.legs}""")


class Cat(Animal):         # Child class
    name = None

    def get_name(self, name):
        self.name = name

    def move(self):
        print(f"{self.name} runs on 4 legs.")

    def sound(self):
        print(f"{self.name} says: meow")

    def show_info(self):
        print(f"""Name: {self.name}
Eyes: {self.eyes}
Ears: {self.ears}
Legs: {self.legs}""")

dog1 = Dog()
dog1.get_name("nugget")
dog1.get_info(2, 2, 4)
dog1.show_info()
dog1.move()
dog1.sound()

cat1 = Cat()
cat1.get_name("sushi")
cat1.get_info(2, 2, 4)
cat1.show_info()
cat1.move()
cat1.sound()
            
        
        
            