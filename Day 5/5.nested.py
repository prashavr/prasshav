a = 10
b = 5
 

if a > b:
    print("A is greater ")
    print("than b.")
elif a ==b:
    print("A and B are equal.")
elif a < b:
    print("B is greater than A")
else:
    print("Else block.")









#Voting Eligibility
# get user age
# if user age < 18: print statement
#if suer age > 18:
#       print a statement
#       ask if they have voting card:
#       if yes: print a statement;
#       if no:
#           ask if you want to crate one
#           if yes: print a statement
#           if no: print a statement

age = int(input("Enter yoyr age:"))
if age >=18:
    print("You are eligible to vote.")   
    card = input("Do you have voting card?(y/n)>>>")
    if card == "y":
        print("Good.")
    elif card == "n":
        create = input("Do you want to create a card?(y/n)>>>")
        if create == "y":
            print("You can visit the official site.")
        elif create =="n":
            print("You do not want to create one.")
        else:
            print("This is not a valid choice (CREATE).")
    else:
        print("This is not a valid choice (CARD)")
else:
    print("You are not eligible to vote.")
    
    
# Licence
# get user age
# if user age < 18: 
#     print statment
#     ask if they can to get one(yes/no)
#     if yes: print a statement
#     if no: print a statement
#       one statement for invalid choice(optional)
# if user age >= 18:
#      print a stetement
#     ask if they have Licence:
#     if yes: print a statement:
#     if no: 
#        ask if you want to create one
#        if yes: print a statement
#        if no: print a statement
#        one statement for invalid choice(optional)
#     if not yes or no: a statement for the choice(optional)


age = int(input("Enter yoyr age:"))
if age >=18:
    print("You are eligible to vote.")   
    card = input("Do you have voting card?(y/n)>>>")
    if card == "y":
        print("Good.")
    elif card == "n":
        create = input("Do you want to create a card?(y/n)>>>")
        if create == "y":
            print("You can visit the official site.")
        elif create =="n":
            print("You do not want to create one.")
        else:
            print("This is not a valid choice (CREATE).")
    else:
        print("This is not a valid choice (CARD)")
else:
    print("You are not eligible to vote.")



    