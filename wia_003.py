import wx


class App(wx.App):
    def OnInit(self):
        wx.Frame(None, -1, "Bare").Show()
        return True


app = App()
app.MainLoop()
