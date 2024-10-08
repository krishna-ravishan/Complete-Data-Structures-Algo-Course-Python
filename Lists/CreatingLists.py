shopping_list = ['milk', 'eggs', 'bread'] 

# random_list = ['a', 1, 2, ['b', 1.4], 9.5 ,'Hello']

# print(shopping_list[0])
# print(random_list)

# print('milk' in shopping_list)

# print(shopping_list[-1])
 
# for i in shopping_list:
#     print(i)

for i in range(len(shopping_list)):
    shopping_list[i] += "+"
    print(shopping_list[i], end="")