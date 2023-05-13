

class Librarian:
    """ Создайте приложение для работы в библиотеке. Оно
        должно оперировать следующими сущностями: Книга,
        Библиотекарь, Читатель. Приложение должно позволять
        вводить, удалять, изменять, сохранять в файл, загружать из
        файла, логировать действия, искать информацию (результаты поиска
        выводятся на экран или файл) о сущностях. При реализации
        используйте максимально возможное количество паттернов проектирования.
    """

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.logger = Logger('library_log.txt')

    def add_book(self, book, library):
        # library.books[book.title] = {'author': book.author}
        library.books.append(book)
        message = f"{self.name} added book '{book.title}' to {library.name}\n"
        self.logger.log(message)

    def remove_book(self, book, library):
        library.books.remove(book)
        message = f"{self.name} removed book '{self.book.title}' from {self.library.name}\n"
        self.logger.log(message)

    # def search_by_author(self, author, library):
    #     result = []
    #     for title, book in self.books.items():
    #         if book['author'] == author:
    #             result.append(title)
    #     return result
    #
    # def search_by_title(self, title):
    #     if title in self.books:
    #         return self.books[title]
    #     return


class FileStrategy:
    def file_in(self, library, message):
        file_name = library.name.lower().replace(' ', '_') + '.txt'
        with open(file_name, 'w') as f:
            f.write(message)

    def file_out(self, file_name):
        with open(file_name, 'r', encoding='UTF-8') as f:
            pass


class ConsoleStrategy:
    @staticmethod
    def __out__(obj, value=None):
        if value:
            print(value)
        else:
            print(*obj.arr)


class Strategy:
    pass


class Logger:
    def __init__(self, file_name):
        self.file_name = file_name

    def log(self, message):
        with open(self.file_name, 'a', encoding='UTF-8') as f:
            f.write(message)


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Reader:
    def __init__(self, name, age, books=[]):
        self.name = name
        self.age = age
        self.books = books
        self.logger = Logger('library_log.txt')

    def take_a_book(self, book, library):
        if book in library.books:
            library.books.remove(book)
            self.books.append(book)
            message = f"{self.name} take a book '{book.title}' from {library.name}\n"
            self.logger.log(message)
            return True
        return False

    def return_book(self, book, library):
        if book in self.books:
            self.books.remove(book)
            library.books.append(book)
            message = f"{self.name} returned book '{book.title}' to {library.name}\n"
            self.logger.log(message)
            return True
        return False


class Library:

    def __init__(self, name, books=[]):
        self.name = name
        self.books = books
        self.logger = Logger('library_log.txt')


if __name__ == '__main__':
    library = Library('Central Library')
    book_1 = Book('1984', 'George Orwell')
    book_2 = Book('To Kill a Mockingbird', 'Harper Lee')
    book_3 = Book('The Call of Cthulhu', 'Howard Philips Lovecraft')
    librarian = Librarian('Andrey', 42)
    librarian.add_book(book_1, library)
    librarian.add_book(book_2, library)
    librarian.add_book(book_3, library)
    reader = Reader('Lehca', 30)
    reader.take_a_book(book_1, library)
    reader.return_book(book_1, library)

    # while (user_log := input("Choose a command to execute:\n"
    #                          "1 Add book library\n"
    #                          "2 Delete book library\n"
    #                          "3 Replace book library\n"
    #                          "4\n"
    #                          "5\n"
    #                          "6\n"
    #                          "7\n"
    #                          "0 Exit")) != '0':
    #     match user_log:
    #         case _:
    #             print("There is no command like this.")
    # print("Program finish.")
