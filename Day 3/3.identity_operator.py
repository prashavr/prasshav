#Identity Operator :  Check if two values are equal, location
a = 10
b = 15
c = 10

#is: if two values are identical, Output: true, else false
print (a is b)
print (a is c)
print(id(a))
print(id(b))
print(id(c))

#is not if two data are identical then output is false, else true
print (a is not b)
print (a is not c)

#a = 10        --> id:1
#b = 15        --> id:2
#c = 10        --> id:1


#input () #to prevent the program from closing immediately after execution enter data trhough terminal and press enter to close the program
a = input () #stores data in variable a
print(a) 

a = input ("Enter your name: a") #stores data in variable a
print(a) 