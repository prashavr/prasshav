#Indexing:get or access a single data from the sequence , ordered datatype(dict, list, tuple, string)

#count the position or index of character
a = "Hello"
# H = 0
# e = 1
# l = 2
# l = 3
# o = 4

print (a[-1]) #o negative indexing: start counting from the end of the string
#print (a[1]) #e

b = "I am ( learning"
#print out ( from b
# I = 0
#   = 1
# a = 2
# m = 3
# ( = 4
#   = 5
# l = 6
# e = 7 etc

# count position or index of data
fruits = ["apple", "banana", "grapes", "orange" "mango", "papaya", "pineapple", "watermelon"]
# print our orange from the fruits list
#print our data using index 
print (fruits[3]) #orange
fruits[3] = "cat" #list is mutable: data can be changed, tuple immutable so the existing data in tuple cant be changed
print(fruits)#change the data in the list using index

#in dictionary use key to access the value signed in it
my_dict = {"name": "ram", "age": 35, "city": "Kathmandu", "contact": 9841234567}
print(my_dict["name"]) #ram 
my_dict["name"] = "shyam" #change the value of key name
print(my_dict["name"])
    
