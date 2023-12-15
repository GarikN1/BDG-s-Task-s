# 1) Write a Python program to read the whole text of a file and catch the error if files does not exists
# file_path = "BDG.txt"
# try:
#     # with open(file_path,"r") as file:
#     with open("BDG.txt","r") as file:

#         file = file.read()
#         print(file)
# except  FileNotFoundError:
#     print("This file does not exist")

# 2) 
# Wrie a python program to catch error a num dividing by zero.

# x = 10
# y = 0

# try:
#     z = x / y
#     print(z, "anverjutyn")
# except ZeroDivisionError :
#     print("ZeroDivisionError")

# 3) 
#Write a python program that will raise an exception (Invalid File) if text file contents first symbol with number


# file_path = "BDG.txt"
# with open("BDG.txt", "r") as file:
#         file = file.read(1)
#         if file.isdigit():
#             raise Exception ("invalid file")