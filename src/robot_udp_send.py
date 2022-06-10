
# py3
import socket
import numpy as np
import struct

UDP_IP = "127.0.0.1"
UDP_PORT = 8787

point = np.zeros(6,np.float32) # px,py,pz,rx,ry,rz
point[0] = 1.1
point[1] = 2.1
point[2] = 3.1
point[3] = 4.1
point[4] = 5.1
point[5] = 6.1
message = b""
for i in range(6):
    message += struct.pack('f', point[i])

print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)
print("message: %s" % message)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
sock.sendto(message, (UDP_IP, UDP_PORT))