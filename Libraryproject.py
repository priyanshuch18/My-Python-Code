class Library():
    def __init__(self, listOfBooks):
        self.books = listOfBooks 
        pass
    def displayAvailableBooks(self):
        print("the books present in this library are:")
        for book in self.books:
            print(" *" +book)
    def borrowBook(self, bookName):
        if bookName in self.books:
            print("you have been issued{bookName}.Please keep it safe and return it within 30 days")
            self.books.remove(bookName)
            return True
        else:
            print("sorry this book is already been issued")
            return False
    def returnBook(self,bookName):
        self.books.append(bookName)
        print("hope you enjoyed it")
class Student():
    def requestBook(self):
        reqBook = input("enter the name of the book you want to borrow")
        return self.book
    def returnBook(self):
        self.book= input("enter the name of the book you want to borrow")
        return self.book
if __name__ == "__main__":
    centralLibrary = Library(["algorithm", "django", "clrs"])
    centralLibrary.displayAvailableBooks()
    student = Student()
    while(True):
        welcomeMsg = '''=====WELCOME TO CENTRAL LIBRARY====
        Please choose an option:
        1. Listing all the books
        2. Request a book
        3. Return a book
        4. Exit the library'''
        print(welcomeMsg)
        a = int(input("Enter the choice: "))
        if  a== 1:
            centralLibrary.displayAvailableBooks()
        elif a ==2:
            centralLibrary.borrowBook(student.requestBook())
        elif a == 3:
            centralLibrary.returnBook(student.returnBook())
        elif a == 4:
            print("thanks for choosing central library have a great day ahead")
            exit()
        else:
            print("Invalid Choice")
        
