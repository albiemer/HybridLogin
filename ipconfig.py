import socket

class myip:
    ip = '192.168.1.2'
    port = '5000'

    def fullip():
        return myip.ip + ':' + myip.port

#print(myip.fullip())