from PyQt5 import QtWidgets
from canvas import GraphicsCanvas
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar
from qt_material import apply_stylesheet


class label(QtWidgets.QLabel):
    def __init__(self, parent, geometry, text):
        super(label, self).__init__(parent)
        self.setText(text)
        self.setGeometry(geometry)


class combobox(QtWidgets.QComboBox):
    def __init__(self, parent, geometry, num_items):
        super(combobox, self).__init__(parent)
        for i in range(num_items):
            self.addItem("")
        self.setGeometry(geometry)


class table_view(QtWidgets.QTableView):
    def __init__(self, parent, geometry, model):
        super(table_view, self).__init__(parent)
        self.setModel(model)
        self.setGeometry(geometry)


class push_button(QtWidgets.QPushButton):
    def __init__(self, parent, geometry, text):
        super(push_button, self).__init__(parent)
        self.setText(text)
        self.setGeometry(geometry)
        self.setStyleSheet("""
                QPushButton{
                    font-size: 15px;
                    font-weight: bold;
                    border: 1px solid #5AF2FF;
                    border-radius: 4px;
                    color: #5AF2FF;
                }
                """)


class text_browser(QtWidgets.QTextBrowser):
    def __init__(self, parent, geometry):
        super(text_browser, self).__init__(parent)
        self.setGeometry(geometry)


class my_button_colorist(QtWidgets.QPushButton):
    def __init__(self, parent, geometry, window, theme, text):
        super(my_button_colorist, self).__init__(parent)
        self.setGeometry(geometry)
        self.clicked.connect(lambda: apply_stylesheet(window, theme))
        self.setText(text)


class message_box(QtWidgets.QMessageBox):
    def __init__(self, title, text, icon, parent=None):
        super(message_box, self).__init__()
        self.setWindowTitle(title)
        self.setText(text)
        self.setIcon(icon)
        self.exec_()


class my_table_view(QtWidgets.QTableView):
    def __init__(self, parent, geometry, model):
        super(my_table_view, self).__init__(parent)
        self.setGeometry(geometry)
        self.setModel(model)


class my_plot_widget(QtWidgets.QWidget):
    def __init__(self, parent, geometry, fig, main_window):
        super(my_plot_widget, self).__init__(parent)
        self.setGeometry(geometry)
        self.fig = fig
        self.layout = QtWidgets.QVBoxLayout(self)
        self.canvas = GraphicsCanvas(self.fig)
        self.layout.addWidget(self.canvas)
        self.toolbar = NavigationToolbar(self.canvas, main_window)
        self.layout.addWidget(self.toolbar)


class line_edit(QtWidgets.QLineEdit):
    def __init__(self, parent, geometry, placeholder_text):
        super(line_edit, self).__init__(parent)
        self.setGeometry(geometry)
        self.setPlaceholderText(placeholder_text)