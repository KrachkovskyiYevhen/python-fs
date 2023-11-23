from ferag_message import FeragMessage
class RouteInfo():
    def __init__(self):
        super().__init__()
        self.routeName = ""
        self.limit = 0
        self.maxStack = 0
        self.standard = 0
        self.parameterN = 0
        self.maxBundle = 0
        self.parameterSz = 0
        self.topsheetMarker = 0
        self.eaMarker = 0
        self.eaAddressDefinition = 0
        self.topsheetTemplateDirectory = 0
        self.editionName = ""
        self.productReferenceNumbers = []

    def ParameterSz(self):
        return "+35%04d" % self.parameterSz

    def SetParameterSz(self, parameterSz):
        self.parameterSz = parameterSz

    def ProductReferenceNumbers(self):
        prreffmt = ""
        for pr in self.productReferenceNumbers:
            prreffmt += "+41%02d" % pr
        return prreffmt

    def AddProductReferenceNumber(self, productReferenceNumber):
        self.productReferenceNumbers.append(productReferenceNumber)

    def TopsheetTemplateDirectory(self):
        return "+56%03d" % self.topsheetTemplateDirectory

    def SetTopsheetTemplateDirectory(self, topsheetTemplateDirectory):
        self.topsheetTemplateDirectory = topsheetTemplateDirectory

    def EaMarker(self):
        return "+69%1d" % self.eaMarker

    def SetEaMarker(self, eaMarker):
        self.eaMarker = eaMarker

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

    def EditionName(self):
        if self.editionName == "":
            return ""
        return "+20%-30s" % self.editionName

    def SetEditionName(self, editionName):
        self.editionName = editionName

    def EaAddressDefinition(self):
        if self.eaAddressDefinition == 0:
            return ""
        return "+91%06d" % self.eaAddressDefinition

    def SetEaAddressDefinition(self, eaAddressDefinition):
        self.eaAddressDefinition = eaAddressDefinition

    def TopsheetMarker(self):
        return "+59%1d" % self.topsheetMarker

    def SetTopsheetMarker(self, topsheetMarker):
        self.topsheetMarker = topsheetMarker

    def SetRouteName(self, routeName):
        self.routeName = routeName

    def RouteName(self):
        return "+11%-13s" % self.routeName

    def Payload(self):
        data = self.RouteName()
        data += self.Limit()
        data += self.MaxStack()
        data += self.Standard()
        data += self.ParameterN()
        data += self.MaxBundle()
        data += self.ParameterSz()
        data += self.TopsheetMarker()
        data += self.EaMarker()
        data += self.EaAddressDefinition()
        data += self.TopsheetTemplateDirectory()
        data += self.EditionName()
        data += self.ProductReferenceNumbers()
        return data

    def Message(self):
        fm = FeragMessage('2402', '!')
        message = fm.MessageTemplate()
        return message(self.Payload())

    def NewRouteInfo(self):
        self.FeragMessage = FeragMessage('2402', '!')
        return self