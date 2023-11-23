from ferag_message import FeragMessage
class ProductReference:
    def __init__(self):
        self.FeregMessage = FeragMessage("2450", "!") 
        self.productReferenceNumber = 0
        self.productName = ""
        self.productUsageType = 0
        self.sheetLayers = 0
        self.copiesAssigned = 0
        self.productWeight = 0
        self.supervision = 0
        self.overlap = 0
        self.feedingMode = 0
        self.scatter = 0
        self.issueReference = ""

    def IssueReference(self):
        if self.issueReference == "":
            return ""
        return "+99195%-8s" % self.issueReference

    def SetIssueReference(self, issueReference):
        self.issueReference = issueReference
        
    def MissingParameter(self):
        return "+99105%04d%08d" % (self.missingParameter.missingRate, self.missingParameter.missingSize)

    def SetMissingParameter(self, missingParameter):
        self.missingParameter = missingParameter

    def Scatter(self):
        return "+99276%06d" % self.scatter

    def SetScatter(self, scatter):
        self.scatter = scatter

    def FeedingMode(self):
        return "+99101%02d" % self.feedingMode

    def SetFeedingMode(self, feedingMode):
        self.feedingMode = feedingMode

    def Overlap(self):
        return "+45%02d" % self.overlap

    def SetOverlap(self, overlap):
        self.overlap = overlap

    def Supervision(self):
        return "+44%02d" % self.supervision

    def SetSupervision(self, supervision):
        self.supervision = supervision

    def ProductWeight(self):
        return "+36%05d" % self.productWeight

    def SetProductWeight(self, productWeight):
        self.productWeight = productWeight

    def CopiesAssigned(self):
        return "+02%08d" % self.copiesAssigned

    def SetCopiesAssigned(self, copiesAssigned):
        self.copiesAssigned = copiesAssigned

    def SheetLayers(self):
        return "+35%04d" % self.sheetLayers

    def SetSheetLayers(self, sheetLayers):
        self.sheetLayers = sheetLayers

    def ProductUsageType(self):
        return "+55%02d" % self.productUsageType

    def SetProductUsageType(self, productUsageType):
        self.productUsageType = productUsageType

    def ProductName(self):
        return "+42%-30s" % self.productName

    def SetProductName(self, productName):
        self.productName = productName

    def ProductReferenceNumber(self):
        return "+99141%03d" % self.productReferenceNumber

    def SetProductReferenceNumber(self, productReferenceNumber):
        self.productReferenceNumber = productReferenceNumber

    def GetProductReferenceNumber(self):
        return self.productReferenceNumber

    def NewProductReference(self):
        self.FeregMessage = FeragMessage("2450", "!")
        self.missingParameter = MissingParameter()
        return self

    def payload(self):
        data = self.ProductReferenceNumber()
        data += self.ProductName()
        data += self.ProductUsageType()
        data += self.SheetLayers()
        data += self.CopiesAssigned()
        data += self.ProductWeight()
        data += self.Supervision()
        data += self.Overlap()
        data += self.FeedingMode()
        #data += self.Scatter()
        data += self.MissingParameter()
        data += self.IssueReference()
        return data

    def Message(self):
        fm = FeragMessage('2450', '!')
        message = fm.MessageTemplate()
        return message(self.payload())


class MissingParameter:
    def __init__(self):
        self.missingRate = 0
        self.missingSize = 1

    def NewMissingParameter(self, missingRate, missingSize):
        self.missingRate = missingRate
        self.missingSize = missingSize
        return self
