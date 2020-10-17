#Program to find IP address of the client

#import socket module 
import socket

host_name = socket.gethostname()
print('Host Name: {}'.format(host_name))
ip_addr = socket.gethostbyname(host_name)
print('IP Address: {}'.format(ip_addr))
