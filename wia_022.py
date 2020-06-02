import wx


class Frame(wx.Frame):
    def __init__(self):
        super().__init__(None, -1, "静态文本演示")

        panel = wx.Panel(self)

        wx.StaticText(panel, wx.ID_ANY, "这是静态文本演示程序", (100, 10))

        rev = wx.StaticText(panel, -1, "可以设置前景色和后景色的文本。", (100, 40))
        rev.SetForegroundColour("white")
        rev.SetBackgroundColour("black")

        center = wx.StaticText(
            panel, -1, "居中对齐的文本", (100, 70), (160, -1), wx.ALIGN_CENTER
        )
        center.SetForegroundColour("white")
        center.SetBackgroundColour("black")

        right = wx.StaticText(
            panel, -1, "右对齐的文本", (100, 100), (160, -1), wx.ALIGN_RIGHT
        )
        right.SetForegroundColour("white")
        right.SetBackgroundColour("black")
        text = wx.StaticText(panel, -1, "设置新的字体", (20, 130))
        font = wx.Font(18, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        text.SetFont(font)

        wx.StaticText(panel, -1, "第一行文本\n第二行文本\n第三行文本", (20, 170))
        wx.StaticText(
            panel, -1, "第一行文本\n第二行文本\n第三行文本", (220, 170), style=wx.ALIGN_RIGHT
        )


if __name__ == "__main__":
    app = wx.App()
    Frame().Show()
    app.MainLoop()
