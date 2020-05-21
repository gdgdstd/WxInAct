

import random
import string 
import wx 
import wx.grid 


def _gen_data():

    def to_format1():
        length = random.randrange(1,3)
        text = ''.join(random.sample(string.ascii_letters,length))
        text = text.upper()
        return text

    def to_format2():
        length = random.randrange(3,5)
        text = ''.join(random.sample(string.ascii_letters,length))
        text = text.capitalize()
        return text    

    def to_format3():
        length = random.randrange(4,11)
        text = ''.join(random.sample(string.ascii_letters,length))
        text = text.capitalize()
        return text 

    data = []
    for x in range(10):
        text1 = to_format1()
        text2 = to_format2()
        text3 = to_format3()

        data.append((text1,text2, text3))
    return tuple(*data)

def _gen_labels():
    return ('Last', 'First')

class LineupTable(wx.grid.PyGridTableBase):

    data =  _gen_data()
    labels = _gen_labels()

    def __init__(self):
        super().__init__()

    def GetNumberRows(self):
        return len(self.data)

    def GetNumberCols(self):
        return self.data[0]-1

    
