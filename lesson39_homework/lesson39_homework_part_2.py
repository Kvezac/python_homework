from abc import ABC

"""Разработайте систему управления библиотекой Python, позволяющую добавлять новые типы книг без изменения
существующей кодовой базы. В системе должен быть базовый класс Book, определяющий общие свойства и методы для всех
типов книг. Подклассы, такие как FictionBook, NonFictionBook и ReferenceBook, должны наследоваться от класса Book и
предоставлять определенные реализации для соответствующих типов. Чтобы добавить новый тип книги, вы должны иметь
возможность создать новый подкласс книги и реализовать необходимые функции без изменения существующего кода.
Библиотечная система должна по-прежнему иметь возможность беспрепятственно обрабатывать новый тип книг. Придерживаясь
принципа открытости/закрытости, система управления библиотекой позволит легко расширять ее без необходимости
изменения основной кодовой базы, повышая удобство сопровождения и снижая риск появления ошибок."""


class Book(ABC):
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_year(self):
        return self.year


class FictionBook(Book):
    def __init__(self, title, author, year, genre):
        super().__init__(title, author, year)
        self.genre = genre

    def get_genre(self):
        return self.genre


class NonFictionBook(Book):
    def __init__(self, title, author, year, topic):
        super().__init__(title, author, year)
        self.topic = topic

    def get_topic(self):
        return self.topic


class ReferenceBook(Book):
    def __init__(self, title, author, year, category):
        super().__init__(title, author, year)
        self.topic = category

    @property
    def category(self):
        return self.category


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def search_book(self, book):
        for value in self.books:
            if value == book:
                return self.book

    def remove_book(self, book):
        self.books.remove(book)

    def __str__(self):
        result = ""
        for ind, book in enumerate(self.books, 1):
            result += f"{ind}. type: {book.__class__.__name__} {*[i for i in book.__dict__.values()],}\n"
        return result


if __name__ == '__main__':
    library = Library()

    fiction_book = FictionBook("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Novel")
    non_fiction_book = NonFictionBook("The Selfish Gene", "Richard Dawkins", 1976, "Evolutionary biology")
    reference_book = ReferenceBook("The Oxford English Dictionary", "Various", 1884, "Dictionary")

    library.add_book(fiction_book)
    library.add_book(non_fiction_book)
    library.add_book(reference_book)
    print(library)

