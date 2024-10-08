# 1. Dictionary are unordered and lists are ordered
# 2. In dictionary we access them via keys vs in lists we access them via indexs
# 3. Dict is a collection of key-value pairs that can be of any datatype but list is a collection of individual elements
# 4. No duplicate members are allowed in a dictionary and in list duplicate elemnts are allowed

# DICTIONARY COMPREHENSION

# new_dict = {new_key:new_value for item in list if condition} or {new_key:new_value for (key, value) in dict.items() if condition}
import random
city_names = ["Paris", "London", "Mumbai", "Berlin", "Madrid"]

new_dict = {city:random.randint(20, 30) for city in city_names}

new = {city:temp for (city, temp) in new_dict.items() if temp > 25}
print(new)