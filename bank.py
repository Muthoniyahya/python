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

    def show-balance(self):
        for transaction in self.balance:
            amount=transaction["amount"]
            narration=transaction["narration"]
            time=transaction["time"]
            date=time.strftime["%d/%m/%y"]
          print(f"{date}:{narration} {amount}")
        return  
    def withdraw(self,amount):
        if amount>self.balance:
            return f"your balance is {self.balance} you cannot withdraw{amount}"
        else:
            self.balance-=amount
            now=datetime.now()
            withdrawals={"amount":amount,"time":now,"narration":"you have withdrawn"}#a dictionary with transaction details
            self.statement.append(withdrawals)
        return self.show_balance()

    def borrow(self,amount):
        if amount <0:
            return f"you cannot borrow a negative amount"
        elif self.loan>0:
            return f"you cannot borrow an amount of {amount}"
        elif amount>0.1*self.balance:
            return f" you do not qualify for the loan of ksh {amount}"
        else:
            loan=amount*1.05
            self.loan=loan
            self.balance+=amount
            now=datetime.now()
            borrow_transaction={"amount":amount,"time":now,"narration":"you have borrowed ksh"}
            self.statement.append(borrow_transaction)
            return f"your outstanding loan is ksh {self.loan}"

    def repay_loan(self,amount):
        if amount<0:
            return "you cannot repay with a negative amount"
        elif amount<=self.loan:
            loan_balance=self.loan-amount
            return f"you have paid ksh{amount} your outstanding loan balance is {loan_balance} "
        else:
             
            excess=amount-self.loan
            self.loan=0
            self.deposit(excess)
            now=datetime.now()
            repay_transaction={"amount":amount,"time":now,"narration":"you have repaid your loan of ksh"}
            self.statement.append(repay_transaction)
            return f"you have fully repaid your loan and your excess of ksh {excess} has been deposited in your account,your balance is {self.balance} "
      
