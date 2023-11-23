from ferag_message import FeragMessage

class RouteEnd():
    def __init__(self, ):
        super().__init__()
        self.routeName = ''

    def RouteName(self):
        return "+11%-13s" % self.routeName

    def SetRouteName(self, routeName):
        self.routeName = routeName

    def Payload(self):
        data = self.RouteName()
        return data

    def Message(self):
        fm = FeragMessage('2406', '!')
        message = fm.MessageTemplate()
        return message(self.Payload())

    def NewRouteEnd(self):
        self.FeragMessage = FeragMessage('2406', '!')
        return self
 
