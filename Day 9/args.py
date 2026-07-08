#args : is used to define args, a* is followed by the args_name
#a parameter accepts multiple datas, accepts data in tuple format
#add the data to the function

# def addition(*args):
#     total=0
#     for i in args:
#         total += i
#     print (total) 
           
# addition(4,5,3,4)
# addition(1,2,3,4,5,6,6,7)
# addition(1,29,3,45,5,50,6,6,75)

#create a function that prints out the introduction of the user name sent to it
#eg: I am .....

def username(*name):
    for usernames in name:
        print(f"I am {name}")
        
username ("Ram", "Sita" "Shyam", "Hari", "Krishna")
# username ("Ram", "Sita", "Shyam", "Hari", "Krishna",)
# username ("Ram", "Sita", "Shyam", "Hari", "Krishna")
