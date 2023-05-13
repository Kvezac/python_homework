from abc import ABC
from datetime import datetime





class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre


class Librarian(ABC):
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id

class Reader(Librarian):
    def __init__(self, name, age, id):
        super().__init__(name, age, id)


class Library:
    """ Создайте приложение для работы в библиотеке. Оно
    должно оперировать следующими сущностями: Книга,
    Библиотекарь, Читатель. Приложение должно позволять
    вводить, удалять, изменять, сохранять в файл, загружать из
    файла, логировать действия, искать информацию (результаты поиска
    выводятся на экран или файл) о сущностях. При реализации
    используйте максимально возможное количество паттернов проектирования.
    """
    def __init__(self):
        self.books = []
        self.readers = []

    def add_book(self, book):
        self.logger(f"Book '{book.title}' added to the library")
        self.books.append(book)

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.logger(f"Book '{book.title}' remove")
                self.books.remove(book)

    def edit_book(self, title, author=None, year=None, genre=None):
        for book in self.books:
            if book.title == title:
                if author:
                    book.author = author
                if year:
                    book.year = year
                if genre:
                    book.genre = genre

    def save_to_file(self):
        filename = 'library_log.txt'
        with open(filename, 'w') as f:
            for book in self.books:
                self.logger(f"Save to {filename}")
                f.write(f"{book.title},{book.author},{book.genre}\n")

    def load_from_file(self):
        filename = 'library_log.txt'
        with open(filename, 'r') as f:
            lines = f.readlines()
            for line in lines:
                title, author, genre = line.strip().split(',')
                book = Book(title, author, genre)
                self.books.append(book)
                self.logger(f"Losd book '{book.title}'")


    def logger(self, action):
        with open('log.txt', 'a') as f:
             f.write(f"{datetime.now()}: {action}\n")

    def search_books_by_author(self, author):
        result = []
        for book in self.books:
            if book.author == author:
                result.append(book)
        self.logger(f"Search books author")
        return result

    def search_books_by_genre(self, genre):
        result = []
        for book in self.books:
            if book.genre == genre:
                result.append(book)
        self.logger('Search books by genre')
        return result

    def add_reader(self, reader):
        self.readers.append(reader)
        self.logger(f"Reader '{reader.name}' added to the library")

    def remove_reader(self, reader):
        self.readers.remove(reader)
        self.logger(f"Reader '{reader.name}' removed from the library")

    def edit_reader(self, reader, new_name=None, new_age=None, new_email=None):
        if new_name:
            reader.name = new_name
        if new_age:
            reader.age = new_age
        if new_email:
            reader.email = new_email
        self.logger(f"Reader '{reader.name}' edited in the library")


if __name__ == '__main__':
    library = Library()
    print("Welcome to the library!")
    while True:
        choice = input("\nPlease choose an option:\n"
                       "1. Add a book\n"
                       "2. Search for books by author\n"
                       "3. Add a reader\n"
                       "4. Save library data to file\n"
                       "5. Load library data from file\n"
                       "6. Exit\n: ")
        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            genre = input("Enter book genre: ")
            book = Book(title, author, genre)
            library.add_book(book)
            print("Book added successfully.")
        elif choice == "2":
            author = input("Enter author name: ")
            books = library.search_books_by_author(author)
            if books:
                print("Books by", author + ":")
                for book in books:
                    print(book.title)
            else:
                print("No books found by", author)
        elif choice == "3":
            name = input("Enter reader name: ")
            age = int(input("Enter reader age: "))
            email = input("Enter reader email: ")
            reader = Reader(name, age, email)
            library.add_reader(reader)
            print("Reader added successfully.")
        elif choice == "4":
            library.save_to_file()
            print("Library data saved to file.")

        elif choice == "5":
            library.load_from_file()
            print("Library data loaded from file.")

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
