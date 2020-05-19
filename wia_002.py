import wx


class Frame(wx.Frame):
    def __init__(self):
        super().__init__(None, -1, "鼠标位置演示")

        panel = wx.Panel(self)
        panel.Bind(wx.EVT_MOTION, self.OnMove)
        wx.StaticText(panel, -1, "位置：", pos=(12, 10))
        self.posCtrl = wx.TextCtrl(panel, -1, "", pos=(50, 8))

    def OnMove(self, evt):
        pos = evt.GetPosition()
        self.posCtrl.SetValue(f"{pos.x}, {pos.y}")


class App(wx.App):
    def OnInit(self, redirect=False, filename=None):
        Frame().Show()
        return True


def main():
    app = App()
    app.MainLoop()


if __name__ == "__main__":
    main()
