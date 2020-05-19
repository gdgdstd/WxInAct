import wx


class Frame(wx.Frame):
    def __init__(self):
        super().__init__(None, -1, "扩展")


class App(wx.App):
    def OnInit(self):
        self.frame = Frame()
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True


if __name__ == "__main__":
    app = App()
    app.MainLoop()
