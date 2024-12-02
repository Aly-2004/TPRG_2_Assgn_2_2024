#Client.py

#By Alyousef Soliman 100883692
#This program is strictly my own work. Any material
#beyond course learning materials that is taken from
#the Web or other sources is properly cited, giving
#credit to the original author(s).


"""
Client Script for Raspberry Pi
- Connects to the server running on Raspberry Pi.
- Receives and displays system information sent in JSON format.

Runs on a PC or another system.
"""

import socket
import json

#Server details
host = '192.168.10.111'  #Replace with the Raspberry Pi's IP address
port = 5000

#Creates a socket and connect to the server
client_socket = socket.socket()
client_socket.connect((host, port))

#Receives data from the server
data = client_socket.recv(1024)
client_socket.close()

#Parses the JSON data
parsed_data = json.loads(data.decode('utf-8'))

#Prints the received data
print("System Information from Raspberry Pi:")
for key, value in parsed_data.items():
    print(f"{key}: {value}")
