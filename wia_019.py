import wx


class AbstractModel:
    def __init__(self):
        self.listeners = []

    def AddListener(self, listener_func):
        self.listeners.append(listener_func)

    def RemoveListener(self, listener_func):
        self.listeners.remove(listener_func)

    def Update(self):
        for func in self.listeners:
            func(self)


class SimpleName(AbstractModel):
    def __init__(self, first="", last=""):
        super().__init__()

        self.set(first, last)

    def set(self, first, last):
        self.first = first
        self.last = last

        self.Update()


class Frame(wx.Frame):
    def __init__(self):
        super().__init__(None, -1, "演示", size=(340, 200))

        panel = wx.Panel(self)
        panel.SetBackgroundColour("white")

        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)

        self.textFields = {}
        self.CreateTextFields(panel)

        self.model = SimpleName()
        self.model.AddListener(self.OnUpdate)

        self.CreateButtonBar(panel)

    def CreateButtonBar(self, parent, yPos=0):
        button_data = (
            ("Fred", self.OnFred),
            ("Wilm", self.OnWilm),
            ("Barc", self.OnBarc),
        )
        xPos = 0

        for label, func in button_data:
            pos = (xPos, yPos)
            button = self.BuildOneButton(parent, label, func, pos)
            xPos += button.GetSize().width

    def BuildOneButton(self, parent, label, handler, pos=(0, 0)):
        button = wx.Button(parent, -1, label, pos)
        self.Bind(wx.EVT_BUTTON, handler, button)
        return button

    def CreateTextFields(self, parent):
        text_field_data = (("First", (10, 50)), ("Last", (10, 80)))
        for label, pos in text_field_data:
            self.CreateCaptionText(parent, label, pos)

    def CreateCaptionText(self, parent, label, pos):
        static = wx.StaticText(parent, wx.ID_ANY, label, pos)
        static.SetBackgroundColour("white")
        textPos = (pos[0] + 75, pos[1])
        self.textFields[label] = wx.TextCtrl(
            parent, wx.ID_ANY, "", size=(100, -1), pos=textPos, style=wx.TE_READONLY
        )

    def OnUpdate(self, model):
        pass
        self.textFields["First"].SetValue(model.first)
        self.textFields["Last"].SetValue(model.last)

    def OnCloseWindow(self, evt):
        self.Destroy()

    def OnFred(self, evt):
        self.model.set("Fred", "Flinstones")

    def OnWilm(self, evt):
        pass

    def OnBarc(self, evt):
        pass


if __name__ == "__main__":
    app = wx.App()
    Frame().Show()
    app.MainLoop()
