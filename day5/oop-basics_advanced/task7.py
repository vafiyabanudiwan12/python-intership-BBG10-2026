class library:
    def __init__(self):
        self._books = []
        
    def add_book(self, title):
         self._books.append(title)
         print(title,"added successfully")
    def remove_book(self, title):
        if title in self._books:
            self._books.remove(title)
            print(title, "removed successfully")
        else:
            print("booknot found")
    def list_books(self):
        return self._books.copy() 
library = library()

library.add_book("python")
library.add_book("java")
library.add_book("c++")

print("All books:", library.list_books())

library.remove_book("java")

print("Updeted books:", library.list_books())
           