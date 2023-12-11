import db
import random
from business import Book, Library

def add_book(books):    
    title = input("Title: ")
    author = input("Author: ")
    pages = input("Pages: ")
    book_rank = books.count + 1

    book = Book(title, author, pages, book_rank)
    books.add(book)
    db.add_book(book)
    print(f"{book.title} was added.\n")

def get_library_number(books, prompt):
    while True:
        try:
            number = int(input(prompt))
        except ValueError:
            print("Invalid integer. Please try again.")
            continue

        if number < 1 or number > books.count:
            print("Not a valid book number. Please try again.")
        else:
            return number

def delete_book(books):
    number = get_library_number(books, "Number: ")
    book = books.remove(number)
    db.delete_book(book)
    db.update_book_rank(books)
    print(f"{book.title} was deleted.\n")

def move_book(books):
    old_number = get_library_number(books, "Current rank: ")
    book = books.get(old_number)
    print(f"{book.title} was selected.")
    new_number = get_library_number(books, "New rank: ")

    books.move(old_number, new_number)
    db.update_book_rank(books)
    print(f"{book.title} was moved.\n")

def choose_book(books):
    if not books:
        print("No books to choose from.")
        return
    random_title(books)

def random_title(books):
    if not books:
        print("No books to choose from.")
        return
    chosen_book = random.choice(list(books))
    print(f"You should read {chosen_book.title}.")

def display_library(books):
    if books == None:
        print("There are no books in the library.")        
    else:
        print(f"{'Rank':10}{'Title':25}{'Author':20}{'Pages':>6}")
        print("-" * 64)
        for i, book in enumerate(books, start=1):
            print(f"{book.bookRank:<10d}{book.title:25}{book.author:20}" + \
                  f"{book.pages:6d}")
    print()   

def display_separator():
    print("=" * 64)

def display_title():
    print("                           Kindle Books")

def display_menu():
    print("MENU OPTIONS")
    print("1 – Display library")
    print("2 – Add book")
    print("3 – Remove book")
    print("4 – Change book ranking")
    print("5 – Choose random title to read")
    print("6 - Exit program")
    print()

def main():
    display_separator()
    display_title()
    display_menu()

    db.connect()
    books = db.get_books()
    if books == None:
        books = Library()         
    
    display_separator()
    
    while True:
        try:
            option = int(input("Menu option: "))
        except ValueError:
            option = -1
            
        if option == 1:
            display_library(books)
        elif option == 2:
            add_book(books)
            books = db.get_books()
        elif option == 3:
            delete_book(books)
        elif option == 4:
            move_book(books)
        elif option == 5:
            random_title(books)
        elif option == 6:
            db.close()
            print("Bye!")
            break
        else:
            print("Not a valid option. Please try again.\n")
            display_menu()

if __name__ == "__main__":
    main()
