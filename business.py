from dataclasses import dataclass

@dataclass
class Book:
    title:str = ""
    author:str = ""
    pages:int = 0
    bookRank:int = 0
    bookID:int = 0

class Library:
    def __init__(self):
        self.__list = []

    @property
    def count(self):
        return len(self.__list)

    def add(self, book):
        return self.__list.append(book)
    
    def remove(self, number):
        return self.__list.pop(number-1)
    
    def get(self, number):
        return self.__list[number-1]
    
    def set(self, number, book):
        self.__list[number-1] = book
        
    def move(self, oldNumber, newNumber):
        book = self.__list.pop(oldNumber-1)
        self.__list.insert(newNumber-1, book)

    def __iter__(self):
        for book in self.__list:
            yield book
            
        
def main():
    library = Library()
    library.add(Book(1, "Summit Lake", "Charlie Donlea", 337))
    library.add(Book(2, "The Last Mrs. Parrish", "Liv Constatine", 403))
    
    for book in library:
        print(book.bookRank, book.title, book.author, book.pages)
        
    print("Bye!")

if __name__ == "__main__":
    main()

