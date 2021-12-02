from abc import ABC, abstractmethod


class AbstractDataLoader(ABC):
    @abstractmethod
    def save(self):
        pass
