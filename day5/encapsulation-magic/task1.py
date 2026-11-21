class wallrt:
    def __init__(self, initial_balance=0):
        if initial_balance< 0:
         raise ValueError("Initial balance cannot be negative.")
        self._balance = initial_balance
    @property
    def balance(self):
        return self._balance
    def deposit(self, amount):
        if amount <=0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += amount
    def withdraw(self,amount):
        if amount <= 0:
            raise ValueError("withdrawal amount masut be positive.")
        if amount > self._balance:
            raise ValueError("Insufficient balance")
        self._balance -=amount         
        