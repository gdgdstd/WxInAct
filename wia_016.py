import random
import string
import wx
import wx.grid


class SimpleGrid(wx.grid.Grid):
    def __init__(self, parent):
        super().__init__(parent, -1)

        self.CreateGrid(10, 2)
        self.SetColLabelValue(0, "第一列")
        self.SetColLabelValue(1, "第二列")

        for x in range(10):
            for y in range(2):
                string.ascii_letters
                text = "".join(random.sample(string.ascii_letters, 6))
                text = text.capitalize()
                self.SetCellValue(x, y, text)


class Frame(wx.Frame):
    def __init__(self):
        super().__init__(None, -1, "一个简单的表格", size=(275, 275))

        grid = SimpleGrid(self)


if __name__ == "__main__":
    app = wx.App(False)
    Frame().Show()
    app.MainLoop()
