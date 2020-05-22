import random
import string
import wx
import wx.grid


def _gen_data():
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


def _gen_labels():
    return ("Last", "First")


class LineupTable(wx.grid.GridTableBase):

    data = _gen_data()
    labels = _gen_labels()

    def GetNumberRows(self):
        return len(self.data)

    def GetNumberCols(self):
        return len(self.data[0]) - 1

    def GetColLabelValue(self, col):
        return self.labels[col]

    def GetRowLabelValue(self, row):
        return self.data[row][0]

    def IsEmptyCell(self, cell):
        return False

    def GetValue(self, row, col):
        return self.data[row][col + 1]

    def SetValue(self, row, col, value):
        pass


class SimpleGrid(wx.grid.Grid):
    def __init__(self, parent):
        super().__init__(parent, -1)

        self.SetTable(LineupTable())


class Frame(wx.Frame):
    def __init__(self):
        super().__init__(None, -1, "表格", size=(275, 275))

        panel = wx.Panel(self, -1)
        self.grid = SimpleGrid(panel)


if __name__ == "__main__":
    app = wx.App(False)
    Frame().Show(True)
    app.MainLoop()
