class Inventory:
 def __init__(self, items):
     self.items = items
 def _len_(self):
     return len(self.items)
 def _getitem_(self,index):
     return self.items[index]
i =  Inventory(["pen", "book", "pencil"])
print(len(i))
print(i[1])
    