import json

class ColorPalette:

    def __init__(self, name=''):
        self._name=name
        self._colors=[]

    def getName(self):
        return self._name
    
    def getColors(self):
        return self._colors

    def formatForPlot(self):
        plot_data = {"x":[], "y":[], "z":[], "colors":[]}
        for color in self._colors:
            plot_data["x"].append(color["rgb"][0])
            plot_data["y"].append(color["rgb"][1])
            plot_data["z"].append(color["rgb"][2])
            plot_data["colors"].append((
                                    (color["rgb"][0]/255),
                                    (color["rgb"][1]/255),
                                    (color["rgb"][2]/255)
            ))
        return plot_data
    #END OF def formatForPlot(self)

    @staticmethod
    def loadFromJson(file):
        palette = ColorPalette()

        with open(file, "r") as palette_file:

            raw_data = json.load(palette_file)
            
            palette._name    = raw_data["name"]
            palette._colors  = raw_data["colors"]

        return palette
