""" Создайте реализацию паттерна Builder. Протестируйте
    работу созданного класса
"""

from abc import ABC, abstractmethod


class Phone:
    def __init__(self):
        self.data: str = ""

    def about_phone(self) -> str:
        return self.data

    def append_data(self, string: str):
        self.data += string


class IDeveloperBuilder(ABC):

    @abstractmethod
    def create_display(self):
        pass

    @abstractmethod
    def create_box(self):
        pass

    @abstractmethod
    def system_install(self):
        pass

    @abstractmethod
    def get_phone(self) -> Phone:
        pass


class AndroidDeveloper(IDeveloperBuilder):

    def __init__(self):
        self.__phone = Phone()

    def create_display(self):
        self.__phone.append_data("Creat display: Samsung;\n")

    def create_box(self):
        self.__phone.append_data("Hull creat: Samsung;\n")

    def system_install(self):
        self.__phone.append_data("System installed: Android;\n")

    def get_phone(self) -> Phone:
        return self.__phone


class IphoneDeveloper(IDeveloperBuilder):

    def __init__(self):
        self.__phone = Phone()

    def create_display(self):
        self.__phone.append_data("Create display: Iphone;\n")

    def create_box(self):
        self.__phone.append_data("Hull create: Iphone;\n")

    def system_install(self):
        self.__phone.append_data("System installed: Ios;\n")

    def get_phone(self) -> Phone:
        return self.__phone


class Director:
    def __init__(self, developer: IDeveloperBuilder):
        self.__developer = developer

    def set_developer(self, developer: IDeveloperBuilder):
        self.__developer = developer

    def mount_only_phone(self) -> Phone:
        self.__developer.create_box()
        self.__developer.create_display()
        return self.__developer.get_phone()

    def mount_full_phone(self) -> Phone:
        self.__developer.create_box()
        self.__developer.create_display()
        self.__developer.system_install()
        return self.__developer.get_phone()


if __name__ == '__main__':
    android_developer: IDeveloperBuilder = AndroidDeveloper()

    director = Director(android_developer)

    samsung: Phone = director.mount_full_phone()
    print(samsung.about_phone())

    iphone_developer: IDeveloperBuilder = IphoneDeveloper()
    director.set_developer(iphone_developer)

    iphone: Phone = director.mount_only_phone()
    print(iphone.about_phone())
