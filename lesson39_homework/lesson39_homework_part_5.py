import datetime
from abc import ABC, abstractmethod

""" Разработайте систему ведения журнала Python, которая поддерживает различные типы средств ведения журнала,
например ConsoleLogger, FileLogger и DatabaseLogger. Реализуйте принцип инверсии зависимостей, используя абстракции (
интерфейсы) для ведения журнала. Определите интерфейс с именем Logger, который включает такие методы, как log_info(),
log_warning() и log_error(). Каждый класс регистратора (ConsoleLogger, FileLogger, DatabaseLogger) должен реализовать
этот интерфейс и предоставить собственную реализацию методов ведения журнала. Модули высокого уровня в системе должны
зависеть от интерфейса регистратора, а не от конкретных реализаций регистратора. Это позволяет легко подключать или
заменять различные типы регистраторов, не влияя на функциональность модулей высокого уровня. Придерживаясь принципа
инверсии зависимостей, вы создаете гибкую и расширяемую систему ведения журналов, которая обеспечивает слабую
связанность и модульность вашей кодовой базы."""


class Logger(ABC):
    @abstractmethod
    def log_info(self, message):
        pass

    @abstractmethod
    def log_warning(self, message):
        pass

    @abstractmethod
    def log_error(self, message):
        pass


class ConsoleLogger(Logger):
    def log_info(self, message):
        print(f"[INFO] {message}")

    def log_warning(self, message):
        print(f"[WARNING] {message}")

    def log_error(self, message):
        print(f"[ERROR] {message}")


class FileLogger(Logger):
    def __init__(self, filename):
        self.filename = filename

    def log_info(self, message):
        self.write_to_file(f"[INFO] {message}")

    def log_warning(self, message):
        self.write_to_file(f"[WARNING] {message}")

    def log_error(self, message):
        self.write_to_file(f"[ERROR] {message}")

    def write_to_file(self, message):
        with open(self.filename, "a") as f:
            f.write(message + "\n")


class DatabaseLogger(Logger):
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def log_info(self, message):
        self.write_to_database("INFO", message)

    def log_warning(self, message):
        self.write_to_database("WARNING", message)

    def log_error(self, message):
        self.write_to_database("ERROR", message)

    def write_to_database(self, level, message):
        pass


class TimeNowStr():
    @staticmethod
    def time_now_str():
        return datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')


def do_something(logger):
    logger.log_info(f"{TimeNowStr.time_now_str()} Starting...")
    logger.log_warning(f"{TimeNowStr.time_now_str()} Something looks suspicious...")
    logger.log_error(f" {TimeNowStr.time_now_str()} Oops, something went wrong!")


if __name__ == '__main__':
    console_logger = ConsoleLogger()
    file_logger = FileLogger("logfile.txt")

    do_something(console_logger)
    do_something(file_logger)
