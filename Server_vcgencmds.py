#Server_vcgencmds.py

#By Alyousef Soliman 100883692
#This program is strictly my own work. Any material
#beyond course learning materials that is taken from
#the Web or other sources is properly cited, giving
#credit to the original author(s).


"""
Server Script for Raspberry Pi
- Collects and sends system information using vcgencmd commands.
- Sends data to the client in JSON format.

Runs on Raspberry Pi.
"""

import socket
import os
import json

def get_core_temperature():
    """Fetch the CPU temperature using vcgencmd."""
    return float(os.popen('vcgencmd measure_temp').readline().replace("temp=", "").replace("'C", "").strip())

def get_core_voltage():
    """Fetch the core voltage using vcgencmd."""
    return float(os.popen('vcgencmd measure_volts core').readline().replace("volt=", "").replace("V", "").strip())

def get_arm_clock():
    """Fetch the ARM clock speed using vcgencmd."""
    return int(os.popen('vcgencmd measure_clock arm').readline().replace("frequency(48)=", "").strip())

def get_gpu_clock():
    """Fetch the GPU clock speed using vcgencmd."""
    return int(os.popen('vcgencmd measure_clock core').readline().replace("frequency(1)=", "").strip())

def get_throttled_status():
    """Fetch throttled status using vcgencmd."""
    return os.popen('vcgencmd get_throttled').readline().replace("throttled=", "").strip()

#Initialize socket
server_socket = socket.socket()
host = ''  #Listen on all interfaces
port = 5000  #Port number
server_socket.bind((host, port))
server_socket.listen(5)

print("Server is running and waiting for connections...")

while True:
    client_socket, addr = server_socket.accept()
    print(f"Connection established with {addr}")

    #Collect data
    data = {
        "Core Temperature (°C)": round(get_core_temperature(), 1),
        "Core Voltage (V)": round(get_core_voltage(), 1),
        "ARM Clock (Hz)": get_arm_clock(),
        "GPU Clock (Hz)": get_gpu_clock(),
        "Throttled Status": get_throttled_status(),
    }

    #Convert to JSON and send to client
    json_data = json.dumps(data)
    client_socket.send(bytes(json_data, 'utf-8'))
    client_socket.close()
