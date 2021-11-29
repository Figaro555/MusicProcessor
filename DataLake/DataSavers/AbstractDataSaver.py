from abc import ABC, abstractmethod


class AbstractDataSaver(ABC):
    @abstractmethod
    def save(self):
        pass
