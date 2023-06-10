from abc import ABC, abstractmethod
import datetime



# 1

class SocialMediaAccount(ABC):
    def __init__(self, username):
        self.username = username

    @abstractmethod
    def post(self, content):
        pass


class FacebookAccount(SocialMediaAccount):
    def post(self, content):
        print(f"Posting on Facebook as {self.username}: {content}")


class InstagramAccount(SocialMediaAccount):
    def post(self, content):
        print(f"Posting on Instagram as {self.username}: {content}")


class TwitterAccount(SocialMediaAccount):
    def post(self, content):
        print(f"Posting on Twitter as {self.username}: {content}")


class SocialMediaAccountFactory:

    def create_account(self, platform, username):
        if platform == "Facebook":
            return FacebookAccount(username)
        elif platform == "Instagram":
            return InstagramAccount(username)
        elif platform == "Twitter":
            return TwitterAccount(username)


class ProxySocialMediaAccount(SocialMediaAccount):
    def __init__(self, account):
        self.account = account

    def post(self, content):
        if self.is_content_safe(content):
            self.account.post(content)
        else:
            print("Content is not safe for posting.")

    def is_content_safe(self, content):
        return True if content else False


# 2
class File:
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        try:
            with open(self.filename, 'r', encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            raise "File with this name does not exist"

    def write(self, content):
        with open(self.filename, 'w') as f:
            f.write(content)

    def append(self, content):
        with open(self.filename, 'a', encoding="utf-8") as f:
            f.write(content)

    def delete(self):
        import os
        os.remove(self.filename)


class FileProxy:
    def __init__(self, filename):
        self.file = File(filename)
        self.cache = None
        self.log = []

    def read(self):
        self.log.append('Read attempt')
        if self.cache is not None:
            return self.cache
        else:
            content = self.file.read()
            self.cache = content
            return content

    def write(self, content):
        self.log.append(f'{datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")}--> Write attempt')
        self.file.write(content)
        self.cache = None

    def append(self, content):
        self.log.append(f'{datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")}--> Append attempt')
        self.file.append(content)
        self.cache = None

    def delete(self):
        self.log.append(f'{datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")}--> Delete attempt')
        self.file.delete()
        self.cache = None

    def restrict_access(self):
        self.log.append(f'{datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")}--> Access restricted')

    def enable_caching(self):
        self.log.append(f'{datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")}-> Caching enabled')

    def disable_caching(self):
        self.log.append(f'{datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")}-> Caching disabled')

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
    # 1
    print(1)
    factory = SocialMediaAccountFactory()
    facebook_account = factory.create_account("Facebook", "Top_academy")
    instagram_account = factory.create_account("Instagram", "Not_academy")
    twitter_account = factory.create_account("Twitter", "mr_Grey")

    proxy_facebook_account = ProxySocialMediaAccount(facebook_account)
    proxy_instagram_account = ProxySocialMediaAccount(instagram_account)
    proxy_twitter_account = ProxySocialMediaAccount(twitter_account)

    proxy_facebook_account.post("Hello, Facebook!")
    proxy_instagram_account.post("Hello, Instagram!")
    proxy_twitter_account.post("Hello, Twitter!")
    proxy_twitter_account.post("")
    # 2
    print(2)
    n = FileProxy("test_2.txt")
    n.write("New")
    [print(log) for log in n.log]
    n.append("Bye")
    [print(log) for log in n.log]
    n.write("My line write!")
    [print(log) for log in n.log]
    # 3
    print(3)
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
