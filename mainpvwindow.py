# This Python file uses the following encoding: utf-8

from PySide6.QtWidgets import QMainWindow, QWidget, QHBoxLayout,QVBoxLayout, QGroupBox, QLineEdit, QPushButton, QSpinBox, QFileDialog, QColorDialog 
from PySide6.QtGui import QColor

import matplotlib
matplotlib.use("QTAgg")

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure

from colorpalette import ColorPalette

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
        self.plot_ax.set_xlim(255, 0)
        self.plot_ax.set_ylabel("Green")
        self.plot_ax.set_ylim(0, 255)
        self.plot_ax.set_zlabel("Blue")
        self.plot_ax.set_zlim(0, 255)

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

        self.file_box = QLineEdit("*No palette file loaded*")
        self.file_box.setReadOnly(True)
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

        self.rgb_red = QSpinBox()
        self.rgb_red.setRange(0,255)
        rgb_line.layout().addWidget(self.rgb_red)

        self.rgb_green = QSpinBox()
        self.rgb_green.setRange(0,255)
        rgb_line.layout().addWidget(self.rgb_green)

        self.rgb_blue = QSpinBox()
        self.rgb_blue.setRange(0,255)
        rgb_line.layout().addWidget(self.rgb_blue)

        rgb_picker = QPushButton("picker")
        rgb_picker.clicked.connect(self.rgbPick)
        rgb_line.layout().addWidget(rgb_picker)

        rgb_control = QWidget()
        rgb_control.setLayout(QHBoxLayout())
        single_rgb_group.layout().addWidget(rgb_control)

        rgb_add = QPushButton("Add")
        rgb_add.clicked.connect(self.addRgbPoint)
        rgb_control.layout().addWidget(rgb_add)

        rgb_clear = QPushButton("Clear")
        rgb_clear.clicked.connect(self.clearRgbPoint)
        rgb_control.layout().addWidget(rgb_clear)

        #Plot area

        pScatterPlot = FigureCanvasQTAgg(self.plot_figure)

        root.layout().addWidget(pScatterPlot)
    #END OF def setupUI(self)

    def loadPalette(self):
        file_choice = QFileDialog.getOpenFileName(self, "Open Palette", "~","palette file (*.json);;All Files (*)")

        filename = str(file_choice[0])

        if filename:

            color_palette = ColorPalette.loadFromJson(filename)

            self.plot_ax.set_title(color_palette.getName())

            plot_data = color_palette.formatForPlot()

            if "palette" in self.plot_dataset.keys() and self.plot_dataset["palette"] is not None:
                self.plot_dataset["palette"].remove()
            
            self.plot_dataset["palette"] = self.plot_ax.scatter(xs=plot_data["x"], ys=plot_data["y"], zs=plot_data["z"], c=plot_data["colors"], marker="o")

            self.file_box.setText(filename)


        self.plot_figure.canvas.draw()
    #END OF def loadPalette(self)

    def clearPalette(self):
        self.file_box.setText("*No palette file loaded*")
        self.plot_ax.set_title("")

        if "palette" in self.plot_dataset.keys() and self.plot_dataset["palette"] is not None:
            self.plot_dataset["palette"].remove()
            self.plot_dataset["palette"] = None
            self.plot_figure.canvas.draw()
    # END OF def clearPalette(self)
        
    def rgbPick(self):
        picked_color = QColorDialog.getColor(initial=QColor.fromRgb(self.rgb_red.value(),self.rgb_green.value(),self.rgb_blue.value()))

        print(str(picked_color.isValid()))

        if picked_color.isValid():
            self.rgb_red.setValue(picked_color.red())
            self.rgb_green.setValue(picked_color.green())
            self.rgb_blue.setValue(picked_color.blue())
    #END OF def rgbPick(self)

    def addRgbPoint(self):
        #TODO: Calculate the nearest colors based on the pallete if loaded.

        if "single" in self.plot_dataset.keys() and self.plot_dataset["single"] is not None:
            self.plot_dataset["single"].remove()

        self.plot_dataset["single"] = self.plot_ax.scatter(self.rgb_red.value(),self.rgb_green.value(),self.rgb_blue.value(),marker = "^")
        self.plot_figure.canvas.draw()
    #END OF def addRgbPoint(self)

    def clearRgbPoint(self):
        if "single" in self.plot_dataset.keys() and self.plot_dataset["single"] is not None:
            self.plot_dataset["single"].remove()
            self.plot_dataset["single"]=None
            self.plot_figure.canvas.draw()
    #END OF def clearRgbPoint(self)

#END OF class MainPVWindow(QMainWindow)
