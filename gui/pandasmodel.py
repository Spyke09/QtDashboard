from PyQt5.QtCore import QAbstractTableModel, QVariant
from PyQt5 import QtCore


class PandasModel(QAbstractTableModel):  # модель библиотеки pandas
    def __init__(self, data, headers_row, headers_column, parent=None):
        QAbstractTableModel.__init__(self, parent)
        self.data = data
        self.headers_row = headers_row
        self.headers_column = headers_column

    def headerData(self, section, orientation, role):
        if role == QtCore.Qt.DisplayRole:  # Проверяем есть ли ячейка для отображения данных
            if orientation == QtCore.Qt.Horizontal:  # Если это загловки  столбцов
                return self.headers_column[section]  # То задаем соответствующее значение заголовков по индексу
            else:  # Иначе  это заголовки строк
                if not self.headers_row:
                    return section + 1
                return self.headers_row[section]  # То задаем соответствующее значение заголовков по индексу

    def rowCount(self, parent=None):
        return len(self.data.values)

    def columnCount(self, parent=None):
        return self.data.columns.size

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if index.isValid():
            if role == QtCore.Qt.DisplayRole:
                return QVariant(str(self.data.iloc[index.row()][index.column()]))
        return QVariant()