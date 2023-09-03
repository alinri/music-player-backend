from abc import ABC, abstractmethod


class INotificaiton(ABC):
    @abstractmethod
    def send_message(self, content: str):
        raise NotImplementedError
