# PascalCase for class names
# snake-case for identifiers (variables) and functions
from os import system
system("cls")
class User:
    # no empty class in python
    def __init__(self, user_id, username) -> None:
        self.user_id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
        # constructor of the User class
        print("new user is created")
    
    def follow(self, another_user):
        self.following += 1
        another_user.followers += 1
        print(f"{self.username} started following {another_user.username}")
        
        
class Car:
    def __init__(self, seats = 5) -> None: #default argument ctor ? yes
        print("a new car is created")
        self.seats = seats
    
    def enter_race_mode(self): # a method - unlike a normal function - always needs to have the first parameter : self
        self.seats = 2


user_1 = User(1, "george")
user_2 = User(2, "odette")

user_1.follow(user_2)
print(user_2.followers)
# print(user_1.user_id)
# print(user_1.followers)

# car_1 = Car()
# car_2 = Car(7)
# print(car_1.seats)
# print(car_2.seats)