class money:
 def __init__(self,amount,currency):
     self.amount = amount
     self.currency = currency
     
def _lt_(self,other):
    if self .currency !=other .currency: 
        raise  ValueError("different currencies") 
    return self. amount < other .amount
def _gt_ (self,other):
    if self.currency != other.currency:
        raise ValueError("differ currencies")
    return self.amount > other.amount
m1 = money(500,"INR")
m2 = money(1000, "INR")

print(m1 < m2)
print(m1 > m2)
