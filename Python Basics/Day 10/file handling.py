# File handling: process of manipulating file programatically

#open the file
#f = open(file_path, mode)

# close 
# f.close() 

# read (r)
# f = open("Day3.txt", 'r')
# a = f.read()
# print (a)
 
# #Write(w):new lines/data replace the old lines/data, if file does not exist new file is created
# f = open("day1.txt", 'w')
# f.write("BYE")
# f.close()

# #append (a): new lines are added to the file at the end, if file does not exist a new file is created
# f = open("day1.txt", 'a')
# f.write("Welcome")
# f.close

#todo:
#login /register (ask user)
#if register: get username from user, store it in a file
#if login: get username from user and check if the username exists in the file

choice = input("Would you like to (login) or (register)? ")

if choice == "register":
    username = input("Choose a username: ")
    file = open("users.txt", "a")
    file.write(username + "\n")
    file.close()
    print("Registration successful!")

elif choice == "login":
    username = input("Enter your username: ")
    file = open("users.txt", "r")
    users = file.read()
    if username in users:
        print("Login successful! Welcome,", username)
    else:
        print("Username not found.")

else:
    print("Invalid choice.")


