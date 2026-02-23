from abc import ABC, abstractmethod


class Component(ABC):

    @abstractmethod
    def run(self, input_data):
        pass