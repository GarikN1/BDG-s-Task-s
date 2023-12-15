# #Classh_task
# # Define a class named BankAccount with an __init__ method that initializes two
# # instance variables: account_holder and balance.
# # The class has methods like deposit and withdraw, each of which takes an amount as
# # an argument and updates the account balance accordingly. These methods also
# # include checks for valid input and available funds.
# # The get_balance method allows you to retrieve the account balance.
# # We create an Object of the BankAccount class called account1 with an initial balance
# # of $1000.
# # We deposit $500 and withdraw $200 from the account and print the account
# # information.

# class BankAccount:
#     def __init__(self,account_name,balance):
#         self.account_name = account_name
#         self.balance = balance
        
#     def deposit(self,amount):
#             if amount > 0:
#                 self.balance += amount
#                 print("deposit" f"{amount}", "New Balanc" f"{self.balance}")
#             else: print("0")
            
#     def windtraw(self, amount):
#             if 0 < amount <= self.balance:
#                 self.balance -= amount
#                 print("Wintdraw" f"{amount}", "New Balanc :" f"{self.balance}")
#             else: print(0)
            
#     def get_balance(self):
#                 return self.balance
            
# account1 = BankAccount("Garik",1000)
# account1.deposit(500)
# account1.windtraw(200)
# print(f"Account name : {account1.account_name}")
# print(f"Account banalce : {account1.get_balance()}")

# 2. Class task:
# Create a Python class representing a Hospital account with methods to schedule visit
# and remove schedule


# class Hospital:
#     def __init__(self,pacienti_anun):
#         self.pacienti_anun = pacienti_anun
#         self.pacient = []
        
        
#     def ekela(self, data, jam):
#         ekela = (data , jam)
#         if ekela not in self.pacient:
#             self.pacient.append(ekela)
#             print(f"pacient@ ekela {data} ,{jam}")
#         else:print("tenc mard chi ekel")
    
        
#     def dursgal(self,data,jam):
#         gnacela = (data,jam)
#         if gnacela not in self.pacient:
#             print("wertyui ", self.pacient)
#             self.pacient.remove(gnacela)
#             print(f"gnacela {data},{jam}")
#         else:print("tenc mard chi ekel")
        
#     def stugum(self):
#         if self.pacient:
#             print(self.pacienti_anun)
#         for (ekela, gnacela) in self.pacient:
#             print({ekela[0]} , {gnacela[1]})
#         else:print("tenc mard chka")
        
# hivand = Hospital("Garo jan")
# hivand.ekela("06.09.2023", "15:26")
# hivand.stugum ()
# hivand.gnacela("06.09.2023", "18:00")
# hivand.stugum ()

#Other task
# Vehicle 
# create a Bus class that inherits from the Vehicle class. Give capacity argument of Bus.seating_capacity a default value 50 
# use the following code for your parentvehicle class


# class Vehicle:
#     def __init__(self,color,mark,year):
#         self.color = color
#         self.mark = mark
#         self.year = year
        
#     def full_name(self):
#         return f"{self.color} {self.mark} {self.year}"
    
# class Bus(Vehicle):
#     def __init__(self, color, mark, year,seats):
#         super().__init__(color, mark, year,)
#         seats = 50
#         self.seats = seats

# Bus_1 = Bus("White","Paz","1945",50)
# print(Bus)