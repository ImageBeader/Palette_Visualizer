# This Python file uses the following encoding: utf-8

from PySide6.QtWidgets import QMainWindow, QLabel, QWidget, QHBoxLayout

class MainPVWindow(QMainWindow):
    def __init__(self):
        super(MainPVWindow, self).__init__()

        self.setWindowTitle("Palette Visualizer")
        self.setGeometry(500,270     #Window position
                        ,960,540     #Window size
                        )

        self.setupUi()

    def setupUi(self):
        root = QWidget(self)
        root.setGeometry(0,0
                        ,self.width(),self.height()
                        )
        root.setLayout(QHBoxLayout())

        label = QLabel("Pallete Visualizer Controls go here")
        label.setGeometry(110,50
                         ,200,100
                         )
        root.layout().addWidget(label)

        label2 = QLabel("The plot chart goes here")
        label2.setGeometry(110,50
                         ,200,100
                         )
        root.layout().addWidget(label2)
