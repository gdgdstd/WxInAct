import wx


class SketchWindow(wx.Window):
    def __init__(self, parent, id):
        super().__init__(parent, id)

        self.SetBackgroundColour("white")
        self.color = "black"
        self.thickness = 1
        self.pen = wx.Pen(self.color, self.thickness, wx.SOLID)

        self.lines = []
        self.cur_line = []
        self.pos = (0, 0)
        self.InitBuffer()

        self.Bind(wx.EVT_LEFT_DOWN, self.OnLeftDown)
        self.Bind(wx.EVT_LEFT_UP, self.OnLeftUp)
        self.Bind(wx.EVT_MOTION, self.OnMove)
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Bind(wx.EVT_IDLE, self.OnIdle)
        self.Bind(wx.EVT_PAINT, self.OnPaint)

    def InitBuffer(self):
        size = self.GetClientSize()

        self.buffer = wx.EmptyBitmap(size.width, size.height)
        dc = wx.BufferDC(None, self.buffer)

        dc.SetBackgroundColour(wx.Brush(self.GetBackgroundColour()))

        dc.Clear()
        self.DrawLine(dc)

        self.reInitBuffer = False

    def GetLinesData(self):
        return self.lines[:]

    def SetLinesData(self, lines):
        self.lines = lines[:]

        self.InitBuffer()
        self.Refresh()

    def OnLeftDown(self, evt):
        self.cur_line = []
        self.pos = evt.GetPositionTuple()
        self.CaptureMouse()

    def OnLeftUp(self, evt):
        if self.HasCapture():
            self.lines.append(self.color, self.thickness, self.cur_line)
            self.cur_line = []

            self.ReleaseCapture()

    def OnMofe(self, evt):
        
