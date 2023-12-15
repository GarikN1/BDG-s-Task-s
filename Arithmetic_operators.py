 #1. Sum
# #Input two integers and print out their sum. Preserve the exact format from
# #the examples (e.g. the output should contain exactly three lines)

#a = 4
#b = 5
# #a = int(input())
# #b = int(input())
# sum = a + b
# print(sum)

#a = 17
#b = 8

# a = int(input())
# b = int(input())
# sum = a + b
# print(sum)

# 2.The Last Digit
# Input a natural number N and output its last digit.

#Sample Input 156, 789155, 7;
#Sample Output 6, 5, 7

# result = 156 % 10
# print(result)

# result = 789115 % 10
# print(result)

# result = 7 % 10
# print(result)


# 4 Comparison 
# Input two positive integers, and output a line describing their relation.
# Follow the sample format.

# Sample input 7 9 ,11 11 , 4 -4
# Sample output 7 < 9 , 11 = 11 , 4 > -4

# a = int(input())
# b = int(input())
# if a < b:
#     print(a, "<",  b)

# a = 11
# b = 11
# a = int(input())
# b = int(input())
# if a = b:
#     print (a, =, b)

# a = 4
# b = -4
# a = int(input())
# b = int(input())
# if a > b:
#     print (a > b)

# 5.Birth Year
# Փոփոխված
# The program prompts the user their birth year. Assuming a person’s age
# is a non-negative integer not exceeding 120, output the user’s age or the
# words “Incorrect Year”. The sample outputs assume it’s currently the year
# 2016. If you are writing this program during any other year, the correct
# answers may differ. Store the value of the current year in a variable.
# Sample input 2016 , 2018 , 1903
# Sample output 7 , 5 , 120 

# current_year = 2023
# birth_year = int(input()) #2016
# age = current_year - birth_year:
# if birth_year <= current_year:
#     print(age , 7)

# current_year = 2023
# birth_year = int(input()) #2018
# age = current_year - birth_year:
#     if birth_year <= current_year
#     print(age, 5)

# current_year = 2023
# birth_year = int(input(1903)) 
# age = current_year - birth_year
# if birth_year <= current_year:
#     print (120 , age)

#6Three Numbers
# Input three integers. Output the word “Sorted” if the numbers are listed in
# a non-increasing or non-decreasing order and “Unsorted” otherwise.

# Sample Input
# 1 2 3 
# 1 3 2
# 5 0 -4
# 9 9 9 
# 9 9 0
# Sample output
# sorted
# unsorted
# sorted
# sorted
# sorted
# a = int(input("1"))
# b = int(input("2"))
# c = int(input("3"))
# if a <= b <= c:
#     print("sorted")
# else:
#     print("Unsorted")

# a = int(input(1))
# b = int(input(3))
# c = int(input(2))
# if a <= b <= c:
#     print("sorted")
# else:
#     print("Unsorted")

# a = int(input(9))
# b = int(input(9))
# c = int(input(9))
# if a = b = c:
#     print("sorted")
# else:
#     print("Unsorted")
    
# a = int(input(9))
# b = int(input(9))
# c = int(input(0))
# if a <= b >= c:
#     print("sorted")
# else:
#     print("Unsorted")

#8 Salaries
# Given the salaries of three employees working at a department, find the
# amount of money by which the salary of the highest-paid employee differs
# from the salary of the lowest-paid employee. The input consists of three
# positive integers - the salaries of the employees. Output a single number,
# the difference between the top and the bottom salaries

# Sample input

# 100 500 1000
# 500 100 1000
# 36 11 20
# 20 20 20

# Sample output
# 900
# 900
# 25
# 0

# salaries = input(100 500 1000)
# salaries_list = list(map(int, salaries.split()))
# max_salary = max(1000)
# min_salary = min(100)
# difference = max_salary - min_salary
# print(difference)

# salaries = input(500 100 1000)
# salaries_list = list(map(int, salaries.split()))
# max_salary = max(1000)
# min_salary = min(100)
# difference = max_salary - min_salary
# print(difference)

# salaries = input(36 11 20)
# salaries_list = list(map(int, salaries.split()))
# max_salary = max(36)
# min_salary = min(11)
# difference = max_salary - min_salary
# print(difference)

# salaries = input(20 20 20)
# salaries_list = list(map(int, salaries.split()))
# max_salary = max(20)
# min_salary = min(20)
# difference = max_salary - min_salary
# print(difference)

#9 Rounding - 2

# Given a real number, round it to the nearest whole.
# Sample Input 0.3 , 1.2398 , 1.5 , 67.567
# Sample output 0 , 1 , 2 , 68

# Terminal

# a = 0.3
# round(a)

# a = 1.2398
# round(a)

# a = 1.5
# round(a)

# a = 67.567
# round(a)


# 3 , 7 , 8- Chem arel
