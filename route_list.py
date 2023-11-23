from ferag_message import FeragMessage

class RouteListEntry():
    def __init__(self):
        super().__init__()
        self.routeName = ""
        self.routeCode = 0
        self.rampNumber = -1
        self.copiesInRoute = 0

    def CopiesInRoute(self):
        if self.copiesInRoute == 0:
            return ""
        return "+23%06d" % self.copiesInRoute

    def SetCopiesInRoute(self, copiesInRoute):
        self.copiesInRoute = copiesInRoute

    def RampNumber(self):
        if self.rampNumber == -1:
            return ""
        return "+25%02d" % self.rampNumber

    def SetRampNumber(self, rampNumber):
        self.rampNumber = rampNumber

    def RouteCode(self):
        if self.routeCode == 0:
            return ""
        return "+79%05d" % self.routeCode

    def SetRouteCode(self, routeCode):
        self.routeCode = routeCode

    def RouteName(self):
        return "+11%-13s" % self.routeName

    def SetRouteName(self, routeName):
        self.routeName = routeName

    def Payload(self):
        data = self.RouteName()
        data += self.RouteCode()
        data += self.RampNumber()
        data += self.CopiesInRoute()
        return data

    def Message(self):
        fm = FeragMessage('2401', '!')
        message = fm.MessageTemplate()
        return message(self.Payload())

    def NewRouteListEntry(self):
        self.FeragMessage = FeragMessage('2401', '!')
        self.rampNumber = -1
        return self