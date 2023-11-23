from ferag_message import FeragMessage
from control_character import ControlCharacterSet
class ProductionDrop:
    def __init__(self):
        self.FeragMessage = FeragMessage("2403", "!")
        self.agentName = ""
        self.numberOfCopies = 0
        self.ControlCharacters = ControlCharacterSet()
        self.limit = 0
        self.maxStack = 0
        self.standard = 0
        self.parameterN = 0
        self.maxBundle = 0
        self.parameterSz = 0
        self.dontProduce = False
        self.topsheetData = ""
        self.productReferenceNumbers = []

    def TopsheetData(self):
        if self.topsheetData == "":
            return ""
        tsd = self.topsheetData
        if len(tsd) > 5996:
            tsd = tsd[:5996]
        tsdSegment = "+58" + tsd
        fm = FeragMessage("2414", "!")
        message = fm.MessageTemplate()
        return message(tsdSegment)

    def MaxBundle(self):
        return "+34%04d" % self.maxBundle

    def SetMaxBundle(self, maxBundle):
        self.maxBundle = maxBundle

    def ParameterN(self):
        return "+33%04d" % self.parameterN

    def SetParameterN(self, parameterN):
        self.parameterN = parameterN

    def Standard(self):
        return "+32%04d" % self.standard

    def SetStandard(self, standard):
        self.standard = standard

    def MaxStack(self):
        return "+31%04d" % self.maxStack

    def SetMaxStack(self, maxStack):
        self.maxStack = maxStack

    def Limit(self):
        return "+30%04d" % self.limit

    def SetLimit(self, limit):
        self.limit = limit

    def ParameterSz(self):
        return "+35%04d" % self.parameterSz

    def SetParameterSz(self, parameterSz):
        self.parameterSz = parameterSz

    def SetTopsheetData(self, topsheetData):
        self.topsheetData = topsheetData

    def ProductReferenceNumbers(self):
        prreffmt = ""
        for pr in self.productReferenceNumbers:
            prreffmt += "+99141%03d" % pr
        return prreffmt

    def AddProductReferenceNumber(self, productReferenceNumber):
        self.productReferenceNumbers.append(productReferenceNumber)

    def NumberOfCopies(self):
        return "+13%05d" % self.numberOfCopies

    def SetNumberOfCopies(self, numberOfCopies):
        self.numberOfCopies = numberOfCopies

    def AgentName(self):
        return "+12%-10s" % self.agentName

    def SetAgentName(self, agentName):
        self.agentName = agentName

    def Payload(self):
        data = self.AgentName()
        data += self.NumberOfCopies()
        data += self.ControlCharacters.GetControlCharactersMessage()
        data += self.Limit()
        data += self.MaxStack()
        data += self.Standard()
        data += self.ParameterN()
        data += self.MaxBundle()
        data += self.ParameterSz()
        data += self.ProductReferenceNumbers()
        return data

    def Message(self):
        fm = FeragMessage('2403', '!')
        message = fm.MessageTemplate()
        return message(self.Payload())

    def NewProductionDrop(self):
        return ProductionDrop()
