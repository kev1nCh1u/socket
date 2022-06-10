
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
PORT = 9930
network = "221.120.83.108"
network = "192.168.72.110"
# s.sendto('Sm;0;E'.encode('utf-8'), (network, PORT))
# s.sendto('Sm;1,test;E'.encode('utf-8'), (network, PORT))
s.sendto('Mr;0,0,-0.8,0.08,-0.02,diff,0,1.0,test;1,3,2.34,-2.21,1.53,diff,0,1.0,test,0.1;2,19,2.3,0.71,1.55,diff,0,1.0,test;3,3,3.02,-0.94,1.55,diff,0,1.0,test,2;4,3,2.98,1.89,-0.002,diff,0,1.0,test,0;5,3,3.97,1.82,-1.52,diff,0,1.0,test,0;6,3,4.09,-0.85,-1.52,diff,0,1.0,test,2;E'.encode('utf-8'), (network, PORT))
print('send')
