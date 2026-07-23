#exception handling :exception that raises during the execution of the program
#try: block of code that raise exception are placed in try block
#except : block of code that. needs to be executed when exception raises in try block
#finally ; block of code that is to be executed when either exception case raises or not
#only one catch all
# try:
#     a = int(input("Enter a number: "))
#     print (a + 5)
# except ValueError:
#     print("Value Error")
# except NameError:
#     print("Name Error")
# except:
#     print("Catch all except blocks")
# finally:
#     print("ERROR ERROR")
    
    # try:
#     a = int(input("Enter a number: "))
#     print (a + 5)
# except:
#     print("Value Error")
# finally:
#     print("ERROR ERROR")

# try:
#     print (a + 5)
# except:
#     print("A is not defined.")
    
while True:
    try:
        num1 =("Enter you first number:")
        op = ("Enter an operator (+,-,*,/):")
        num2 = ("Enter your second number:")
        
        if op == "+":
            print(num1 + num2) 
        elif op == "-":
            print(num1 - num2)
        elif op == "*":
            print(num1 * num2)
        elif op == "/":
            print(num1 / num2)
        else:
            print("Invalid operator.")
    except:
        print("exception handling")
    
    choice = ("Do you want to continue? (y/n)")
    if choice == "n":
        break