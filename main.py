# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QMainWindow




if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = QMainWindow()
    window.setWindowTitle("Palette Visualizer")
    window.setGeometry(500,270      #Window position
                      ,960,540     #Window size
                      )

    window.show()


    sys.exit(app.exec())
