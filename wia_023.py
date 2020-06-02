import wx


class Frame(wx.Frame):
    def __init__(self):
        super().__init__(None, -1, "文本输入演示")

        panel = wx.Panel(self)

        label = wx.StaticText(panel, -1, "基本控件：")
        text = wx.TextCtrl(panel, -1, "这里已输入了一些东西。", size=(175, -1))
        text.SetInsertionPoint(0)

        pwd_label = wx.StaticText(panel, -1, "密码：")
        pwd_text = wx.TextCtrl(
            panel, -1, "password", size=(175, -1), style=wx.TE_PASSWORD
        )

        sizer = wx.FlexGridSizer(cols=2, hgap=6, vgap=6)
        sizer.AddMany((label, text, pwd_label, pwd_text))

        panel.SetSizer(sizer)


if __name__ == "__main__":
    app = wx.App()
    Frame().Show()
    app.MainLoop()
