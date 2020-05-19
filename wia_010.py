import wx


class App(wx.App):
    def OnInit(self):

        dlg = wx.SingleChoiceDialog(
            None, "请选择Pyhton版本", "提示", "1.2 1.5 2.0 3.0 3.8".split()
        )
        ret = ""
        if dlg.ShowModal() == wx.ID_OK:
            ret = dlg.GetStringSelection()

        dlg.Destroy()

        wx.MessageBox(f"{ret}", "选择")

        return True


app = App()
app.MainLoop()
