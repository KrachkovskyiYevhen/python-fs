from title_info import TitleInfo
from title_end import TitleEnd
from product_reference import ProductReference
from route import Route
from route_list import RouteListEntry
from product_reference import MissingParameter

class FeragString:
    def __init__(self):
        self.TitleInfo = TitleInfo()
        self.TitleEnd = TitleEnd()
        self.ProductReferences = []
        self.ProductReferencesNr = 0
        self.Routes = []
        self.RouteCount = 0
        self.RouteListEntries = []
        self.RouteListEntryCount = 0
        self.RouteInfoEntries = []
        self.ProductionDropEntries = []
        self.RouteEndEntries = []
        
        self.productReference = ProductReference()
        self.missingParameter = MissingParameter()
        self.route = Route()
        
    def newProductReference():
        pr = ProductReference()
        return pr.NewProductReference()

    def SetTitleName(self, titleName):
        self.TitleInfo.SetTitleName(titleName)
        self.TitleEnd.SetTitleName(titleName)

    def PrintOut(self):
        info = self.TitleInfo.Message()
        for pr in self.ProductReferences:
            info += pr.Message()
        for rt in self.Routes:
            info += rt.GetRouteListEntry().Message()
        for rt in self.Routes:
            info += rt.GetRouteMessage()
        info += self.TitleEnd.Message()
        return info

    def AddProductReference(self, pr = ProductReference()):
        if pr.productReferenceNumber == 0:
            self.ProductReferencesNr += 1
            pr.SetProductReferenceNumber(self.ProductReferencesNr)
        if pr.productReferenceNumber == 1 and pr.productUsageType == 0:
            pr.SetProductUsageType(1)
        self.ProductReferences.append(pr)
        return None

    def AddRoute(self, r):
        self.RouteCount += 1
        self.Routes.append(r)
        return None
    
    def NextRouteCode(self):
        return self.RouteCount + 1

    def AddRouteListEntry(self, rl):
        self.RouteListEntryCount += 1
        self.RouteListEntries.append(rl)
        return None

    def AddRouteInfo(self, ri):
        self.RouteInfoEntries.append(ri)
        return None

    def AddProductionDrop(self, pd):
        self.ProductionDropEntries.append(pd)
        return None

    def AddRouteEnd(self, re):
        self.RouteEndEntries.append(re)
        return None
