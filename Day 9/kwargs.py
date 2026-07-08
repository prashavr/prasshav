#kwargs: keyword arguments, sent multiples keyword argument to a prameter
#** used to define kwargs, it is followed kwargs_name
def student(**kwargs):
    print (kwargs)
    for i,j in kwargs.items():
        print(i)
        print(j)
        print(f"{i} : {j}")
        #print(f"Name : {name}")
        #print(f"age : {age}")
        #print(f"roll : {roll}")
        #print(f"add : {add}")
        #print(f"email : {email}")
        
student(name = "Ram", age=25, roll = 2, add = "KTM", email = "email.google.com")


#return : return certain values/data to the function call. by default None is returned
# function based
# add two number
#multiple 3 times with the sum
def addition(first,second):     # function define
    add = first+second
    return add

#print (add)

a = addition (25,5)

print (a * 3)
print (a * 10)




        