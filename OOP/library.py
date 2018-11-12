class Library:

    def __init__(self, listOfAvailableBooks):
        self.availableBooks = listOfAvailableBooks
        
    def displayAvailableBooks(self):
        print()
        print("Available Books: ")
        for book in self.availableBooks:
            print(book)
        print('\n')
        
    def lendBook(self, requestedBook):
        if requestedBook in self.availableBooks:
            print("\nYou have now borrowed the book \n")
            self.availableBooks.remove(requestedBook)
        else:
            print("\nSorry, the book is not available in our list \n")
        
    def addBook(self, returnedBook):
        self.availableBooks.append(returnedBook)
        print("\nYou have returned the book. Thank you!! \n")
        
        
class Customer:
    def requestBook(self):
        print("Enter the name of the book you would like to borrow: ")
        self.book = input()
        return self.book
        
    def returnBook(self):
        print("Enter the name of the book which you are returning: ")
        self.book = input()
        return self.book
    
library = Library(['A Game of Thrones', 'A Clash of Kings', 'A Storm of Swords', 'A Feast for Crows', 'A Dance with Dragons'])
customer = Customer()

while True:
    print("Enter 1 to display the available books")
    print("Enter 2 to request for a book")
    print("Enter 3 to return a book")
    print("Enter 4 to exit")
    print("\n")
    userChoice = int(input())
    
    if userChoice == 1:
        print('\n')
        library.displayAvailableBooks()
    elif userChoice == 2:
        print('\n')
        requestedBook = customer.requestBook()
        library.lendBook(requestedBook)
    elif userChoice == 3:
        print('\n')
        returnedBook = customer.returnBook()
        library.addBook(returnedBook)
    elif userChoice == 4:
        break
