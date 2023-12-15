# 1.Arrange
# Arrange string characters such that lowercase letters should come first

# Sample input
# PyNaTive

# Sample output
# yaivePNT

# word = "PyNaTive"
# lowercase = []
# uppercase = []

# for char in word:
#     if char.islower():
#         lowercase += char
#     else:
#         uppercase += char

# arranged_string = ''.join(lowercase + uppercase)
# print(arranged_string)

#2 Count
# Count all letters, digits, and special symbols from a given string

# Sample Input
# P@#yn26at^&i5ve

# Sample Output
# chars = 8
# digits = 3
# symbol = 4

# string = "P@#yn26at^&i5ve"
# char_count = 0
# digit_count = 0
# symbol_count = 0

# for char in string:
#     if char.isalpha():
#         char_count += 1
#     elif char.isdigit():
#         digit_count += 1
#     else:
#         symbol_count += 1

# print("chars =", char_count)
# print("digits =", digit_count)
# print("symbols =", symbol_count)


# 3.Balance
# Write a program to check if two strings are balanced. For example, strings s1 and
# s2 are balanced if all the characters in the s1 are present in s2. The character’s
# position doesn’t matter.

# Sample input
# s1 = "Yn"
# s2 = "PYnative"    #True

# s1 = "Ynf"
# s2 = "PYnative"   #False


# s1 = "Yn"
# s2 = "PYnative"