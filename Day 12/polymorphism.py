#polymorphism: poly: multiple, morph: form
#different classes have the same method name
#functionality depends on the object it is called

a = 1
b = 1

x = "hello"
y = "world"

print(a.add(b))
print(x.add(y))


class Dog:
    def move(self):
        print("Dog move with legs")


class Bird:
    def move(self):
        print("Bird move using wings.")


class Fish:
    def move(self):
        print("Fish move using fins.")


d1 = Dog()
b1 = Bird()
f1 = Fish()

d1.move()
b1.move()
f1.move()

# abstraction: data hiding(hide complex internal details/events from users
# ATM: internal validation are hidden from user
# Bike Car: internal engine