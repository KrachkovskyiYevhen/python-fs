from ferag_message import FeragMessage

class TitleEnd:
    def __init__(self):
        self.titleName = ""
        self.FeragMessage = FeragMessage("2441", "!")

    def TitleName(self):
        return "+40%-8s" % self.titleName

    def SetTitleName(self, titleName):
        self.titleName = titleName

    def Message(self):
        fm = FeragMessage('2441', '!')
        message = fm.MessageTemplate()
        return message(self.TitleName())

    def NewTitleEnd(self):
        self.FeragMessage = FeragMessage('2441', '!')
        return self