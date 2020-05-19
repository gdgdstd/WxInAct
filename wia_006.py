import wx


class Frame(wx.Frame):
    def __init__(self):
        super().__init__(None, -1, "按钮")

        panel = wx.Panel(self)

        button = wx.Button(panel, -1, label="关闭", pos=(125, 20), size=(50, 30))

        self.Bind(wx.EVT_BUTTON, self.OnCloseMe, button)

        self.Bind(wx.EVT_CLOSE, self.OnClose)

    def OnCloseMe(self, evt):
        self.Close()

    def OnClose(self, evt):
        self.Destroy()


class App(wx.App):
    def OnInit(self):
        Frame().Show()

        return True


if __name__ == "__main__":
    app = App()
    app.MainLoop()
