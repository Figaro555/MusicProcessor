from abc import ABC, abstractmethod


class AbstractConnector(ABC):
    @abstractmethod
    def get_connection(self):
        pass
