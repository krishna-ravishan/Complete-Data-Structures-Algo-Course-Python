# # new_list = [new_item for item in list if condition]

# prev_list = [-1, 10, -20, 2, -90, 60, 45, 20]

# new_list = [item for item in prev_list if item >= 0]

# print(new_list)

# # Take the square of the negative number

# new2_list = [item*item for item in prev_list if item < 0]

# print(new2_list)

# sentence = "My name is Krishna"

# def is_consonant(letter):
#     vowels = "aeiou"
#     return letter.isalpha() and letter.lower() not in vowels

# consonants = [i.lower() for i in sentence if is_consonant(i)]

# print(consonants)

# new3_list = [number if number > 0 else 'Negative Number' for number in prev_list]

# print(new3_list)

a=[1,2,3,4,5]
print(a[3:0:-1])