# # OOP Encapsulation

# class Person:
#     def __init__(self,name,age = 0):
#         self.name = name
#         self.__age = age
        
# person = Person("Dev",30)
# print(person.name)
# #print(person.__dir__())
# print(person._Person__age)

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.__age = age
    
#     def get_age(self):
#         return self.__age
    
#     def set_age(self,new_age):
#         if 0 <= new_age <= 120:
#             self.__age = new_age
#         else:
#             print("invalid age value")


# class Person:
#      def __init__(self,name,age):
#          self.name = name
#          self.__age = age
         
#      @property
#      def age(self):
#          return self.__age

#      @age.setter
#      def age(self,new_age):
#          if 0 <= new_age <= 120:
#              self.__age = new_age
#          else:
#              print("invalid age value")

# programer = Person("Vzgo", 30)
# print(programer.name) 
# print(programer.age)
# programer.age = 121
# print(programer.age)




# Exercise:
#
# ● Create a BankAccount class with private and public attributes.
# account_number (public)
# balance (private)
# owner_name (public)
# 
# ● Implement the following methods:
# __init__(self, account_number, initial_balance, owner_name): Initialize the
# account_number, balance, and owner_name attributes.
# deposit(self, amount): Add the given amount to the balance.
# withdraw(self, amount): Deduct the given amount from the balance if there
# are sufficient funds.
# get_balance(self): Return the current balance.
# display_account_info(self): Print the account number, owner's name, and
# current balance.
# 
# ● Demonstrate the use of this class by creating a BankAccount object, making
# deposits and withdrawals, and displaying account information.


# class BankAccount:
#     def __init__(self,account_number,initial_balance,owner_name):
#         self.account_number = account_number
#         self.__balance = initial_balance
#         self.owner_name = owner_name
        
        
#     def deposit(self,amount):
#         if amount > 0 :
#             self.__balance += amount
    
    
#     def windraw(self,amount):
#         if amount > 0 and self.__balance>= amount:
#             self.__balance -= amount
            
#     def get_balance(self,):
#         return self.__balance
    
#     def display_account_info(self):
#         print(f"Account number:{self.account_number}")
#         print(f"Initial balance: {self.__balance}")
#         print(f" Owner name : {self.owner_name}")
        
# #if __name__ == "__main__": 
# account = BankAccount("N1" , 1000000 , "Garo jan")
# account.deposit(500)
# account.windraw(200)
# account.display_account_info()





# write a class named temperatures that has the attribute temperature(private).,default value is 0

# class TemperaturesSensor:
#     def __init__(self,temperatures= 0):
#         self.__temperatures = temperatures
        
#     @property
#     def temperatures(self):
#         return self.__temperatures
    
#     @temperatures.setter
#     def temperatures(self,new_temperatures):
#         if 0 <= new_temperatures:
#             self.__temperatures = new_temperatures
#         else:
#             raise Exception("curta")
    
# temperatures = TemperaturesSensor(95)
# print(temperatures.temperatures)        
# temperatures.temperatures = -5