# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication

from mainpvwindow import MainPVWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainPVWindow()
    window.show()

    sys.exit(app.exec())
