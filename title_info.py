import datetime
from ferag_message import FeragMessage

class TitleInfo:
    def __init__(self):
        self.feragMessage = FeragMessage("2440", "!")
        self.printObjectName = ""
        self.titleName = ""
        self.publicationDate = datetime.datetime.now()
        self.issueReference = ""
        self.countryCode = ""
        self.printObjectColor = ""
        self.additionalInfo = ""
        self.showEmptyAdditionalInfo = False

    def ShowEmptyAdditionalInfo(self):
        self.showEmptyAdditionalInfo = True

    def SetPrintObjectName(self, printObjectName):
        self.printObjectName = printObjectName

    def AdditionalInfo(self):
        if self.additionalInfo == "" and not self.showEmptyAdditionalInfo:
            return ""
        return "+08" + self.additionalInfo

    def SetAdditionalInfo(self, additionalInfo):
        self.additionalInfo = additionalInfo

    def PrintObjectColor(self):
        if self.printObjectColor == "":
            return ""
        return "+94" + self.printObjectColor

    def SetPrintObjectColor(self, printObjectColor):
        self.printObjectColor = printObjectColor

    def CountryCode(self):
        if self.countryCode == "":
            return ""
        return "+97" + self.countryCode

    def SetCountryCode(self, countryCode):
        self.countryCode = countryCode

    def SetPublicationDate(self, publicationDateString):
        self.publicationDate = datetime.datetime.strptime(publicationDateString, "%Y-%m-%d")

    def PublicationDate(self):
        if self.publicationDate == "":
            return ""
        return "+95" + self.publicationDate.strftime("%Y%m%d")

    def Message(self):
        fm = FeragMessage('2440', '!')
        message = fm.MessageTemplate()
        return message(self.Payload())
    
    def Payload(self):
        data = self.PrintObjectName()
        data += self.TitleName()
        data += self.PublicationDate()
        data += self.IssueReference()
        data += self.CountryCode()
        data += self.PrintObjectColor()
        data += self.AdditionalInfo()
        return data

    def SetIssueReference(self, issueReference):
        self.issueReference = issueReference

    def IssueReference(self):
        if self.issueReference == "":
            return ""
        return "+99195" + self.issueReference

    def PrintObjectName(self):
        if self.printObjectName == "":
            return ""
        return "+11%-13s" % ("+93" + self.titleName)

    def TitleName(self):
        return "+40%-8s" % self.titleName

    def SetTitleName(self, titleName):
        self.titleName = titleName

    def NewTitleInfo(self):
        self.FeragMessage = FeragMessage('2440', '!')
        return self
