# todo: implementing while loop
# get two numbers from user(a,b)
# check the greater number and print it out
# if a is greate than b print a statement {a} is greater than {b}
# if a is less than b
# if a and b are equal
# ask if they want to continue: yes: interate the code, no: terminate the loop

while True:
    a = int(input('Enter a number :'))
    b = int(input('Enter a number :'))
    if  a>b:
        print ("A is greater than B.")
    else:
        print ("B is greater than A.")
    c =input("Do you want to continue? (y/n):-")
    if c != "y":
        print("Okay.")
        break
    
# get two numbers from user and a operator(+,-,*,/)
# if the operator is +, print the sum of two number
# if the operator is -, print the subtraction of two number
# if the operator is *, print the multiple of two number
# if the operator is /, print the division of two number
# ask if they want to continue: yes: interate the code, no: terminate the loop

while True:
    num1 = int(input("Enter your first number: "))
    op = input("Enter your operator to calculate the result (+,-,*,/): ")
    num2 = int(input("Enter your second number: "))

    if op == "+":
        print(f"Addition: {num1 + num2}")
    elif op == "-":
        print(f"Subtraction: {num1 - num2}")
    elif op == "*":
        print(f"Multiplication: {num1 * num2}")
    elif op == "/":
        if num2 == 0:
            print("Error: Cannot divide by zero.")
        else:
            print(f"Division: {num1 / num2}")
    else:
        print("Invalid operator.")

    c = input("Do you want to continue? (y/n): ")
    if c == "n":
        print("Okay")
        break