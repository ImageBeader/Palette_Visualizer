# This Python file uses the following encoding: utf-8

from PySide6.QtWidgets import QMainWindow, QWidget, QHBoxLayout,QVBoxLayout, QGroupBox, QLineEdit, QPushButton, QSpinBox

import matplotlib
matplotlib.use("QTAgg")

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg

class MainPVWindow(QMainWindow):
    def __init__(self):
        super(MainPVWindow, self).__init__()

        self.setWindowTitle("Palette Visualizer")
        self.setGeometry(500,270     #Window position
                        ,1280,720     #Window size
                        )

        self.setupUi()

    def setupUi(self):
        #Root widget

        root = QWidget(self)
        root.setGeometry(0,0
                        ,self.width(),self.height()
                        )
        root.setLayout(QHBoxLayout())

        #tool area

        tool_box = QWidget()
        tool_box.setLayout(QVBoxLayout())
        root.layout().addWidget(tool_box)

        #palette load

        file_load_group= QGroupBox("Pallete File")
        file_load_group.setLayout(QVBoxLayout())
        tool_box.layout().addWidget(file_load_group)

        file_box = QLineEdit("Pallete Visualizer Controls go here")
        file_box.setGeometry(110,25
                            ,200,100
                            )
        file_load_group.layout().addWidget(file_box)

        pallete_load_btn = QPushButton("load")
        file_load_group.layout().addWidget(pallete_load_btn)

        pallete_clear_btn = QPushButton("clear")
        file_load_group.layout().addWidget(pallete_clear_btn)

        #manual color check

        single_rgb_group = QGroupBox("Single point check")
        single_rgb_group.setLayout(QVBoxLayout())
        tool_box.layout().addWidget(single_rgb_group)

        rgb_line = QWidget()
        rgb_line.setLayout(QHBoxLayout())
        single_rgb_group.layout().addWidget(rgb_line)

        rgb_red = QSpinBox()
        rgb_line.layout().addWidget(rgb_red)

        rgb_green = QSpinBox()
        rgb_line.layout().addWidget(rgb_green)

        rgb_blue = QSpinBox()
        rgb_line.layout().addWidget(rgb_blue)

        rgb_control = QWidget()
        rgb_control.setLayout(QHBoxLayout())
        single_rgb_group.layout().addWidget(rgb_control)

        rgb_add = QPushButton("Add")
        rgb_control.layout().addWidget(rgb_add)

        rgb_clear = QPushButton("Clear")
        rgb_control.layout().addWidget(rgb_clear)

        #Plot area

        pScatterPlot = FigureCanvasQTAgg()
        root.layout().addWidget(pScatterPlot)
