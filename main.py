# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QMainWindow,QLabel

class MainPVWindow(QMainWindow):
    def __init__(self):
        super(MainPVWindow, self).__init__()

        self.setWindowTitle("Palette Visualizer")
        self.setGeometry(500,270     #Window position
                        ,960,540     #Window size
                        )

        label = QLabel("Pallete Visualizer",self)
        label.setGeometry(110,50
                         ,200,100
                         )

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainPVWindow()
    window.show()

    sys.exit(app.exec())
