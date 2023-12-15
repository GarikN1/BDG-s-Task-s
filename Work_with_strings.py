#1. Write a Python program to get a string made of the first 2 and the last 2 chars from a
#given string.

#Example:
#Sample String : 'w3resource'
#Expected Result : 'w3ce'
#__________________________

#Sample String : 'w3'
#Expected Result : 'w3w3'

#text = "w3resource"
#text[0:2] + text[8: ]
#print(text)

#text = "w3resource"
#text[0:2] + text[0:2]

#2. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If
#the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string
#is less than 3, leave it unchanged.

#Example:
#Sample String : 'abc'
#Expected Result : 'abcing'
#_______________________

#Sample String : 'string'
# Result : 'stringly'

#text1 = "abc"
#text2 = "ing"
#text = text1 + text2
#print(text)

#text1 = "string"
#text2 = "ly"
#text = text1 + text2
#print(text)

#3. Write a Python program to remove the n-th index character from a nonempty string.
#Example:
#Sample string: ‘abcdefgh’
#n - 3
#Expected result: abcefgh

#text = "abcdefg"
#text = [0:3] + text[4: ]
#print(text)

#4. Write a Python program to change a given string to a new string where the first and last chars
#have been exchanged.
#Example:
#ample: ‘abcdefgh’
#Expected: ‘hbcdefga’

#text = "abcdefgh"
#"h" + text[1: ]
#print(text)

#5. Write a Python function to get a string made of 4 copies of the last two characters of a
#specified string (length must be at least 2).
#Example:
#Sample = ‘Python'
#Expected onononon
#________________
#Sample 'Exercises'
#Expected eseseses

#text = "python"
#text[4: ] + text[4: ] + text[4: ]
#print(text)



# 7-Write a Python program to print the floating numbers upto 2 decimal places
# (number must be not greater than 10)
# Example:
# Sample = 2.145548
# Expected - 2.14
# _______________________
# Sample = 9.5748
# Expected - 9.57

# a = 2.145548
# round(a , 2)

# a = 9.5748
# round(a , 2)



# 9. Append new string in the middle of a given (even number of characters) string
# Example:

# Sample = ‘python’
# new_string = ‘new’
# Expected ‘pytnewhon

# text1 = "python"
# text2 = "new"
# text[0:3] + "new" + [3: ]
# print(text)
