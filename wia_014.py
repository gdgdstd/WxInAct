import wx


class Frame(wx.Frame):
    def __init__(self):
        super().__init__(None, wx.ID_ANY, "重构应用程序")

        panel = wx.Panel(self, wx.ID_ANY)

        self.CreateButtonBar(panel)

    def CreateButtonBar(self, panel):
        self.BuildOneButton(panel, "第一个", self.OnFirst)
        self.BuildOneButton(panel, "前一个", self.OnPrev, (80, 0))
        self.BuildOneButton(panel, "后一个", self.OnNext, (160, 0))
        self.BuildOneButton(panel, "最后一个", self.OnLast, (240, 0))

    def BuildOneButton(self, parent, label, handler, pos=(0, 0)):
        button = wx.Button(parent, wx.ID_ANY, label, pos)
        self.Bind(wx.EVT_BUTTON, handler, button)
        return button

    def OnFirst(self, evt):
        pass

    def OnPrev(self, evt):
        pass

    def OnNext(self, evt):
        pass

    def OnLast(self, evt):
        pass


class App(wx.App):
    def OnInit(self):
        self.frame = Frame()
        self.frame.Show()
        self.SetTopWindow(self.frame)

        return True


def main():
    app = App()
    app.MainLoop()


if __name__ == "__main__":
    main()
