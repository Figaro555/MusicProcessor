from abc import ABC, abstractmethod


class AbstractTablesCreator(ABC):
    @abstractmethod
    def create_tables(self):
        pass
