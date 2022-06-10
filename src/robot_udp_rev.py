import socket
import struct
import numpy as np

UDP_IP = "127.0.0.1"
UDP_PORT = 8787

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)
print("start...")

point = np.zeros(6,np.float32) # px,py,pz,rx,ry,rz

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print("received message: %s" % data)

    try:
        for i in range(6):
            point[i] = struct.unpack('f', data[i*4:i*4+4])[0]
        print(point)
    except:
        print("data error...")