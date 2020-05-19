import wx


class App(wx.App):
    def OnInit(self):

        dlg = wx.TextEntryDialog(None, "这是显示的消息", caption="提示")
        ret = ""
        if dlg.ShowModal() == wx.ID_OK:
            ret = dlg.GetValue()

        dlg.Destroy()

        wx.MessageBox(f"{ret}", caption="提示")

        return True


app = App()
app.MainLoop()
