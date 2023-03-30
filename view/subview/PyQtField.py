from PyQt5.QtWidgets import (
    QHBoxLayout,
    QWidget, 
    QLabel,
    QLineEdit
    )
from .Field import Field

class MetaClass(type(Field), type(QWidget)):
    pass

class PyQtField(Field, QWidget, metaclass=MetaClass):
    def __init__(self, field_name, label):
        super().__init__()
        self.field_name = field_name
        self.label = label
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        self._add_widgets()


    def _add_widgets(self):
        label_ = QLabel(self.label)
        self.layout.addWidget(label_)
        
        input_ = QLineEdit()
        self.input = input_
        self.layout.addWidget(input_)

    def get_input_text(self):
        return self.input.text()
