'''
1) open putty and run serverForVcoClient.py with 
execfile("serverForVcoClient.py") on RP2040

2) run in spyder main.py and enter frequency


'''

import serial
import sys

class Connector_SerialPort:
    
    def __init__(self,main):
     
        self.main=main
        self.RFtype='CW'      
        # open USB 
        self.ser = serial.Serial('/dev/ttyACM0', 9600)
    
    # send data to RP2040
    def send_to_microcontroller(self,data):
        
        data=str(data)+"\r\n"
        self.ser.write(data.encode())
        print(data.encode())
        
    # receive data from the RP2040    
    def receive_from_microcontroller(self):
        
        self.receive=self.ser.read()        
        if self.receive:
            print("RPI got from Pico: ",self.receive.decode('utf-8').rstrip())