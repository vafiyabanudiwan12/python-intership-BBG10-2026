class stack:
 def _init_(self):
     self._items =[]
def push(self,item):
 self ._items.append(item) 
 def pop(self):
     if self._items:
         return self._items.pop()
     return "stack is empty"
 def _str_(self):
     return str(self._items)
 s = stack
 s.push(10)
 s.push(20)
 s.push(30)
 
 print(s)
 print(s.pop())
 print(s) 