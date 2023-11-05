import machine
import sys
from machine import Pin

class SetupBits:
    
    def __init__(self):
        # A0 - A8 are bits, if they are 0 then they are turned off, if they are 1 they are turned on
        self.A0 = 0
        self.A1 = 0
        self.A2 = 0
        self.A3 = 0
        self.A4 = 0
        self.A5 = 0
        self.A6 = 0
        self.A7 = 0
        self.A8 = 0
        
        # # bit numbers 1,2,4,8,16,32,64,128,256
        self.A0b = 1
        self.A1b = 2
        self.A2b = 4
        self.A3b = 8
        self.A4b = 16
        self.A5b = 32
        self.A6b = 64
        self.A7b = 128
        self.A8b = 256
        # set the array to 20 zeros
        self.pinArray=[0 for i in range(20)]
        
        # set 16 pins low
        for i in range(16):
            self.pinArray[i]=machine.Pin(i, machine.Pin.OUT)
            self.pinArray[i].value(0)
            
        # turn off sweep pin
        pin0=machine.Pin(0, machine.Pin.OUT)
        pin0.value(1)
     
    # writing entered frequency to master device
    def sendEcho(self,s):       
        s="from RP: "+s+"\r\n"
        sys.stdout.write(s)
    
        # set the code for the divider
    def checkBits(self):
        
        f=944+self.A0*1+self.A1*2+self.A2*4+self.A3*8+self.A4*16+self.A5*32+self.A6*64+self.A7*128+self.A8*256
        
        print("checked f=",f)
    
    def findBits(self,frequency):
        print("findBits()")
        
        # 944 is subtracted from the frequency as a starting/reference point when all bits are set to 0, 944 is the minimum frequency of the PLL Frequency Synthesizer
        d=frequency - 944
  
        done=False
        while(not done):
            # set all pins to 0/low
            for i in range(0,20):
                self.pinArray[i]=0 #.value(0)
                
            # if d/256 is greater than or equal to 1, set that bit to 1, subtract 256 from it and light up the LED
            if d/256 >=1:
                self.A8  = 1
                d=d-256
                print("A8=",self.A8)
                pin5=machine.Pin(5, machine.Pin.OUT)
                pin5.value(1)
                print("d=",d)
            else:
                # else set that bit to 0 and turn the LED off
                print('Not A8')
                self.A8 = 0
                pin5=machine.Pin(5, machine.Pin.OUT)
                pin5.value(0)
             
            # if d/128 is greater than or equal to 1, set that bit to 1, subtract 128 from it and light up the LED    
            if d/128>=1:                         
                d=d-128
                self.A7 = 1
                pin6=machine.Pin(6, machine.Pin.OUT)
                pin6.value(1)
                print("A7=",self.A7b)  
            else:
                # else set that bit to 0 and turn the LED off
                print('Not A7')     
                self.A7  = 0
                pin6=machine.Pin(6, machine.Pin.OUT)
                pin6.value(0)
            
            # if d/64 is greater than or equal to 1, set that bit to 1, subtract 64 from it and light up the LED 
            if d/64 >= 1:             
                d = d - 64
                self.A6 = 1
                pin3=machine.Pin(3, machine.Pin.OUT)
                pin3.value(1)
                print('A6=', self.A6b) 
            else:
                # else set that bit to 0 and turn the LED off
                print('Not A6')
                self.A6  = 0
                pin3=machine.Pin(3, machine.Pin.OUT)
                pin3.value(0)
            
            # if d/32 is greater than or equal to 1, set that bit to 1, subtract 32 from it and light up the LED 
            if d/32 >= 1:              
                d = d - 32
                self.A5 = 1
                pin1=machine.Pin(1, machine.Pin.OUT)
                pin1.value(1)
                print('A5=', self.A5b)  
            else:
                # else set that bit to 0 and turn the LED off
                print('Not A5')
                self.A5  = 0
                pin1=machine.Pin(1, machine.Pin.OUT)
                pin1.value(0)
            
            # if d/16 is greater than or equal to 1, set that bit to 1, subtract 16 from it and light up the LED 
            if d/16 >= 1:             
                d = d - 16
                self.A4 = 1
                pin2=machine.Pin(2, machine.Pin.OUT)
                pin2.value(1)
                print('A4=', self.A4b) 
            else:
                # else set that bit to 0 and turn the LED off
                print('Not A4')
                self.A4 = 0
                pin2=machine.Pin(2, machine.Pin.OUT)
                pin2.value(0)
           
            # if d/8 is greater than or equal to 1, set that bit to 1, subtract 8 from it and light up the LED 
            if d/8 >= 1:
                self.A3 = 1
                d = d - 8
                self.A3 = 1
                pin15=machine.Pin(15, machine.Pin.OUT)
                pin15.value(1)
                print('A3=', self.A3b)  
            else:
                # else set that bit to 0 and turn the LED off
                print('Not A3')
                self.A3  = 0
                pin15=machine.Pin(15, machine.Pin.OUT)            
                pin15.value(0)
            
            # if d/4 is greater than or equal to 1, set that bit to 1, subtract 4 from it and light up the LED 
            if d/4 >=1:            
                d = d - 4
                self.A2 = 1
                pin14=machine.Pin(14, machine.Pin.OUT)
                pin14.value(1)
                print('A2=', self.A2b)
            else:
                # else set that bit to 0 and turn the LED off
                print('Not A2')
                self.A2 = 0
                pin14=machine.Pin(14, machine.Pin.OUT)
                pin14.value(0)
             
            # if d/2 is greater than or equal to 1, set that bit to 1, subtract 2 from it and light up the LED 
            if d/2 >= 1:
                self.TestA1b = 1
                d = d - 2
                self.A1 = 1
                pin4=machine.Pin(4, machine.Pin.OUT)
                pin4.value(1)
                print('A1=', self.A1b) 
            else:
                # else set that bit to 0 and turn the LED off
                print('Not A1')
                self.A1  = 0
                pin4=machine.Pin(4, machine.Pin.OUT)
                pin4.value(0)
            
            # if d/1 is greater than or equal to 1, set that bit to 1, subtract 1 from it and light up the LED 
            if d/1 >=1:
                self.TestA0b = 1
                d = d - 1
                self.A0 = 1
                pin7=machine.Pin(7, machine.Pin.OUT)
                pin7.value(1)
                print('A0=', self.A0b)
            else:
                # else set that bit to 0 and turn the LED off
                print('Not A0')
                self.A0  = 0
                pin7=machine.Pin(7, machine.Pin.OUT)
                pin7.value(0)
                
            z=self.A0*1+self.A1*2+self.A2*4+self.A3*8+self.A4*16+self.A5*32+self.A6*64+self.A7*128+self.A8*256
            if z==0:
                frequency=944
                
            done=True


sb=SetupBits()   
# this will ask for the frequency, send to master device, and perform calculations, unless the user types "exit" it will stop the program
while True:
    x= input("RP Frequency? ")
    sb.sendEcho(x)
    if x=='exit':
        sys.exit(0)        
    print("RP frequency got=",x)  
    Frequency = int(x)
    done=False  
    sb.findBits(Frequency)
    sb.checkBits()