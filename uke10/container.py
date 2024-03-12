from abc import ABC, abstractmethod

class Container(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def add(self, element):
        pass

    @abstractmethod
    def contains(self, element):
        pass

    @abstractmethod
    def __str__(self):
        pass