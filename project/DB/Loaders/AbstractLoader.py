from abc import ABC, abstractmethod


class AbstractLoader(ABC):
    def __init__(self, connector):
        self.connector = connector

    @abstractmethod
    def load(self, list_to_load):
        pass
