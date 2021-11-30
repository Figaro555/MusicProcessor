from abc import ABC, abstractmethod


class AbstractDBManager(ABC):
    @abstractmethod
    def process_data(self):
        pass
