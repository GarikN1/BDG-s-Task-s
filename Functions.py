#Max of Three

# Write a Python function to find the Max of three numbers.
# sample input max_of_three(5,11,3)
# sample output 11

# def max_of_three(x ,y ,z):
#     return max(x , y ,z)
# result = max_of_three(5,11,3)
# print(result)




#Letters Count

# Write a Python function to calculate count of each letter in string

# Sample input count_letters(‘abrakadabra’)
# Sample output {a: 5, b: 2, r: 2, k: 1, d: 1}


# def count_letters(input_string):
#     letter_count = {}
#     for letter in input_string:
#         if letter.isalpha():
#             letter = letter.lower()
#             letter_count[letter] = letter_count.get(letter, 0) + 1
#     return letter_count
# result = count_letters("abrakadabra")
# print(result)




# Certainly! Here's a Python function called remove_duplicates that takes a list as an argument and returns a new list with duplicates removed:

# def remove_items(numbers):
#     return list(set(numbers))
# list_1 = [1,1,2,2,3,3,4,5]
# list_2 = remove_items(list_1)
# print(list_2)






# dictionary update write a python function called update_dictionary that takes two dictionaries as argumnets.
# The function should update the first dictionary with the key-value pairs from the second dictionary , and then return the updated dictionary


# def update_dictionary(dict_1, dict_2):
#     dict_1.update(dict_2)
#     return dict_2

# dict_1 = {"a" : 1, "b" : 2}
# dict_2 = {"b" : 3 , "d" : 4}
# update = update_dictionary(dict_1, dict_2)
# print(update)






# def square(x):
#     print(x,"=",x**2)
# for i in range(1,11):
#     square(i) 




# def string_opposite():
#     sentence = input()
#     return sentence[::-1]
# print(string_opposite())



# def sum_and_average(numbers):
#     sum = 0
#     i = 0
#     while i < len(numbers):
#         sum += numbers[i]
#         i += 1 
#     mijiny = sum / len(numbers) 
#     return sum, mijiny#

# numbers1 = [134, 124, 7, 24]
# print(sum_and_average(numbers1))



