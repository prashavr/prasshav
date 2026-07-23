# slicing:

#start index : inclusive -> read
#end index : exclusive -> stop reading before this index
#syntax: variable[start_index : end:index]

#print out learning
a = "I am ( learning python basics"
print(a[6:11])  # ???????

#print out learning
#print I am 
#print python
#print python basics

print (a[0:5])
print (a[14:21])
print (a[14:]) #if we dont specify the end index it will read till the end of the string

fruits = ["apple", "banana", "mango", "orange","grapes", "papaya", "pineapple", "watermelon"]
#print out "grapes", "papaya", "pineapple", "watermelon"
print(fruits[4:8])
#print out all fruits except last 3 fruits
print (fruits[0:5])
#print out all fruits except last 4 fruits
print (fruits[0:4])
#print out any 5 datas
print (fruits[0:5])

#print out the data in odd index
print (fruits[0:8:2])
#print out the data in even index
print (fruits[1:8:2])
#print out the reverse from the list
print (fruits[::-1])

print ("hello")
name = "ram"
age = "35"
print ("hello", name, "you are", age, "years old.") 
print ("hello " + name + " you are " + age + " years old.") 
print(f"hello {name} you are {age} years old.")

#define multiple variables and create a sentence using them

#create a list of hobbies
a = [1,2,3,4]
#print out a sentence include a hobby in the sentence
# " i like ----"
 # List of 5 hobbies
hobbies = [ "Swimming", "Gym", "Gaming", "Reading", "Climbing"]
print(f"I like {hobbies[0]}")
print(f"I like {hobbies[1]}")
print(f"I like {hobbies[2]}")
print(f"I like {hobbies[3]}")
print(f"I like {hobbies[4]}")


