# Loop

# while loop: conditional(True/False)
# while block is executed until the condition is met
# if condition is True, while block is executed
# if condition is False then only program teminate

# condition=True

# while condition:
#   #statements

# a = 5
# b = 0

# while a > b:
#     b += 1
#     print("A is greater than b.")
#     if b == 3:
#         break
#     b += 1
# print("Whileloop end.")


# a = 5
# b = 0
# while a > b:
#     b += 1
#     if b == 3:
#         continue
#         print("A is greater than b.", b)
# print("Whileloop end.")

# for loop
#iterable: sequential data(group data, string data)
# a = [1,2,3,4]
# iteration: process of moving from first index to last index of data
# iterator: variable using to perform iteration in iterable

#Syntax:
# for iterator in iterable:
#     statement1
#     statement2


a = [1,2,3,4,5,6,7,8]

# for i in a:
#     print("For loop", i) #i to print out the value of a

#todo:
# create a list of your hobbies
#print out a statement using each hobbies.


#a = "python basics"
#print out each characters

#print the sum of data present in variable a

# create a list of dictionary with name, age, contact, .....
# a = [{name:"ram", age, contact}, {name:"sita", age, contact}, {name:"sita", age, contact}]
# using for loop print out the introduction of the user in the list

h = ["Basketball", "Swimming", "Gaming", "Larping", "Ragebaiting"]
for i in h:
    print("My hobby is,", i)
    
#print out each characters
string = "Python Basics"

for c in string:
    print (c)    

#sum of data 

a = [1,2,3,4,5,6,7,8]
sum = 0
for num in a:
    sum+=num
    print ("Total sum is", sum)
    
z = ["apple", "mango", "watermelon", "cat", "dog", "mouse", "butterfly","table"]
# print the number of times the loop is executed using iterable z
count = 0
for i in z:
    count+=1
    print("Total num is times the loop is executed is:", count)

x = (1,15, 6, 13, 18, 9)
# find the greatest number and print
# find the smallest number and print
print(f"Greatest number: {max(x, key=int)}")
print(f"Smallest number: {min(x, key=int)}")





    



