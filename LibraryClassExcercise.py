import os
class Library:
    def __init__(self, filename):
        self._filename = filename

    def print_Books(self):
        if os.path.exists(self._filename):
            with open(self._filename, "r") as file:
                while True:
                    line = file.readline()  # readline() method reads a single line from the file.
                    if not line:
                        break
                    print(line, end = "")

    def addBook(self, strBook):
        if not os.path.exists(self._filename):
            open(self._filename, "w").close()  # Create empty file
            print(f"\nLibrary '{self._filename}' created.")
        with open(self._filename, "a") as f:
            f.write(strBook + "\n")


    def getNoOfBooks(self):
        try:
            with open(self._filename, "r") as f:
                line_count = sum(1 for _ in f)
            return line_count
        except FileNotFoundError:
            print(f"Error: File '{self._filename}' not found.")
            return 0


FILE_NAME = input("Enter your Library Name: \n")
libObj = Library(FILE_NAME+".txt")

while True:
    print("\n1. Print all books")
    print("2. Add a book")
    print("3. Get the number of books")
    print("4. Exit this library")
    userChoice = input("Enter your choice: \n")
    match userChoice:
        case "1":
            libObj.print_Books()
        case "2":
            strBook = input("Enter the name of the book: ")
            libObj.addBook(strBook)
        case "3":
            print("The number of books is: ", libObj.getNoOfBooks())
        case "4":
            break