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


    
from datetime import datetime
class BankAccount:
  
    def __init__(self,phone_number,name):
     self.phone_number=phone_number
     self.balance=0
     self.name=name
     self.borrow=0
     self.statement=[]

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
        else:
            self.balance=amount
            now=datetime.now()
            transaction={
                "amount":100,
                "time":now,
                "narration":"you withdrew"
            } 
            def show_statement(self):
                for transaction in self.statement   
                    amount=transaction["amount"]  
                    narration=transaction["narration"]
                    time=transaction["time"]
                    date=time.striftime("%d/%m/%y")
                    print(f"{date}:{narration}:{amount}")
                return
            

    def loan(self,amount):
        return f"Hello your loan balance is {amount}"

    def repayloan(self,amount):
        return f"Hello your loan balance is {amount}"

   def borrowloan(self,loan,amount):
       self.loan=0
       if amount<0:
           return f"Dear {self.name} your loan balance is {amount}"

       elif self.loan > 0:
            return f"Dear {self.name} your loan limit is {amount}"

        elif amount < 0:
            return f"Sorry you do not qualify to withdraw ksh{amount}"
        else:
            self.balance=amount
            now=datetime.now()
            transaction={
                "amount":3000,
                time:"now",
                "narration"="you have borrowed"
            }
            self.statement.append(transaction)
            return f "self.show_balance()"
    

    def repay(self,loan,amount):
        if amount < 0:
            return f "your loan balance is fully settled charging fee is {amount}"
    
        elif amount <= self.loan:
            self.loan -= amount
            return f""
        
        else:
           diff=amount - self.loan
           self.loan=0
           self.deposit(diff)

            now=datetime.now()
            transaction={
                "amount":3000,
                time:"now",
                "narration"="you have repaid"
            }
            self.statement.append(transaction)
            return self.show_balance()


    
        
        
