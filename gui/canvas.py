from PyQt5.QtWidgets import QSizePolicy
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class GraphicsCanvas(FigureCanvas):  # холст для помещения графика
    def __init__(self, fig, parent=None):
        self.fig = fig
        FigureCanvas.__init__(self, self.fig)  # в конструктор супер-класса помещаем график
        FigureCanvas.setSizePolicy(self, QSizePolicy.Maximum, QSizePolicy.Expanding)  # график будет на всю область
        FigureCanvas.updateGeometry(self)
        plt.style.use('dark_background')
        self.fig.patch.set_visible(False)  # прозрачность холста
        plt.grid(True)