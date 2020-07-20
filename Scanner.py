#!/usr/bin/python3

import socket

class Scanner():

    def __init__(self):
        pass

    def grab_banner(self,ip,port):
        try:
            s = socket.socket()
            s.connect((ip,port))
            banner = s.recv(1024)
            return banner
        except Exception as e:
            return 

    def check_vulns(self,banner):
        with open('vulns.txt','r') as f:
            for line in f.readlines():
                if line.strip('\n').split('_|_')[0].encode() in banner:
                    return line.strip('\n').split('_|_')[1] 

        return

