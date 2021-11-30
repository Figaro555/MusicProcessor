from abc import ABC, abstractmethod


class AbstractInitializer(ABC):
    @abstractmethod
    def create_tables(self):
        pass
