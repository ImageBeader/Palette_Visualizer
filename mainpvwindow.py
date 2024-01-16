# This Python file uses the following encoding: utf-8

from PySide6.QtWidgets import QMainWindow, QWidget, QHBoxLayout,QVBoxLayout, QGroupBox, QLineEdit, QPushButton, QSpinBox

import matplotlib
matplotlib.use("QTAgg")

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure

class MainPVWindow(QMainWindow):

    def __init__(self):
        super(MainPVWindow, self).__init__()

        self.setWindowTitle("Palette Visualizer")
        self.setGeometry(500,270     #Window position
                        ,1280,720     #Window size
                        )

        self.plot_dataset = {}
        self.initializeScatterPlot()

        self.setupUi()
    #END OF def __init__(self)

    def initializeScatterPlot(self):
        self.plot_figure = Figure()
        self.plot_ax = self.plot_figure.add_subplot(projection='3d')

        self.plot_ax.set_xlabel("Red")
        self.plot_ax.set_ylabel("Green")
        self.plot_ax.set_zlabel("Blue")

        self.plot_dataset["single"] = self.plot_ax.scatter(xs=128,ys=128,zs=96, marker='^')

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

        self.file_box = QLineEdit("Pallete Visualizer Controls go here")
        self.file_box.setGeometry(110,25
                            ,200,100
                            )
        file_load_group.layout().addWidget(self.file_box)

        pallete_load_btn = QPushButton("load")
        pallete_load_btn.clicked.connect(self.loadPalette)
        file_load_group.layout().addWidget(pallete_load_btn)

        pallete_clear_btn = QPushButton("clear")
        pallete_clear_btn.clicked.connect(self.clearPalette)
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

        pScatterPlot = FigureCanvasQTAgg(self.plot_figure)

        root.layout().addWidget(pScatterPlot)
    #END OF def setupUI(self)

    def loadPalette(self):
        self.file_box.setText("Loaded palette")

    def clearPalette(self):
        self.file_box.setText("")

        if "palette" in self.plot_dataset.keys() and self.plot_dataset["palette"] is not None:
            self.plot_dataset["palette"].remove()
            self.plot_dataset["palette"] = None

        self.plot_figure.canvas.draw()
