from SocketServer import TCPServer,StreamRequestHandler,ForkingMixIn,ThreadingMixIn
import time
class Handler(StreamRequestHandler):

    def handle(self):
        addr=self.request.getpeername()
        print 'Got connection from',addr
        time.sleep(20)
        self.wfile.write('Thank you for connecting')

class F_server(ForkingMixIn,TCPServer):
    pass

class T_server(ThreadingMixIn,TCPServer):
    pass


#server=TCPServer(('',1234),Handler)
server=T_server(('',1234),Handler)
server.serve_forever()
