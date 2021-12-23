import os
from pathlib import Path

from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QDialog


class CustomDialog(QDialog):
    def __init__(self, parent):
        super(CustomDialog, self).__init__(parent)
        self.load_ui()

    def load_ui(self):
        loader = QUiLoader()
        path = os.fspath(Path(__file__).resolve().parent / "dialog.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        window = loader.load(ui_file, self)
        ui_file.close()
        window.show()
