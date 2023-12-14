#Conditional statements in Python and for loop
# 1.Multiply
# Write a Python program to multiply all the items in a list.

# Sample input
# [1, 2, 3, 4]
# [5,7,3,9,11]
# [24,1,1,13]

# Sample Output
# 24
# 10395
# 325

# a = [1,2,3,4,]
# total = 1
# for i in a:
#     total *= i
#     print(total)

# a = [5,7,3,9,11]
# total = 1
# for i in a:
#     total *= i
#     print(total)

# a = [24,1,1,13]
# total = 1
# for i in a:
#     total*= i
#     print(total)

# 6.Square
# # Turn every item of a list into its square

# Sample Input
# [5, 7, 3, 9, 11]

#Sample output
#[25, 49, 9, 81, 121]

a = [5,7,3,9,11]
b = [i ** 2 for i in a]
print(b)