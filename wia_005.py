import wx


class Frame(wx.Frame):
    def __init__(self, image):

        self.bmp = wx.Bitmap(image)
        w, h = self.bmp.GetWidth(), self.bmp.GetHeight()

        super().__init__(None, -1, "显示 Hello, wxPython", size=(w, h))

        self.bmpCtrl = wx.StaticBitmap(self, bitmap=self.bmp)


class App(wx.App):
    def OnInit(self):
        self.frame = Frame("wia_005.png")
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True


if __name__ == "__main__":
    app = App()
    app.MainLoop()
