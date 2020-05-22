"""This is a gird"""
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


class LineupTable(wx.grid.GridTableBase):
    """LineupTable"""

    m_data = m_gen_data()
    m_labels = m_gen_labels()

    # data = m_data

    def GetNumberRows(self):
        """1"""
        return len(self.m_data)

    def GetNumberCols(self):
        """1"""
        return len(self.m_data[0]) - 1

    def GetColLabelValue(self, col):
        """1"""
        return self.m_labels[col]

    def GetRowLabelValue(self, row):
        """1"""

        return self.m_data[row][0]

    def IsEmptyCell(self, row, col):
        """1"""
        return False

    def GetValue(self, row, col):
        """1"""
        return self.m_data[row][col + 1]

    def SetValue(self, row, col, value):
        """1"""


class SimpleGrid(wx.grid.Grid):
    """A Simple Grid"""

    def __init__(self, parent):
        super().__init__(parent, -1)

        self.SetTable(LineupTable(), True)
        print("ok")


class Frame(wx.Frame):
    """ A Frame"""

    def __init__(self):
        super().__init__(None, -1, "表格", size=(600, 400))

        grid = SimpleGrid(self)


if __name__ == "__main__":
    app = wx.App(False)
    Frame().Show(True)
    app.MainLoop()
