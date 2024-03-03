class BankAccount: 
	#The constructor 
    def __init__(self, balance: float, owner: str):
        self.balance = balance 
        self.owner = owner 
  

peters_account = BankAccount(100, "Peter Python") 
paulas_account = BankAccount(20000, "Paula Pythons")

print(peters_account.balance) 
print(paulas_account.balance)
