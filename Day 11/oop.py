#OOP: Object oriented programming
#class: structures, blueprint
#object: data created using class

#Syntax:
#  class class_name:
#  attributes : variable
#  methods : function

class Person():

    def get_info(self,name,age,gender,address):
        self.name= name     #self.attribute_name calls the attribute of the class
        self.age= age
        self.gender= gender
        self.address= address
    
    def intro (self):  #self= object_name
        print(f"""Name: {self.name}
Age: {self.age}
Address: {self.address}
Gender: {self.gender}""")
        
ram = Person()
ram.get_info ("ram", "35", "male", "ktm")
ram.intro()
ram.name

# ram = Person() # object: r1, Person() = class call    
# print(ram.name)
# print(ram.age)
# print(ram.gender)
# print(ram.address)
# ram.intro()


sita = Person() # object: r1, Person() = class call  
sita.name = "Sita"
sita.age = "25"
sita.gender = "Female"
sita.address = "BKT"
sita.abc = "ABC" #define separately   
print(sita.name)
print(sita.age)
print(sita.gender)
print(sita.address)



#create a class car


class car: 
    brand = "Ferrari"
    model = "SF-22"
    color = "Red"

ferrari = car()
print(ferrari.brand)
print(ferrari.model)
print(ferrari.color)
ferrari.driver = "Hamilton"
print(ferrari.driver)

a="abc"
print(a.upper())
print(a.capitalize())

b= a.upper()
print(b)

class str():
     def upper(self):
         pass
     #self capitalize(self)
     # pass