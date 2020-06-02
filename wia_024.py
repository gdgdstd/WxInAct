import wx


class Frame(wx.Frame):
    def __init__(self):
        super().__init__(None, -1, "多行文本框演示")


if __name__ == "__main__":
    app = wx.App()
    Frame().Show()
    app.MainLoop()
