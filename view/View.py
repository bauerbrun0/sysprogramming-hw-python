from abc import ABC, abstractmethod

class View(ABC):
    @abstractmethod
    def setup(self, controller):
        pass

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def show_dialog(self, message, type=None):
        pass

    @abstractmethod
    def add_field_to_layout(self, field_name, label):
        pass
    
    @abstractmethod
    def get_fields(self):
        pass

    @abstractmethod
    def clear_fields(self):
        pass

    @abstractmethod
    def show_dialog(self, message, type):
        pass