from abc import ABC, abstractmethod

class Field(ABC):
    @abstractmethod
    def get_input_text(self):
        pass