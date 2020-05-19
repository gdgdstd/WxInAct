import wx


class App(wx.App):
    def OnInit(self):

        dlg = wx.MessageDialog(None, "这是消息框显示的内容", "提示")
        dlg.ShowModal()
        dlg.Destroy()

        return True


app = App()
app.MainLoop()
