rating = 4.7

if rating > 4.5:
    print("Extraordinary")
elif rating > 4:
    print("Excellent")
elif rating > 3:
    print("Good")
elif rating > 2:
    print("Fair")
else:
    print("Poor")
    
    
import random

number = random.randint(0, 5)

if number == 0:
    print('Flamingos turn pink from eating shrimp.')
elif number == 1:
    print('The only food that doesn\'t spoil is honey.')
elif number == 2:
    print('Shrimp can only swim backwards.')
elif number == 3:
    print('A taste bud\'s life span is about 10 days.')
elif number == 4:
    print('It is impossible to sneeze while sleeping.')
else:
    print('It is illegal to sing off-key in North Carolina.')
    
    
month = int(input("Enter a month number (1-12): "))

if month == 1 or month == 2 or month == 3:
    print("Winter")
elif month == 4 or month == 5 or month == 6:
    print("Spring")
elif month == 7 or month == 8 or month == 9:
    print("Summer")
elif month == 10 or month == 11 or month == 12:
    print("Autumn")
else:
    print("Invalid")
    
    
    
    
weight = float(input("Enter your Earth weight: "))
planet = int(input("""
1. Mercury
2. Venus
3. Mars
4. Jupiter
5. Saturn
6. Uranus
7. Neptune
Enter a planet number: """))

if planet == 1:
    print("Your weight on Mercury is", weight * 0.38)
elif planet == 2:
    print("Your weight on Venus is", weight * 0.91)
elif planet == 3:
    print("Your weight on Mars is", weight * 0.38)
elif planet == 4:
    print("Your weight on Jupiter is", weight * 2.53)
elif planet == 5:
    print("Your weight on Saturn is", weight * 1.07)
elif planet == 6:
    print("Your weight on Uranus is", weight * 0.89)
elif planet == 7:
    print("Your weight on Neptune is", weight * 1.14)
else:
    print("Invalid planet number")
    
# 6.a countdown from 10 to 1. Use a for loop that counts down by using the "step" value in range().
# Inside the loop, print the numbers from 10 to 1, each on its own line.
# When the loop finishes the countdown, print this exact string.

for i in range(10, 0, -1):
    print(i)

print("This exact String")



    
    
    
  