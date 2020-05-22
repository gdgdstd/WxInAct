import random
import string
import wx
import wx.grid


def m_gen_data():
    def to_format1():
        length = random.randrange(1, 3)
        text = "".join(random.sample(string.ascii_letters, length))
        text = text.upper()
        return text

    def to_format2():
        length = random.randrange(3, 5)
        text = "".join(random.sample(string.ascii_letters, length))
        text = text.capitalize()
        return text

    def to_format3():
        length = random.randrange(4, 11)
        text = "".join(random.sample(string.ascii_letters, length))
        text = text.capitalize()
        return text

    data = []
    for _ in range(10):

        text1 = to_format1()
        text2 = to_format2()
        text3 = to_format3()

        data.append((text1, text2, text3))
    return data


def m_gen_labels():
    return ("Last", "First")


class GenericTable(wx.grid.GridTableBase):
    def __init__(self, data, row_labels=None, col_labels=None):
        super().__init__()

        self.data = data
