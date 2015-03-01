from twisted.internet.protocol import Factory, ClientFactory
from twisted.protocols.basic import LineReceiver
from twisted.internet import reactor

GETINFO = "GETINFO"
RUNGAME = "RUNGAME"

class Client(LineReceiver):
    def __init__(self, users, controller):
        self.controller = controller
        self.connect = None

    #def connectionMade(self):
        #self.users.append(self)
        # Send info to player regarding what 
        #self.sendLine("What's your name?")

    #def connectionLost(self, reason):            
        # Try to reestablish connection

    def lineReceived(self, line):
        self.controller.handleListenerInput(line)
        #for protocol in self.users:
        #   if protocol != self:
        #        protocol.sendLine(line)
        #if self.state == GETINFO:
        #    self.handle_GETINFO(line)
        #else:
        #    self.handle_RUNGAME(line)        

    def sendMessage(self, message):
        self.sendLine(message)
        #for name, protocol in self.users.iteritems():
        #    if protocol != self:
        #        protocol.sendLine(message)

class Client_Factory(ClientFactory):
    def __init__(self, controller):
        self.controller = controller
        self.users = [] # maps user names to Chat instances
        self.protocol = None

    def buildProtocol(self, addr):
        self.protocol = Client(self.users, self.controller)
        return self.protocol


if __name__ == "__main__":
    reactor.listenTCP(8123, Client_Factory("hello"))
    reactor.run()
