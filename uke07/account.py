"""
1. Explain the code to the person next to you
2. Try to make changes, use property
3. What other classes to you feel should be here (think simple), if this is an account in a bank.
"""

class Account:

    def __init__(self, balance=0):
        self._balance=balance
        
    #getter and setter
    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, new_balance):
        self.balance = new_balance
    
    #special methods
    def withdraw(self,amount):
        if self._balance<amount:
            raise ValueError("You dont have that much of money!")
        else:
            self._balance-=amount
            
    def deposit(self, amount):
        self.balance += amount