class BankAccount:
  
    def __init__(self,name,phone_number):
     self.phone_number=phone_number
     self.show_balance=0
     self.name=name
     self.borrow=0

    def show_balance(self,amount):
        for transaction in self.balance:
            amount=transaction["amount"]
            narration=transaction["narration"]
            time=transaction["time"]
            date=time.strftime["%d/%m/%y"]
        return f"{date}:{narration} {amount}"
          
    def withdraw(self,amount):
        try:
            10 + amount
        except TypeError:
            return f"The amount must be in figures"
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
      
        def transfer(self,amount):
            try:
                1000 + amount
            except TypeError:
                return f"The amount should be an int"
            fee=amount * 0.5
            total= amount + fee
            if amount > 0:
                return f"Your balance is {self.balance} and you need at least {total} for this transfer"

            else:
                self.balance=total
                account.deposit=(amount)
                return f"You have transfered {amount} to {account} and your balance is this"
        
       def deposit(self,amount):
        self.balance += amount
        return self.show_balance()

        
