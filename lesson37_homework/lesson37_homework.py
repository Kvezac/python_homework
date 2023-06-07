class User:
    def __init__(self, name, email, role):
        if "@" not in email:
            raise ValueError("Invalid email address")
        self.name = name
        self.email = email
        self.role = role
        self.assigned_tasks = []

    def __str__(self) -> str:
        return f"Name: {self.name}\n" \
               f"Email: {self.email}\n" \
               f"Role: {self.role}\n" \
               f"Tasks: {[(task.name, task.status) for task in self.assigned_tasks] if self.assigned_tasks else '-'}"


class Admin(User):

    def create_task(self, task_name):
        if not isinstance(self, Admin):
            raise ValueError("Only Admin users can create tasks")
        task = Task(task_name)
        return task

    def assign_task(self, task, user):
        if not isinstance(self, Admin):
            raise ValueError("Only Admin users can assign tasks")
        if not isinstance(user, User):
            raise ValueError("Invalid  User")
        if task not in TaskManager.tasks:
            raise ValueError("Task does not exist")
        user.assigned_tasks.append(task)


class Task:
    def __init__(self, name):
        if not name:
            raise ValueError("Task name is empty")
        self.name = name
        self.status = "New"

    def change_status(self, status, user):
        if not isinstance(user, (Admin, User)):
            raise ValueError("Only Admin or User change status task")
        self.status = status

    def __str__(self):
        return f"Name: {self.name}\n" \
               f"Status: {self.status}"


class TaskManager:
    tasks = []
    users = []

    @classmethod
    def create_users(cls, name, email, role):
        user = User(name, email, role)
        cls.users.append(user)
        return user

    @classmethod
    def create_task(cls, name, user: User):
        task = user.create_task(name)
        cls.tasks.append(task)
        return task

    @classmethod
    def change_task_status(cls, task, status, user):
        if task not in user.assigned_tasks:
            return print("Такой задачи пользователю не назначалось")
        if task not in [t for user in cls.users for t in user.assigned_tasks]:
            raise ValueError("Task is not assigned to any user")
        task.change_status(status, user)

    @staticmethod
    def change_user_info(user, field, value):
        if field == 'name':
            user.name = value
        if field == 'email':
            user.email = value

    @staticmethod
    def tasks_info():
        return [print(task) for task in TaskManager.tasks]


if __name__ == '__main__':
    n = TaskManager
    admin_user = Admin("Andrey", "Andrey@gmail.com", "admin")
    regular_user = TaskManager.create_users("Vova", "Vova@example.com", "user")
    regular_user_1 = TaskManager.create_users("Sasha", "Sasha@example.com", "user")

    task_1 = TaskManager.create_task("Example 1", admin_user)
    admin_user.assign_task(TaskManager.create_task("Example 2", admin_user), regular_user)
    admin_user.assign_task(task_1, regular_user)
    TaskManager.change_task_status(task_1, 'Finish', regular_user_1)
    TaskManager.change_task_status(task_1, 'Finish', regular_user)
    [print(task.name) for task in n.tasks]
    print(n.users)
    print(regular_user)
    print(admin_user)
    n.change_user_info(regular_user_1, 'name', 'Alexandro')
    n.change_user_info(regular_user_1, 'email', 'Alexandro@gmail.com')
    print(regular_user_1)
    TaskManager.tasks_info()
