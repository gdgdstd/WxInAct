import wx


class Frame(wx.Frame):
    def __init__(self):
        super().__init__(None, -1, "菜单演示")

        panel = wx.Panel(self)
        panel.SetBackgroundColour("white")

        sb = self.CreateStatusBar()
        tb = self.CreateToolBar()
        mb = self.CreateMenuBar()

        # tb.AddSimpleTool(-1, wx.Bitmap("wia_007.png"), "退出", "退出此程序")
        tb.AddTool(-1, "退出", wx.Bitmap("wia_007.png"), "退出此程序")
        tb.Realize()

    def CreateMenuBar(self):

        mb = wx.MenuBar()
        self.SetMenuBar(mb)

        file_menu = wx.Menu()
        mb.Append(file_menu, "[文件&F]")

        file_menu.Append(-1, "关于", "关于此程序")
        file_menu.AppendSeparator()
        mi = file_menu.Append(-1, "退出", "退出此程序")

        self.Bind(wx.EVT_MENU, self.OnMenuExit, id=mi.GetId())

        return mb

    def OnMenuExit(self, evt=None):
        self.Close()


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
