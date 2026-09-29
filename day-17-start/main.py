# class User:
#     pass
#
# user_1 = User()     # user_1 is a object and User() is class
# user_1.id = "1"    #id and name are variables and we just attached object to them to make them attribute
# user_1.name = "Bob" #object.variable = attribute
# print(user_1.name)
#
# user_2 = User()
# user_2.id = "2"
# user_2.name ="saleha"
# print(user_2.name)

#if we use a new user(object) like user_1 is constructed from User class we must pass the two attribute which us user_name and password
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.followers = 0
        self.following = 0 # default value will be 0 for ever new object

    def follow(self, user):
        user.followers += 1
        self.following +=1




user1 = User("saleha", "@saleha786")
user2 = User("asiya", "@asiya786")
print(user1.username, user1.password)

user1.follow(user2)
print(user1.followers, user1.following)

#when a function is attached to object it is called method
# class Car:
#     def enter_race_mode():
#         self.seats = 2

# my_car.enter_race_mode()
