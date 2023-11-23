from route_list import RouteListEntry
from route_info import RouteInfo
from route_end import RouteEnd

class Route:
    def __init__(self):
        self.routeName = ""
        self.routeCode = 0
        self.rampNumber = 0
        self.copiesInRoute = 0
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
        self.ProductionDrops = []

    def GetRouteListEntry(self):
        rle = RouteListEntry()
        rle.SetRouteName(self.routeName)
        rle.SetRouteCode(self.routeCode)
        rle.SetRampNumber(self.rampNumber)
        rle.SetCopiesInRoute(self.copiesInRoute)
        return rle

    def GetRouteMessage(self):
        ri = RouteInfo().NewRouteInfo()
        ri.SetRouteName(self.routeName)
        ri.SetLimit(self.limit)
        ri.SetMaxStack(self.maxStack)
        ri.SetStandard(self.standard)
        ri.SetParameterN(self.parameterN)
        ri.SetMaxBundle(self.maxBundle)
        ri.SetParameterSz(self.parameterSz)
        ri.SetTopsheetMarker(self.topsheetMarker)
        ri.SetEaMarker(self.eaMarker)
        ri.SetEaAddressDefinition(self.eaAddressDefinition)
        ri.SetTopsheetTemplateDirectory(self.topsheetTemplateDirectory)
        ri.SetEditionName(self.editionName)
        for pr in self.productReferenceNumbers:
            ri.AddProductReferenceNumber(pr)
        info = ri.Message()

        for pd in self.ProductionDrops:
            info += pd.Message()
            info += pd.TopsheetData()

        re = RouteEnd().NewRouteEnd()
        re.SetRouteName(self.routeName)
        info += re.Message()

        return info

    def AddProductReferenceNumber(self, prnr):
        self.productReferenceNumbers.append(prnr)

    def AddProductionDrop(self, pd):
        self.ProductionDrops.append(pd)

    def SetRouteName(self, routeName):
        self.routeName = routeName

    def SetRouteCode(self, routeCode):
        self.routeCode = routeCode

    def SetRampNumber(self, rampNumber):
        self.rampNumber = rampNumber

    def SetCopiesInRoute(self, copiesInRoute):
        self.copiesInRoute = copiesInRoute

    def SetLimit(self, limit):
        self.limit = limit

    def SetMaxStack(self, maxStack):
        self.maxStack = maxStack

    def SetStandard(self, standard):
        self.standard = standard

    def SetParameterN(self, parameterN):
        self.parameterN = parameterN

    def SetMaxBundle(self, maxBundle):
        self.maxBundle = maxBundle

    def SetTopsheetMarker(self, topsheetMarker):
        self.topsheetMarker = topsheetMarker

    def SetEaMarker(self, eaMarker):
        self.eaMarker = eaMarker

    def SetTopsheetTemplateDirectory(self, topsheetTemplateDirectory):
        self.topsheetTemplateDirectory = topsheetTemplateDirectory

    def SetEditionName(self, editionName):
        self.editionName = editionName

    def NewRoute():
        r = Route()
        r.rampNumber = -1
        return r
