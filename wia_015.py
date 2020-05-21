import wx


class Frame(wx.Frame):
    def __init__(self):
        super().__init__(None, wx.ID_ANY, "重构应用程序")

        panel = wx.Panel(self, wx.ID_ANY)
        panel.SetBackgroundColour("white")

        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)

        self._CreateMenuBar()
        self._CreateButtonBar(panel)
        self._CreateTextFields(panel)

    def _menu_data(self):
        return (
            (
                "文件(&F)",
                ("打开(&O)\tCtrl+O", "打开文件", self.OnFileOpen),
                ("", "", ""),
                ("退出(&X)", "退出程序", self.OnClose),
            ),
            (
                "编辑(&E)",
                ("复制(&C)\tCtrl+C", "复制", self.OnEditCopy),
                ("剪切(&X)\tCtrl+X", "剪切", self.OnEditCut),
                ("粘贴(&P)\tCtrl+V", "粘贴", self.OnEditPaste),
            ),
            ("配置(&P)", ("选项", "配置选项", self.OnConfig),),
            ("帮助(&H)", ("关于", "关于此程序", self.OnHelpAbout),),
        )

    def _CreateMenuBar(self):

        mb = wx.MenuBar()
        for menu in self._menu_data():
            label = menu[0]
            items = menu[1:]
            mb.Append(self._CreateMenuItems(items), label)

        self.SetMenuBar(mb)

    def _CreateMenuItems(self, items):
        menu = wx.Menu()
        for label, status, handler in items:
            if not label:
                menu.AppendSeparator()
                continue

            mi = menu.Append(wx.ID_ANY, label, status)
            self.Bind(wx.EVT_MENU, handler, mi)
        return menu

    def _button_data(self):
        return (
            ("首个", self.OnFirst),
            ("前一个", self.OnPrev),
            ("后一个", self.OnNext),
            ("末尾", self.OnLast),
        )

    def _CreateButtonBar(self, parent, ypos=0):
        xpos = 0
        for (label, handler) in self._button_data():
            pos = (xpos, ypos)
            button = self._BuildOneButton(parent, label, handler, pos)
            xpos += button.GetSize().width

    def _BuildOneButton(self, parent, label, handler, pos=(0, 0)):
        button = wx.Button(parent, wx.ID_ANY, label, pos=pos)
        self.Bind(wx.EVT_BUTTON, handler, button)
        return button

    def _text_fields_data(self):

        return (
            ("  姓  ", (10, 50)),
            ("  名  ", (10, 80)),
        )

    def _CreateTextFields(self, parent):
        for (label, pos) in self._text_fields_data():
            self._CreateCaptionTextField(parent, label, pos)

    def _CreateCaptionTextField(self, parent, label, pos):
        static = wx.StaticText(parent, wx.ID_ANY, label, pos)
        static.SetBackgroundColour("#0x888888")
        static.SetForegroundColour("white")

        text_field_pos = (pos[0] + 35, pos[1] - 5)
        wx.TextCtrl(parent, wx.ID_ANY, "", pos=text_field_pos)

    def OnCloseWindow(self, evt):
        self.Destroy()

    def OnClose(self, evt):
        self.Close()

    def OnFileOpen(self, evt):
        pass

    def OnEditCopy(self, evt):
        pass

    def OnEditCut(self, evt):
        pass

    def OnEditPaste(self, evt):
        pass

    def OnConfig(self, evt):
        pass

    def OnHelpAbout(self, evt):
        pass

    def OnFirst(self, evt):
        pass

    def OnPrev(self, evt):
        pass

    def OnNext(self, evt):
        pass

    def OnLast(self, evt):
        pass

    def OnFileOpen(self, evt):
        pass

    def OnFileOpen(self, evt):
        pass

    def OnFileOpen(self, evt):
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
