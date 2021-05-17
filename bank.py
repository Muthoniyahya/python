class BankAccount:
    Brand="Equity"
    def __init__(self,services,salary):
     self.services=services
     self.salary=salary

    def opinion(self):
        return f"Equity offers one of the best {self.services}"

    def income(self):
        return f"Employers earn more than enough money for their upkeep ${self.salary}."

