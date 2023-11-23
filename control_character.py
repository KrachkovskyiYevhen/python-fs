class ControlCharacterSet:
    def __init__(self):
        self.DontProduce = False
        self.BundlesToSecondaryExit = False

    def SetDontProduce(self):
        self.DontProduce = True

    def SetBundlesToSecondaryExit(self):
        self.BundlesToSecondaryExit = True

    def GetControlCharactersMessage(self):
        ccCount = 0
        ccString = ""
        if self.DontProduce:
            ccString += "D"
            ccCount += 1
        if self.BundlesToSecondaryExit:
            ccString += "T"
            ccCount += 1
        if ccCount == 0:
            return ""
        return "+14%-16s" % ccString

    def NewControlCharacterSet():
        return ControlCharacterSet()
