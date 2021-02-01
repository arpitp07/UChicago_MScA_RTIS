import socket
import sys
import time

HOST, PORT = "localhost", 9999
# data = " ".join(sys.argv[1:])
data = 'arpit'

# Create a socket (SOCK_STREAM means a TCP socket)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    # sock.sendall(bytes(data + "\n", "utf-8"))

    # Receive data from the server and shut down
    rec = []
    for i in range(10):
        received = int(sock.recv(1024))
        # received = int(received)
        rec.append(received)
        print(f"Average: {sum(rec)/len(rec)}")
        # time.sleep(1)    

# print("Sent:     {}".format(data))
