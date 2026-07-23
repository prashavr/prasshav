#funtion : like variables, block of code is assigned to a function
#function statements:







# def addition():  #function define
#     a = int(input('Enter first number:'))
#     b = int(input('Enter second number:'))
#     print(a + b)        

# addition()    # function call

#calculator

# num1 = int(input("Enter you  first number:"))
# num2 = int(input("Enter your second number:"))
# choice = (input("Enter your operator to calcualte the result (+,-,*,/)"))

# if choice == "+":
#     print(f"Addition : {num1+num2}")
# elif choice == "-":
#     print (f"Substraction : {num1-num2}")
# elif choice == "*":
#     print(f"Multiplication : {num1*num2}")
# elif choice == "/":
#     print(f"Division : {num1/num2}")
# else:
#     print ("Invalid operator.")
    
#parameter: variables defined inside theparathesis in function call
#Arguments: variables defined inside the parathesis in function call
#parameter: accepts the data sent through argument
def intro(name, age, address):
    print(f"My name is {name} and i am {age} years old. I live in {address}")
    
n = 'Ram'
a = 53
add = 'ktm'
intro("Ram", 35, "ktm")


#Keywords arguments: arguments directly assigned to the parameter when function call

def intro(name, age, address):
    print(f"My name is {name} and i {age} am years old. I live in {address}")
    
n = 'Ram'
a = 53
add = 'ktm'
intro(name = "Ram", age = 35, address = "ktm")
intro(age = 35, name = "Ram", address = "ktm")

#Default arguments: if arguments are not defined then default value is used 
def intro(name = "Default", age ="None", address = "Default"):
    print(f"My name is {name} and i am {age} years old. I live in {address}")

intro()
intro(age = 35, name = "Ram", address ="ktm")
intro("Ram", "35", "ktm")

#local and global variable
#global variable can be used or access anywhere in the program
#local variavle can be used inside that function only
a = 15    #a is the gloabal variable
def addition(first):
    b = 5 #b is the local variable
    print(a)
    print(b)
    
addition(a)
print("local")
print(a)
print(b)

addition(a)
print("Global")
print(a)
print(b)

a= 15
def addition(first):
    global a
    a+= 5
    c = 50
    b = 5
    print("Local")
    print(a)
    print(b)
    print(c)
    
addition(a)
print("Globel")
print(a)
print(b)

#calculator : function based