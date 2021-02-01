import socketserver
import time

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        # self.data = self.request.recv(1024).strip()
        # print("{} wrote:".format(self.client_address[0]))
        # print(self.data)
        # just send back the same data, but upper-cased
        for i in range(10):
            number_byte = bytes(str(i), "utf-8")
            self.request.sendall(number_byte)
            time.sleep(1)

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()