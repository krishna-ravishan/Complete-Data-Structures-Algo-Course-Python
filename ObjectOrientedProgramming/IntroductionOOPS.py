# We have a few concepts that we need to know about
    # 1. Object: An object is an instance of a class. 
    # 2. Class: A class is a blueprint/template consisting of attributes and methods for an object. 
    # 3. Attributes: Can be defined as the variables a class has that defines it.
    # 4. Methods: A method can be defined as the functions that define what it does.

# identity, attributes and behaviors describe an object.
# Objects are nouns, and behaviors are verbs.
 
# Now let's learn how to define an object

# robot_a = RobotClass()
# robot_b = RobotClass()

# To access attributes

# robot.battery_level

# To call object methods

# robot.detect_speech()
# Difference between methods and functions is that methods is defined as a part of a class and functions are something that are usually self defined

# Let's create a class

class StarCookie:
    # Let's create a class attribute
    milk = 0.1

    def __init__(self, weight, color):
        print("The cookie is ready...")
        self.color = color
        self.weight = weight

star_cookie1 = StarCookie(15, "White")     

print(star_cookie1.__dict__) # Prints a dictionary consisting of attributes and their values for the object
print(star_cookie1.color)
print(StarCookie.__dict__)
# star_cookie2 = StarCookie("Blue")
# star_cookie2.weight = 25
# print(star_cookie2.weight)
# print(star_cookie2.color)
# star_cookie3 = StarCookie("Yellow")
# star_cookie3.weight = 35
# print(star_cookie3.weight)
# print(star_cookie3.color)

# If we have lots of cookies, we'd have to initialize a new object every single time.

# Initializers: When objects are initialized we can set variables to starting values. We can use a special function called __init__(self) function

# class Youtube:
#     def __init__(self, username, subscribers=0):
#         self.username = username
#         self.subscribers = subscribers

# user1 = Youtube("Krishna Ravishanker", 10000000)
# print(user1.username)
# print(user1.subscribers)

# user2 = Youtube("Elshad")
# print(user2.username)
# print(user2.subscribers)

# Class Methods

class Robot:
    def __init__(self, battery_level):
        self.battery_level = battery_level
    def enter_charge_mode(self):
        self.battery_level += 1

my_robot = Robot(69)
my_robot.enter_charge_mode()
print(my_robot.battery_level)