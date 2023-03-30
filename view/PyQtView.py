import sys
import qdarktheme
from .View import View
from .subview.PyQtField import PyQtField
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtGui
from PyQt5.QtWidgets import (
    QVBoxLayout,
    QWidget, 
    QMessageBox,
    QLabel,
    QLineEdit,
    QPushButton
    )

class MetaClass(type(View), type(QWidget)):
    pass

class PyQtView(View, QWidget, metaclass=MetaClass):
    def __init__(self):
        pass      

    def setup(self, controller):
        self.app = QApplication([])
        self.controller = controller
        qdarktheme.setup_theme("light")
        
    def start(self):
        QWidget.__init__(self)
        
        self._init_layout()
        self.controller.load_fields_to_layout()
        self._add_buttons_to_layout()
        
        self.setWindowTitle("QE12MB")
        self.show()

        sys.exit(self.app.exec_())

    def _init_layout(self):
        self.main_layout = QVBoxLayout()
        self.fields_layout = QVBoxLayout()
        self.main_layout.addLayout(self.fields_layout)
        self.setLayout(self.main_layout)

    def add_field_to_layout(self, field_name, label):
        field = PyQtField(field_name, label)
        self.fields_layout.addWidget(field)

    def get_fields(self):
        fields = []
        for i in range(self.fields_layout.count()):
            field = self.fields_layout.itemAt(i).widget()
            fields.append(field)
        return fields

    def clear_fields(self):
        for i in range(self.fields_layout.count()):
            field = self.fields_layout.itemAt(i).widget()
            field.input.clear()

    def _add_buttons_to_layout(self):
        save_button = QPushButton("Save")
        save_button.clicked.connect(self.controller.handle_click_save)
        self.main_layout.addWidget(save_button)

        exit_button = QPushButton("Exit")
        exit_button.clicked.connect(self.controller.handle_click_exit)
        self.main_layout.addWidget(exit_button)

    def show_dialog(self, message, type=None):
        msg = QMessageBox()

        if type == "error":
            msg.setIcon(QMessageBox.Critical)
        elif type == "info":
            msg.setIcon(QMessageBox.Information)
        elif type == "warning":
            msg.setIcon(QMessageBox.Warning)

        msg.setText(message)
        msg.setWindowTitle("QE12MB")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()
