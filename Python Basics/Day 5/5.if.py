#if else : conditional statement

#if and elif block takes condition but else block does not take condition
#condition must be True to execute the if/elif blocks
#multiple elif block can be defined but if and else only once
#else block is executed if the condition in upper blocks are False

#Syntax:
#if condition:
#   print ("statement")
#else
#   statements

a = 5
b = 5

#if value of  a  is greater than the value of a then print A is greater
#if value of  b  is greater than the value of a then print B is greater
if a > b:
    print("A is greater ")
    print("than b.")
elif a ==b:
    print("A and B are equal.")
elif a < b:
    print("B is greater than A")
else:
    print("Else block.")
    
# todo:
#get two nunmbers
#check the greater number and print it out




num1=int(input("Enter your first number"))
num2=int(input("Enter your second number"))
if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num2 > num1:
    print(f"{num2} is greater than {num1}")
else:
    print("Both numbers are equal")
    
# simple calculator
# get two numbers from user and a operator(+,-,*,/)
# if the operator is +, print the sum of two number
# if the operator is -, print the subtraction of two number
# if the operator is *, print the multiple of two number
# if the operator is /, print the division of two number

# get user's exam marks
# if the mark is greater than 100 and less than 0, print a statment
# if the mark is greater than 90 and less then 100, print a statment("Excekllent")
# if the mark is greater than 80 and less than 90 , print a statement
# if the mark is greater than 70 and less than 80 , print a statement
# if the mark is greater than 60 and less than 70 , print a statement
# if the mark is greater than 50 and less than 60 , print a statement
# if the mark is greater than 40 and less than 50 , print a statement
# if the mark is less than 40, print a statment

# define a dictionary username as key and password as value
# get the username and password from the user
# check if the username exists in the dictioney
# if yes: check if the password is correct(if yes: print Valid or Verified user, if no: print password incorrect)
# if no: print the statement(eg: Invalid username)
    
    
    