class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = True


class Library:
    def __init__(self):
        self.books = []

    # Add a new book
    def add_book(self, book):
        for b in self.books:
            if b.book_id == book.book_id:
                print("Error: Book ID already exists!")
                return

        self.books.append(book)
        print("Book added successfully!")

    # Display all books
    def view_books(self):
        if not self.books:
            print("No books available in the library.")
            return

        print("\n========== BOOK LIST ==========")

        for book in self.books:
            print("\nBook ID:", book.book_id)
            print("Title:", book.title)
            print("Author:", book.author)

            if book.is_available:
                print("Status: Available")
            else:
                print("Status: Issued")

            print("-------------------------------")

    # Search book by ID
    def search_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                print("\nBook Found!")
                print("\nBook ID:", book.book_id)
                print("Title:", book.title)
                print("Author:", book.author)

                if book.is_available:
                    print("Status: Available")
                else:
                    print("Status: Issued")

                return book

        print("Error: Book not found!")
        return None

    # Issue a book
    def issue_book(self, book_id):
        book = self.search_book(book_id)

        if book is None:
            return

        if book.is_available:
            book.is_available = False
            print("Book issued successfully!")
        else:
            print("Sorry! This book is already issued.")

    # Return a book
    def return_book(self, book_id):
        book = self.search_book(book_id)

        if book is None:
            return

        if not book.is_available:
            book.is_available = True
            print("Book returned successfully!")
        else:
            print("This book is already available.")


# Main Menu Function
def main():
    library = Library()

    while True:
        print("\n========== LIBRARY MANAGEMENT SYSTEM ==========")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            try:
                book_id = int(input("Enter Book ID: "))
                title = input("Enter Book Title: ")
                author = input("Enter Author Name: ")

                book = Book(book_id, title, author)
                library.add_book(book)

            except ValueError:
                print("Please enter a valid Book ID!")

        elif choice == "2":
            library.view_books()

        elif choice == "3":
            try:
                book_id = int(input("Enter Book ID: "))
                library.search_book(book_id)
            except ValueError:
                print("Please enter a valid Book ID!")

        elif choice == "4":
            try:
                book_id = int(input("Enter Book ID: "))
                library.issue_book(book_id)
            except ValueError:
                print("Please enter a valid Book ID!")

        elif choice == "5":
            try:
                book_id = int(input("Enter Book ID: "))
                library.return_book(book_id)
            except ValueError:
                print("Please enter a valid Book ID!")

        elif choice == "6":
            print("Thank you for using the Library Management System!")
            break

        else:
            print("Invalid choice! Please select between 1 and 6.")


# Run the program
if __name__ == "__main__":
    main()