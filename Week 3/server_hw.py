#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socketserver
import numpy as np
from time import sleep 
import random
import threading

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        try:
            # take 10 standard normal samples and send them across the network.
        except:
            pass

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass



if __name__ == '__main__':
    print("setting up")
    server = ThreadedTCPServer((HOST,PORT))
    print("shuttung down")
