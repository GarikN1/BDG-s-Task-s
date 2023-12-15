# # Magic function
# print("mihat")
# print([1,2,3,4])
# print({"mihatel",5,6,7,8})

class MyClass:
    def __init__(self,fname,lname,age):
        self.fname = fname
        self.lname = lname
        self.age = age
        
        
    def __str__(self):  
        return f"{self.fname} {self.lname}  {self.age}"
    
    def __eq__(self,other):
        if self.age == other.age :
        #if self.fname == other.fname and self.lname == other.lname:
            return True
        return False
    
user_1 = MyClass(fname = "Garik" , lname= "Hakobyan" , age = 27 )
user_2 = MyClass(fname= "Avik" , lname="Kaspian", age= 27)
print(user_1 == user_2)
print(user_1)
print(user_2)
