
# # Update/Insert a List

# myList = [1, 2, 3, 4, 5, 6, 7]
# print(myList)
# myList[2] = 33
# print(myList)

# # List methods: insert(), append() & extend()

# myList.insert(0, 3)
# print(myList)

# myList.append(2)
# print(myList)

# myList.extend(['a', 'b'])
# print(myList)


# a = [1, 2, 3]
# b = [4, 5, 6]
# c = a + b
# print(c)

# # * Operator

# a = [0, 1]
# a = a * 4
# print(a)

# # len() function
# print(len(a))

# # max() function
# print(max(a))

# # min() function
# print(min(a))

# # sum() function
# print(sum(a))

# # avg() function
# print(sum(a)/len(a))

# # total = 0
# # count = 0
# # while(True):
# #     inp = input("Enter a number: ")
# #     if inp == "done":
# #         break
# #     value = float(inp)
# #     total = total + value
# #     count = count + 1
# #     average = total / count

# # print('average: ', average)

# my_list = list()
# while(True):
#     inp = input("Enter element in list: ")
#     if inp == "done": break
#     inp = float(inp)
#     my_list.append(inp)

# def average(a_list):
#     avg = sum(a_list)/len(a_list)
#     print(f"Average: {avg}")

# average(my_list)

# Strings and Lists
# Use of split() function
# a = 'spam spam spam'
c = 'spam-spam1-spam2' # Use of delimiters
# b = a.split(delimiter)
delimiter = '-'
b = c.split(delimiter)
print(b)
print(delimiter.join(b))
