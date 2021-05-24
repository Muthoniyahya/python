# class BankAccount:
  
#     def __init__(self,service,salary,phone_number,name):
#      self.services=services
#      self.salary=salary
#      self.phone_number=phone_number
#      self.balance=0
#      self.name=name

#     def opinion(self):
#         return f"Equity offers one of the best {self.services}"

#     def income(self):
#         return f"Employers earn more than enough money for their upkeep ${self.salary}."

#     def show_balance(self):
#         return f"Hello {self.name} your balance is {self.balance}"

#     def deposit(self,amount):
#         self.balance += amount
#         return self.show_balance()
#     def withdraw(self,amount)
#         if amount >self.balance
#         return f


    

class BankAccount:
  
    def __init__(self,phone_number,name):
     self.phone_number=phone_number
     self.balance=0
     self.name=name
     self.borrow=0

    def show_balance(self):
        return f"Hello {self.name} your balance is {self.balance}"

    def deposit(self,amount):
        if amount > 0:
           self.balance += amount
           return self.show_balance()

        else:
            
            return f"Dear customer you have insufficient funds your balance is {self.balance}"

    def withdraw(self,amount):
        if amount > self.balance:
            return f"Hello your account balance is {self.balance} you cannot withdraw {amount}"

    def loan(self,amount):
        return f"Hello your loan balance is {amount}"

    def repayloan(self,amount):
        return f"Hello your loan balance is {amount}"
        
    


    



















