"""Use object-oriented Python to model a public library 
(w/ three classes: Library, Shelf, & Book). *  
The library should be aware of a number of shelves. 
Each shelf should know what books it contains. Make the book object have
"enshelf" and "unshelf" methods that control what shelf the book is sitting on.
The library should have a method to report all books it contains. 
Note: this should *not* be a Django (or any other) app - just a single file with
three classes (plus commands at the bottom showing it works) is all that is 
needed. In addition to pushing this python file to your Github account, 
please also setup a http://repl.it/languages/Python (so it runs there) and enter
the saved URL here."""

class Library(object):
    def __init__(self):
        self.shelves = [] #lists of all shelves
    
    #add a shelf to library
    def addShelf(self, shelf):
        self.shelves.append(shelf)
    
    #return a string of books in library
    def listOfBooksInLibrary(self):
        strOfBooks = ""
        for shelf in self.shelves:
            strOfBooks += str(shelf.listOfBooksOnShelf()) + " "
        return strOfBooks
    
    #return number of shelves in library        
    def numOfShelves(self):
        return len(self.shelves)
        
class Shelf(object):
    def __init__(self):
        self.books = [] #lists of all books

    def listOfBooksOnShelf(self):
        strOfBooks = ""
        for book in self.books:
            strOfBooks += str(book.title) + " "
        return strOfBooks
        
class Book(object):
    def __init__(self, title):
        self.title = title
    
    #add book to shelf
    def enshelf(self, shelf):
        shelf.books.append(self)
    #remove book from shelf    
    def unshelf(self, shelf):
        shelf.books.remove(self)
        
#Tests
library = Library()

shelf1 = Shelf()
shelf2 = Shelf()
shelf3 = Shelf()

library.addShelf(shelf1)
library.addShelf(shelf2)
library.addShelf(shelf3)

book1 = Book(1)
book2 = Book(2)
book3 = Book(3)
book4 = Book(4)
book5 = Book(5)
book6 = Book(6)
book7 = Book(7)
book8 = Book(8)
book9 = Book(9)

book1.enshelf(shelf1)
book2.enshelf(shelf2)
book3.enshelf(shelf2)
book4.enshelf(shelf3)
book5.enshelf(shelf3)
book6.enshelf(shelf3)
book7.enshelf(shelf1)
book8.enshelf(shelf1)
book9.enshelf(shelf2)

book1.unshelf(shelf1)
book7.unshelf(shelf1)
book8.unshelf(shelf1)

print(library.numOfShelves())
print(library.listOfBooksInLibrary())
