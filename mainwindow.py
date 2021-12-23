# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.stack = []
        self.load_ui()

    def load_ui(self):
        loader = QUiLoader()
        path = os.fspath(Path(__file__).resolve().parent / "form.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        window = loader.load(ui_file, self)
        ui_file.close()

        self.window = window

        window.pushButton_0.clicked.connect(self.on_number_button_click)
        window.pushButton_1.clicked.connect(self.on_number_button_click)
        window.pushButton_2.clicked.connect(self.on_number_button_click)
        window.pushButton_3.clicked.connect(self.on_number_button_click)
        window.pushButton_4.clicked.connect(self.on_number_button_click)
        window.pushButton_5.clicked.connect(self.on_number_button_click)
        window.pushButton_6.clicked.connect(self.on_number_button_click)
        window.pushButton_7.clicked.connect(self.on_number_button_click)
        window.pushButton_8.clicked.connect(self.on_number_button_click)
        window.pushButton_9.clicked.connect(self.on_number_button_click)

        window.pushButton_Delete.clicked.connect(self.on_delete_button_click)
        window.pushButton_C.clicked.connect(self.on_clear_button_click)
        window.pushButton_minus.clicked.connect(self.on_minus_button_click)

        window.show()

    def on_number_button_click(self, state):
        text = self.window.lineEdit.text()
        self.window.lineEdit.setText(text + self.sender().text())

    def on_delete_button_click(self, state):
        text = self.window.lineEdit.text()
        self.window.lineEdit.setText(text[:-1])

    def on_clear_button_click(self, state):
        text = ""
        self.window.lineEdit.setText("")

    def on_minus_button_click(self, state):
        self.stack.append(
            self.window.lineEdit.text()
        )
        self.stack.append(
            "-"
        )
        self.window.lineEdit.setText("")
        print(self.stack)

if __name__ == "__main__":
    app = QApplication([])
    widget = MainWindow()
#    widget.show()
    sys.exit(app.exec_())
