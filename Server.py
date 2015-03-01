from twisted.internet.protocol import Factory
from twisted.protocols.basic import LineReceiver
from twisted.internet import reactor

GETINFO = "GETINFO"
RUNGAME = "RUNGAME"

class Server(LineReceiver):
    def __init__(self, users):
        self.users = users
        #self.controller = controller
        #self.name = None
        #self.state = GETINFO

    def connectionMade(self):
        self.users.append(self)
        # Send info to player regarding what 
        #self.sendLine("What's your name?")

    def connectionLost(self, reason):
        print "connection lost"
        #if self.users.contains(self):
        #    del self.users[self.name]
            
        # Try to reestablish connection

    def lineReceived(self, line):
        for protocol in self.users:
            if protocol != self:
                protocol.sendLine(line)
        #if self.state == GETINFO:
        #    self.handle_GETINFO(line)
        #else:
        #    self.handle_RUNGAME(line)

    def handle_GETINFO(self, name):
        #self.sendLine("Welcome, %s!" % (name,))
        #self.name = name
        self.users.append(self)
        self.state = RUNGAME

    def handle_CHAT(self, message):
        message = "<%s> %s" % (self.name, message)
        for name, protocol in self.users.iteritems():
            if protocol != self:
                protocol.sendLine(message)
        

    def sendMessage(self, message):
        for name, protocol in self.users.iteritems():
            if protocol != self:
                protocol.sendLine(message)

class ServerFactory(Factory):
    def __init__(self):
        #self.controller = controller
        self.users = [] # maps user names to Chat instances

    def buildProtocol(self, addr):
        return Server(self.users)


if __name__ == "__main__":
    reactor.listenTCP(8123, ServerFactory())
    reactor.run()
