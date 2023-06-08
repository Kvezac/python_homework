from abc import ABC


# 1


# 2


# 3


class RemoteControl:
    def __init__(self):
        self.commands = [None] * 10
        self.history = []
        self.redo_history = []

    def set_command(self, button, command):
        self.commands[button] = command

    def press_button(self, button):
        if self.commands[button]:
            self.commands[button].execute()
            self.history.append(self.commands[button])

    def undo(self):
        if self.history:
            command = self.history.pop()
            command.undo()
            self.redo_history.append(command)

    def redo(self):
        if self.redo_history:
            command = self.redo_history.pop()
            command.execute()
            self.history.append(command)


class Command(ABC):
    def __init__(self, device):
        self.device = device

    def execute(self):
        raise NotImplementedError()

    def undo(self):
        raise NotImplementedError()


class PowerOnCommand(Command):
    def __init__(self, device):
        super().__init__(device)

    def execute(self):
        self.device.power_on()

    def undo(self):
        self.device.power_off()


class PowerOffCommand(Command):
    def __init__(self, device):
        super().__init__(device)

    def execute(self):
        self.device.power_off()

    def undo(self):
        self.device.power_on()


class VolumeUpCommand(Command):
    def __init__(self, device):
        super().__init__(device)

    def execute(self):
        self.device.volume_up()

    def undo(self):
        self.device.volume_down()


class VolumeDownCommand(Command):
    def __init__(self, device):
        super().__init__(device)

    def execute(self):
        self.device.volume_down()

    def undo(self):
        self.device.volume_up()


class Device:
    def power_on(self):
        print("Device is on")

    def power_off(self):
        print("Device is off")

    def volume_up(self):
        print("Volume up")

    def volume_down(self):
        print("Volume down")


class TV(Device):
    def __init__(self):
        self.volume = 0

    def power_on(self):
        print("TV is on")

    def power_off(self):
        print("TV is off")

    def volume_up(self):
        self.volume += 1
        print(f"TV volume is {self.volume}")

    def volume_down(self):
        self.volume -= 1
        print(f"TV volume is {self.volume}")


class DVD(Device):
    def __init__(self):
        self.volume = 0

    def power_on(self):
        print("DVD is on")

    def power_off(self):
        print("DVD is off")

    def volume_up(self):
        self.volume += 1
        print(f"DVD volume is {self.volume}")

    def volume_down(self):
        self.volume -= 1
        print(f"DVD volume is {self.volume}")


if __name__ == '__main__':
    # 3
    tv = TV()
    remote_control = RemoteControl()

    power_on_tv = PowerOnCommand(tv)
    power_off_tv = PowerOffCommand(tv)
    volume_up_tv = VolumeUpCommand(tv)
    volume_down_tv = VolumeDownCommand(tv)
    remote_control.set_command(0, power_on_tv)
    remote_control.set_command(1, power_off_tv)
    remote_control.set_command(2, volume_up_tv)
    remote_control.set_command(3, volume_down_tv)

    remote_control.press_button(0)  # TV is on
    remote_control.press_button(2)  # TV volume is 1
    remote_control.press_button(2)  # TV volume is 2
    remote_control.press_button(3)  # TV volume is 1

    remote_control.undo()  # TV volume is 2
    remote_control.redo()  # TV volume is 1

    dvd = DVD()
    remote_control_dvd = RemoteControl()

    power_on_dvd = PowerOnCommand(dvd)
    power_off_dvd = PowerOffCommand(dvd)
    volume_up_dvd = VolumeUpCommand(dvd)
    volume_down_dvd = VolumeDownCommand(dvd)

    remote_control_dvd.set_command(0, power_on_dvd)
    remote_control_dvd.set_command(1, power_off_dvd)
    remote_control_dvd.set_command(2, volume_up_dvd)
    remote_control_dvd.set_command(3, volume_down_dvd)

    remote_control_dvd.press_button(0)
    remote_control_dvd.press_button(2)
    remote_control_dvd.press_button(2)
    remote_control_dvd.press_button(2)
    remote_control_dvd.press_button(3)

    remote_control_dvd.undo()
    remote_control_dvd.redo()
    remote_control_dvd.press_button(1)
    remote_control.press_button(1)
