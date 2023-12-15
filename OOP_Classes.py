# Ex_ABC
# ex 1
# write an abstract class with name Employee
# write 2 employee classes by inherting from abstracts Employee
# write function
#     get_info -> return string with name and position
#     calculate_salary -> return float with information employee salary


from abc import ABC, abstractclassmethod





#ex 2

# Write an abstract class with name GeometricFigure
# write 2 geometric figure classes by inherting from gEOMETRICfIGURE
# WRITE 2 function
#  get_perimeter > return string with information about capital city
#  get_are -> return string with information about  language

# from math import pi
# from abc import ABC, abstractclassmethod

# class GeometricFigure(ABC):
#     @abstractclassmethod
#     def get_perimeter(self):
#         pass
    
#     @abstractclassmethod
#     def get_area(self):
#         pass
    
    
# class Square(GeometricFigure):
    
#     def get_perimeter(self, a):
#         return a * 4 
    
#     def get_area(self, a):
#         return a ** 2
    
# square_1 = Square()

# print(square_1.get_perimeter(8))
# print(square_1.get_area(8))
    
# class Circle(GeometricFigure):
#     def get_perimeter(self,r):
#         return pi * r
    
    
#     def get_area(self,r):
#         return  pi *r *r 
    
# circle_1 = Circle()
# print(Circle.get_perimeter(8,8))
# print(Circle.get_area(8,8))