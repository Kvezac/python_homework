from abc import ABC, abstractmethod

"""Разработайте программу Python для службы обмена сообщениями, которая включает два отдельных интерфейса:
TextMessaging и MultimediaMessaging. Интерфейс TextMessaging должен определять методы, специфичные для текстовых
сообщений, такие как send_text_message(), receive_text_message() и get_message_history(). Интерфейс
MultimediaMessaging должен включать методы, специфичные для мультимедийных сообщений, такие как
send_multimedia_message(), receive_multimedia_message() и view_media_gallery(). Классы, представляющие различные
службы обмена сообщениями, должны реализовывать соответствующие интерфейсы в зависимости от их возможностей.
Например, класс, реализующий TextMessaging, может обрабатывать текстовые сообщения, а класс, реализующий
MultimediaMessaging, может обрабатывать как текстовые, так и мультимедийные сообщения. Разделяя интерфейсы,
вы гарантируете, что классам нужно будет реализовать только соответствующие методы, предотвращая их принуждение к
предоставлению ненужной функциональности. Это способствует лучшей организации кода и снижает вероятность раздувания
классов или нарушения принципа единой ответственности."""


class TextMessaging(ABC):

    @abstractmethod
    def send_text_message(self, message, recipient):
        pass

    @abstractmethod
    def receive_text_message(self):
        pass

    @abstractmethod
    def get_message_history(self):
        pass


class MultimediaMessaging(ABC):

    @abstractmethod
    def send_multimedia_message(self, media, recipient):
        pass

    @abstractmethod
    def receive_multimedia_message(self):
        pass

    @abstractmethod
    def view_media_gallery(self):
        pass


class TextMessagingService(TextMessaging):

    def __init__(self):
        self.message_history = []

    def send_text_message(self, message, recipient):
        pass

    def receive_text_message(self):
        pass

    def get_message_history(self):
        return self.message_history


class MultimediaMessagingService(MultimediaMessaging, TextMessagingService):

    def __init__(self):
        super().__init__()
        self.media_gallery = []

    def send_multimedia_message(self, media, recipient):
        pass

    def receive_multimedia_message(self):
        pass

    def view_media_gallery(self):
        return self.media_gallery

