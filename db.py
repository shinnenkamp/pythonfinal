import sqlite3
from contextlib import closing

from business import Book, Library

conn = None

def connect():
    global conn
    if not conn:
        DB_FILE = "final.sqlite"
        conn = sqlite3.connect(DB_FILE)
        conn.row_factory = sqlite3.Row

    with conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS Book (
                    bookID INTEGER PRIMARY KEY,
                    bookRank INTEGER,
                    title TEXT,
                    author TEXT,
                    pages INTEGER
                )
            ''')

def close():
    if conn:
        conn.close()

def make_book(row):
    return Book(row["title"], row["author"],
                  row["pages"], row["bookRank"], row["bookID"])

def get_books():    
    query = '''SELECT bookID, bookRank, title, author, pages
               FROM Book
               ORDER BY bookRank'''
    with closing(conn.cursor()) as c:
        c.execute(query)
        results = c.fetchall()

    books = Library()
    for row in results:
        book = make_book(row)
        books.add(book)
    return books

def get_book(id):
    query = '''SELECT bookID, bookRank, title, author, pages
               FROM Book
               WHERE bookID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (id,))
        row = c.fetchone()
        if row:
            book = make_book(row)
            return book
        else:
            return None

def add_book(book):
    sql = '''INSERT INTO Book
               (title, author, pages, bookRank) 
             VALUES
               (?, ?, ?, ?)'''
    with closing(conn.cursor()) as c:
        c.execute(sql, (book.title, book.author, book.pages,
                        book.bookRank))
        conn.commit()

def delete_book(book):
    sql = '''DELETE FROM Book WHERE bookID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(sql, (book.bookID,))
        conn.commit()

def update_book_rank(library):
    for num, book in enumerate(library, start=1):
        book.bookRank = num
        sql = '''UPDATE Book
                 SET bookRank = ?
                 WHERE bookID = ?'''
        with closing(conn.cursor()) as c:
            c.execute(sql, (book.bookRank, book.bookID))
    conn.commit()      

def main():
    connect()
    books = get_books()
    for book in books:
        print(book.bookRank, book.title, book.author, book.pages)


if __name__ == "__main__":
    main()
