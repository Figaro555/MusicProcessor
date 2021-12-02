from abc import ABC, abstractmethod


class AbstractDataManager(ABC):
    @abstractmethod
    def process_data(self):
        pass
