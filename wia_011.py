import wx


class Frame(wx.Frame):
    def __init__(self):
        super().__init__(None, -1, "菜单事件")

        panel = wx.Panel(self)

        panel.SetBackgroundColour("white")

        mb = self.CreateMenuBar()
        sb = self.CreateStatusBar()

    def CreateMenuBar(self):

        mb = wx.MenuBar()
        self.SetMenuBar(mb)

        p = file_menu = wx.Menu()
        mb.Append(file_menu, "[文件&F]")

        mi = p.Append(-1, "关于[&A]", "关于此程序")
        self.Bind(wx.EVT_MENU, self.OnAbout, mi)
        p.AppendSeparator()
        mi = p.Append(-1, "退出[&X]", "退出程序")
        self.Bind(wx.EVT_MENU, self.OnClose, mi)

    def OnClose(self, evt):
        self.Close()

    def OnAbout(self, evt):

        dlg = wx.MessageDialog(self, "本程序由 chenxd 制作维护\n邮箱: gdgdstd@gmail.com\n", "关于")
        dlg.ShowModal()
        dlg.Destroy()


class App(wx.App):
    def OnInit(self):
        frame = Frame()
        frame.Show()
        self.SetTopWindow(frame)
        return True


def main():
    app = App()
    app.MainLoop()


if __name__ == "__main__":
    main()
