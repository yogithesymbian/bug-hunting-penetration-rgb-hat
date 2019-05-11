#!/usr/bin/python
import socket

# recording input into variable -> raw_input()
ip = raw_input("Enter the ip :")
# i want save our port as an integer
port = input("Enter the port :")

# create a socket object [TCP Network   ]
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# evaluate the returned value of the connection our tcp
# if connection is succeeds will return 0
# if connection is fail will return a positive integer or true 
if s.connect_ex((ip, port)):
    print "Port", port, "is closed"
else:
    print "Port", port, "is open"
