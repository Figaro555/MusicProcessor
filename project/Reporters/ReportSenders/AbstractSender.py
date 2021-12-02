from abc import ABC, abstractmethod


class AbstractSender(ABC):
    @abstractmethod
    def send(self):
        pass