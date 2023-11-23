class FeragMessage:
    def __init__(self, messageStart, messageEnd):
        self.messageStart = messageStart
        self.messageEnd = messageEnd

    def getMessageStart(self):
        return "%%%s" % self.messageStart
    
    def getMessageEnd(self):
        return "%s" % self.messageEnd

    def MessageTemplate(self):
        def inner(s):
            message = self.getMessageStart()
            message += s
            message += self.getMessageEnd()
            return message.strip() + "\n"
        return inner
