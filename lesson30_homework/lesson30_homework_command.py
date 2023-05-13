from abc import ABC, abstractmethod


class Command(ABC):
    """ Реализацию паттерна Command.
    Протестируйте работу созданного класса.
    """

    @abstractmethod
    def execute(self):
        pass


class LightOnCommand(Command):
    def __init__(self, light: object):
        self.light = light

    def execute(self):
        self.light.turn_on()


class LightOffCommand(Command):
    def __init__(self, light: object):
        self.light = light

    def execute(self):
        self.light.turn_off()


class Light:
    def turn_on(self):
        print("Light is on")

    def turn_off(self):
        print("Light is off")


class RemoteControl:
    def __init__(self):
        self.commands: dict = {}

    def set_commands(self, slot: int, command: object):
        self.commands[slot] = command

    def press_button(self, slot: int):
        if slot in self.commands:
            self.commands[slot].execute()


if __name__ == '__main__':
    light = Light()
    light_on_command = LightOnCommand(light)
    light_off_command = LightOffCommand(light)
    remote_control = RemoteControl()
    remote_control.set_commands(0, light_on_command)
    remote_control.set_commands(1, light_off_command)
    remote_control.press_button(0)
    remote_control.press_button(1)
