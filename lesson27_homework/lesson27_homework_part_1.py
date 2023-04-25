class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    """ Задание 1
        Пользователь вводит с клавиатуры набор чисел. Полученные числа необходимо сохранить в список (тип
        списка нужно выбрать в зависимости от поставленной ниже задачи). После чего нужно показать меню, в котором
        предложить пользователю набор пунктов:
         1. Добавить новое число в список (если такое число существует в списке, нужно вывести сообщение пользователю
            об этом, без добавления числа).
         2. Удалить все вхождения числа из списка (пользователь вводит с клавиатуры число для удаления)
         3. Показать содержимое списка (в зависимости от выбора пользователя список нужно показать с начала или с конца)
         4. Проверить есть ли значение в списке
         5. Заменить значение в списке (пользователь определяет заменить ли только первое вхождение или все вхождения)
        В зависимости от выбора пользователя выполняется действие, после чего меню отображается снова.
    """

    def __init__(self):
        self.head = None

    def add_number(self, number: object) -> object:

        new_node = Node(number)

        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = new_node
        new_node.prev = current_node

    def number_search(self, number):
        if self.head is None:
            return False
        current_node = self.head
        while current_node is not None:
            if current_node.value == number:
                return True
            current_node = current_node.next
        return False

    def append(self, number):
        if not self.number_search(number):
            self.add_number(number)
            return f'{number} added to the list'
        return f'{number} already in the array'

    def del_number(self, number_del):
        if self.head is None:
            return
        if self.head.value == number_del:
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            return

        current_node = self.head
        while current_node.next is not None:
            if current_node.next.value == number_del:
                if current_node.next.next is not None:
                    current_node.next = current_node.next.next
                    if current_node.next is not None:
                        current_node.next.prev = current_node
                else:
                    current_node.next = None
                    return
            current_node = current_node.next

    def reverse(self):
        tmp = None
        current_node = self.head
        while current_node:
            tmp = current_node.prev
            current_node.prev = current_node.next
            current_node.next = tmp
            current_node = current_node.prev
        if tmp:
            self.head = tmp.prev
        # return self.show()

    def replace(self, number, change_num, count):
        if self.head is None:
            return
        if self.head.value == number:
            self.head.value = change_num
            if isinstance(count, int):
                count -= 1
                if count == 0:
                    return
        current_node = self.head
        while current_node.next is not None:
            if current_node.next.value == number:
                current_node.next.value = change_num
                if isinstance(count, int):
                    count -= 1
                    if count == 0:
                        return
            current_node = current_node.next

    def show(self):
        if self.head is None:
            print('List is empty!')
            return

        current_node = self.head
        while current_node is not None:
            print(current_node.value, end=' ')
            current_node = current_node.next
        print()


class MenuDoublyLinkedList:

    def start(self):
        user_dll = DoublyLinkedList()
        list_number = [int(i) for i in input('Enter whole numbers separated by spaces: ').split()]
        for num in list_number:
            user_dll.add_number(num)
        while (user_inp := input('Select a menu item\n'
                                 '1 Add number to list\n'
                                 '2 Remove all occurrences in a list\n'
                                 '3 Display a list\n'
                                 '4 Expand list and show display\n'
                                 '5 Check if a value is in the list\n'
                                 '6 Replacing a number in a list\n'
                                 'q Exit\n: ')) != 'q':
            print("-" * 50)
            match user_inp:
                case '1':
                    print(user_dll.append(int(input("Enter an integer: "))))
                    print("*" * 50)
                case '2':
                    user_dll.del_number(int(input("Enter number to delete: ")))
                    print("*" * 50)
                case '3':
                    user_dll.show()
                    print("*" * 50)
                case '4':
                    user_dll.reverse()
                    user_dll.show()
                    print("*" * 50)
                case '5':
                    num_search = int(input("Enter a number to search: "))
                    log = user_dll.number_search(num_search)
                    print(f'{num_search} is on the list' if log else f'{num_search} not found')
                    print("*" * 50)
                case '6':
                    number_input = int(input('Enter a number to replace: '))
                    change_num = int(input('Enter what we change to: '))
                    try:
                        count = int(input("Enter the number of substitutions or None: "))

                    except ValueError:
                        count = None
                    user_dll.replace(number_input, change_num, count)
                    print("*" * 50)
                case _:
                    print("Another chance")
                    print("*" * 50)


class Stack:
    """ Задание 2
        Реализуйте класс стека для работы со строками (стек строк).
        Стек должен иметь фиксированный размер.
        Реализуйте набор операций для работы со стеком:
         ■ помещение строки в стек;
         ■ выталкивание строки из стека;
         ■ подсчет количества строк в стеке;
         ■ проверку пустой ли стек;
         ■ проверку полный ли стек;
         ■ очистку стека;
         ■ получение значения без выталкивания верхней строки из стека.
        При старте приложения нужно отобразить меню с
        помощью, которого пользователь может выбрать необходимую операцию

         ■ Измените стек из второго задания, таким образом, чтобы его размер был нефиксированным
    """

    def __init__(self, size=None):
        self.stack = []
        self.size = size

    def peek(self):
        return self.stack[-1]

    def clear_stack(self):
        self.stack.clear()

    def len_stack(self):
        return len(self.stack)

    def check_full(self):
        if self.size is not None:
            return self.size == self.len_stack()
        return False

    def is_empty(self):
        if self.len_stack() == 0:
            return 'Stack is empty!'
        return False

    def push(self, value):
        if not self.check_full():
            self.stack.append(value)
            return f'String add in stack'
        return f'Stack is full'

    def pop(self):
        return self.is_empty() or self.stack.pop()


class MenuStack:

    def start_stack(self):
        user_st = Stack()
        test_list = ['Add strings on th stck', 'Popping a string from th stack',
                     'Counting the number of rows on the stck', 'Counting the number of rows on the stack'
                     'Checking if the stack is empty', 'Checking if the stack is full', 'Stack cleanup']
        for i in test_list:
            user_st.push(i)
        while (user_inp := input('Select a menu item\n'
                                 '1 Add strings on the stack\n'
                                 '2 Popping a string from the stack\n'
                                 '3 Counting the number of rows on the stack\n'
                                 '4 Checking if the stack is empty\n'
                                 '5 Checking if the stack is full\n'
                                 '6 Stack cleanup\n'
                                 '7 See top value without deleting\n'
                                 '8 Set stack size\n'
                                 'q Exit\n: ')) != 'q':
            print("-" * 50)
            match user_inp:
                case '1':
                    print(user_st.push(input("Enter an string: ")))
                    print("*" * 50)
                case '2':
                    print(f'String "{user_st.pop()}" delete from the stack')
                    print("*" * 50)
                case '3':
                    print(f'On the stack {user_st.len_stack()} string')
                    print("*" * 50)
                case '4':
                    print('Stack is empty' if user_st.is_empty() else 'Stack not empty')
                    print("*" * 50)
                case '5':
                    print('Stack full' if user_st.check_full() else 'Stack not full')
                    print("*" * 50)
                case '6':
                    user_st.clear_stack()
                    print("*" * 50)
                case '7':
                    print(user_st.peek())
                    print("*" * 50)
                case '8':
                    size_number = int(input('Set stack size: '))
                    user_st.size = size_number
                case _:
                    print("Another chance")
                    print("*" * 50)


if __name__ == "__main__":
    while (user_log := input("Select the desired menu item:\n"  # Выберите нужный пункт меню
                             "1 Task work with a list of numbers\n"  # задание работа со списком чисел
                             "2 Stack class for working with strings\n"  # Класс стека для работы со строками
                             "0 Exit\n: ")) != '0':
        match user_log:
            case '1':
                user = MenuDoublyLinkedList()
                user.start()
            case '2':
                user_stack = MenuStack()
                user_stack.start_stack()
            case _:
                print("Choose from an existing menu")

print("Program completed")


