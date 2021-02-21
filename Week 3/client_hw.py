#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import statistics
import threading

thread_number = 10
res_mean = [None] * thread_number
res_stdev = [None] * thread_number

    
class TCPClient(threading.Thread):

    def __init__(self, offset, host, port):
        super().__init__()
        self.offset = offset
        self.host = host
        self.port = port

    def work_with_server(self):
        global res_mean
        global res_stdev
        # set up socket just like we do in class


        try:
            # connect to server
            nb = []  # --> [1.006, 0.9867]

            # b'1.006\s0.9867\s1.05'

            while True:
                # receive data from server
            res_mean[self.offset] = # calculate the mean of mean
            res_stdev[self.offset] = # calculate the mean of stdev
        except Exception:
            # process after exception
        finally:
            # clean up


    def run(self):
        self.work_with_server()


