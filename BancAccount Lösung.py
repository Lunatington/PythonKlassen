class BankAccount: 
	#The constructor 
    def __init__(self, balance: float, owner: str):
        self.__balance = balance 
        self.__owner = owner 
        
    def addbalance(self, betrag: float):
        self.balance += betrag
        
    def removebalance(self, betrag: float):
        self.balance -= betrag
  

peters_account = BankAccount(100, "Peter Python") 
paulas_account = BankAccount(20000, "Paula Pythons")

print(peters_account._BankAccount__balance) 
print(paulas_account._BankAccount__balance)
