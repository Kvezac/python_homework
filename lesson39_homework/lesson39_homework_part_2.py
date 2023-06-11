"""Разработайте систему управления библиотекой Python, позволяющую добавлять новые типы книг без изменения
существующей кодовой базы. В системе должен быть базовый класс Book, определяющий общие свойства и методы для всех
типов книг. Подклассы, такие как FictionBook, NonFictionBook и ReferenceBook, должны наследоваться от класса Book и
предоставлять определенные реализации для соответствующих типов. Чтобы добавить новый тип книги, вы должны иметь
возможность создать новый подкласс книги и реализовать необходимые функции без изменения существующего кода.
Библиотечная система должна по-прежнему иметь возможность беспрепятственно обрабатывать новый тип книг. Придерживаясь
принципа открытости/закрытости, система управления библиотекой позволит легко расширять ее без необходимости
изменения основной кодовой базы, повышая удобство сопровождения и снижая риск появления ошибок."""