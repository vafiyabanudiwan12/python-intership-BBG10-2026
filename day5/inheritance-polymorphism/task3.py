class Account:
    def get_interest_rate(self):
        return 4
class SavingsAccount(Account):
    def get_interest_rate(self):
        return 6
class FixedDeposit(Account):
    def get_interest_rate(self):
        return 8
Accounts = [Account(),SavingsAccount(),FixedDeposit()]
for account in Accounts:
  print("interest rate:", account.get_interest_rate(),"%")
          
        