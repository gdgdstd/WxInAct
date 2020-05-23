import random
import string
import wx
import wx.grid


def m_gen_data():
    def to_format1():
        length = random.randrange(1, 3)
        text = "".join(random.sample(string.ascii_letters, length))
        text = text.upper()
        return text

    def to_format2():
        length = random.randrange(3, 5)
        text = "".join(random.sample(string.ascii_letters, length))
        text = text.capitalize()
        return text

    def to_format3():
        length = random.randrange(4, 11)
        text = "".join(random.sample(string.ascii_letters, length))
        text = text.capitalize()
        return text

    data = []
    for _ in range(10):

        text1 = to_format1()
        text2 = to_format2()
        text3 = to_format3()

        data.append((text1, text2, text3))
    return data


def m_gen_labels():
    return ("Last", "First")


class GenericTable(wx.grid.GridTableBase):
    def __init__(self, data, row_labels=None, col_labels=None):
        super().__init__()

        self.data = data
        self.row_labels = row_labels
        self.col_labels = col_labels

    def GetNumberRows(self):
        return len(self.data)

    def GetNumberCols(self):
        return len(self.data[0])

    def GetColLabelValue(self, col):
        if self.col_labels:
            return self.col_labels[col]

    def GetRowLabelValue(self, row):
        if self.row_labels:
            return self.row_labels[row]

    def IsEmptyCell(self, row, col):
        return False

    def GetValue(self, row, col):
        return self.data[row][col]

    def SetValue(self, row, col, value):
        pass


data = (
    "Bob Dernier".split(),
    "Ryne Sandberg".split(),
    "Keith Moreland".split(),
    "Ron Cey".split(),
)

col_labels = "Last First".split()
row_labels = "CF 2B LF 1B".split()


class SimpleGrid(wx.grid.Grid):
    def __init__(self, parent):
        super().__init__(parent, -1)

        table = GenericTable(data, row_labels, col_labels)

        self.SetTable(table, True)


class Frame(wx.Frame):
    def __init__(self):
        super().__init__(None, -1, "A Generic Grid", size=(600, 400))

        grid = SimpleGrid(self)


if __name__ == "__main__":
    app = wx.App(False)
    Frame().Show(True)
    app.MainLoop()
