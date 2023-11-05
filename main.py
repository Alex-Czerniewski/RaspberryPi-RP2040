#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 18:04:14 2023

@author: Alex
"""

from bits import *
from PyQt5 import QtCore as qtc
from PyQt5 import QtWidgets  as qtw
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, 
QLineEdit, QInputDialog)
from Connector_SerialPort import Connector_SerialPort
import sys
import serial
import time, socket
import threading
from ExcelUtil import ExcelUtil

class Main(qtw.QMainWindow):    
    def __init__(self):        
        super(Main,self).__init__()
        self.bits=Ui_MainWindow()
        self.bits.setupUi(self)    
        print ("show GUI")
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
        
        # bit numbers 1,2,4,8,16,32,64,128,256
        self.A0b = 1
        self.A1b = 2
        self.A2b = 4
        self.A3b = 8
        self.A4b = 16
        self.A5b = 32
        self.A6b = 64
        self.A7b = 128
        self.A8b = 256
        
        self.bits.btn_Connect.clicked.connect(self.t_makeConnection)
        self.bits.btn_SActrf.clicked.connect(self.CTRFreq)
        self.bits.btn_SAspan.clicked.connect(self.Span)
        self.bits.btn_reset.clicked.connect(self.Reset)
        self.bits.btn_enter.clicked.connect(self.smallReset)
        self.bits.btn_enter.clicked.connect(self.findBits) 
        self.bits.btn_enter.clicked.connect(self.checkBits)
        self.bits.btn_sweep.clicked.connect(self.t_Sweep)
        
        # initialize excelUtill
        self.excelUtil=ExcelUtil()
        
        # get the file name and directory to write xlsx file to
        directory=self.bits.ledit_Directory.text()
        filename=self.bits.ledit_FileName.text()
        
        self.connector_SerialPort=Connector_SerialPort(self)
        
        # add to file name the file suffix ".xlsx" and directory
        self.fileName=directory+filename+".xlsx"
        
        # create the xlsx file
        self.excelUtil.createFile(self.fileName)
        self.writeLabels();
        
        self.rowF=1;self.col=1;self.rowP=2
        
    def writeLabels(self):
      self.excelUtil.writeData(1,0,"Freq SET"  )
      self.excelUtil.writeData(2,0,"Freq READ"  )
      self.excelUtil.writeData(3,0,"Error"  )
      self.excelUtil.writeData(4,0,"Power dBm"  )
    
    def t_makeConnection(self):
        t = threading.Thread(target=self.makeConnection)
        t.start()  
    
    # create socket server
    def makeConnection(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        PORT = self.bits.ledit_PORT.text()
        IP=self.bits.ledit_IP.text()
        PORT = int(PORT)
        
        self.s.connect((f'{IP}', PORT))
        
        self.s.sendall('*IDN?\n'.encode())
        
        print(self.s.recv(4096))
    
    # have option to set the span of the Spectrum Analyzer
    def Span(self):
        span = self.bits.ledit_Span.text()
        span = int(span)
        span = span * 1000000
        span = str(span)
        Spancmd = 'SENS:FREQ:SPAN ' + span+ "\n"
        self.s.sendall(Spancmd.encode())
        span = int(span)
        span = span / 1000000
        span = str(span)
        self.bits.txtedit_DSA.setText("Span Has Been Set To "+ span +" MHz")
    
    # have option to set the center frequency of the Spectrum Analyzer
    def CTRFreq(self):
        ctrfreq = self.bits.ledit_CTRF.text()
        ctrfreq = int(ctrfreq)
        ctrfreq = ctrfreq * 1000000
        ctrfreq = str(ctrfreq)
        Centercmd = 'SENS:FREQ:CENT ' + ctrfreq+ "\n"
        self.s.sendall(Centercmd.encode())
        ctrfreq = int(ctrfreq)
        ctrfreq = ctrfreq / 1000000
        ctrfreq = str(ctrfreq)
        self.bits.txtedit_DSA.setText("Center Frequency Has Been Set To "+ ctrfreq+ " MHz")
    
    # reset the GUI
    def Reset(self):
        self.bits.cbox_bit1.setChecked(False)
        self.bits.cbox_bit2.setChecked(False)
        self.bits.cbox_bit4.setChecked(False)
        self.bits.cbox_bit8.setChecked(False)
        self.bits.cbox_bit16.setChecked(False)
        self.bits.cbox_bit32.setChecked(False)
        self.bits.cbox_bit64.setChecked(False)
        self.bits.cbox_bit128.setChecked(False)
        self.bits.cbox_bit256.setChecked(False)
        self.bits.ledit_ofreq.setText("")
        self.bits.ledit_freq.setText("")
        self.bits.txtedit_freq.setText("")
        self.bits.txtedit_freq.setText("Successfully Reset")
    
    # set the code for the divider
    def checkBits(self):
        
        f=944+self.A0*1+self.A1*2+self.A2*4+self.A3*8+self.A4*16+self.A5*32+self.A6*64+self.A7*128+self.A8*256
        
        print("RPI checkBits f=",f)
    
    # only resets the checkboxes
    def smallReset(self):
        self.bits.cbox_bit1.setChecked(False)
        self.bits.cbox_bit2.setChecked(False)
        self.bits.cbox_bit4.setChecked(False)
        self.bits.cbox_bit8.setChecked(False)
        self.bits.cbox_bit16.setChecked(False)
        self.bits.cbox_bit32.setChecked(False)
        self.bits.cbox_bit64.setChecked(False)
        self.bits.cbox_bit128.setChecked(False)
        self.bits.cbox_bit256.setChecked(False)

    def t_Sweep(self):
        t = threading.Thread(target=self.Sweep)
        t.start()  
    
    # get spurs
    def findSpurs(self):
        print("find spurs")
        cmd=":CALC:MARK1:CPE 0"+"\r\n";self.s.sendall(cmd.encode())   
        # get the y value of the marker
        cmd="CALC:MARK1:Y?"+"\r\n";  self.s.sendall(cmd.encode())
        # receive and decode the y value of the marker
        rv=self.s.recv(2048);rv=rv.decode()
        
        # try to float rv
        try:
            Pc=float(rv)
            print("Pc=",Pc)
        # except if it's not a number, put a bogus number
        except ValueError:
                Pc=-100.0

        
        time.sleep(5)
        # find the next peak 
        cmd=":CALC:MARK1:MAX:NEXT"+"\r\n";  self.s.sendall(cmd.encode())
        # get the y value of the next peak  
        cmd="CALC:MARK1:Y?"+"\r\n";  self.s.sendall(cmd.encode())
        # receive and decode the next peak y value
        ps=self.s.recv(2048);ps=ps.decode()
        
        # try to float the ps
        try:
            Psp=float(ps)
            Psp=round(Psp,1)
        
        # except if it's not a number, put a bogus number
        except ValueError:
                Psp=-100.0
        print("Psp=",Psp)
        # delta is the second peak minus the first peak
        delta=Psp-Pc
        # print what delta is
        print("delta=",delta)
        # return delta
        return delta

    # frequency sweep sa only?
    def Sweep(self):
        
        # set the attenuation
        cmd=":SENSe:POWer:RF:ATT 5"+"\r\n";self.s.sendall(cmd.encode());time.sleep(1)
        
        # if these radio buttons are checked, set the span, resolution, and vid
        if self.bits.rbtn_Sweep.isChecked():
            span="5000000"   
            res="30000"
            vid="10000"
        if self.bits.rbtn_SpurNB.isChecked():
            span="10000000"
            res="10000"
            vid="10000"
        if self.bits.rbtn_SpurWB.isChecked():
            span="1000000000"  
            res="100000"
            vid="30000"
        
        # set the resolution
        cmd=":SENSe:BANDwidth:RES "+res+"\r\n";self.s.sendall(cmd.encode());time.sleep(1)
        
        cmd=":SENSe:BANDwidth:VID "+vid+"\r\n";self.s.sendall(cmd.encode());time.sleep(1)

        # set the span for the Spectrum Analyzer
        cmd = 'SENS:FREQ:SPAN ' + span+ "\n";  self.s.sendall(cmd.encode())
        
        # turn on a marker
        cmd=":CALC:MARK1:STAT ON";self.s.sendall(cmd.encode())
        cmd=":CALC:MARK1:CPE OFF"+"\r\n";self.s.sendall(cmd.encode()) 
        
        # find the marker's peak
        cmd=":CALCulate:MARKer<n>:CPEak?";self.s.sendall(cmd.encode())
        
        # get the sweep parameters
        minf = float(self.bits.ledit_minf.text())
        maxf = float(self.bits.ledit_maxf.text())
        stepsize = float(self.bits.ledit_stepS.text())
        t = self.bits.ledit_dwellT.text()
        
        t = int(t)
    
        
        self.f=minf;count=0
        while self.f<=maxf:
            f2 = self.f
            print(f2)
            print("in sweep()")
            
            # get/set bits for VCO
            self.setFrequency(f2)             
            
            #set Spectrum Analyzer
            print("set SA Frequency()")
            # if the check box "Div64" is not checked, set the center frequency to "f"
            if self.bits.cbox_Div64.isChecked()==False:   
                print("f2=",f2)
                self.centerFrequency = ':SENSe:FREQuency:CENTer '+str(self.f) +"MHz\r\n"            
                self.s.send(self.centerFrequency.encode())   
            
            # if the check box "Div64" is checked, divide the current frequency by 64, and set the center frequency to "f"
            if self.bits.cbox_Div64.isChecked()==True:    
                F=f2/64
                F=round(F,4)         
                self.centerFrequency = ':SENSe:FREQuency:CENTer '+str(F) +"MHz\r\n"            
                # send command to SA
                self.s.send(self.centerFrequency.encode())              
            time.sleep(1)
            # get frequency
            cmd=":CALC:MARK1:CPE:STAT ON"+"\r\n";self.s.sendall(cmd.encode())
            self.rvf=1
            # get the x value of mark1
            cmdF="CALC:MARK1:X?"+"\r\n"
            self.s.sendall(cmdF.encode())
            # receive frequency
            self.rvf=self.s.recv(2048)
            self.rvf=self.rvf.decode()
            time.sleep(2)
            #set Spec An peak search
            cmd="CALC:MARK1:Y?"+"\r\n"
            # send for frequency
            self.s.sendall(cmd.encode())
            time.sleep(2)
            # receive power
            rv=self.s.recv(2048)
            # decode power
            rv=rv.decode()
           
            # try to float rv and round it
            try:
                self.Rv=float(rv)
                self.Rv=round(self.Rv,1)
            
            # except if rv is not a number, set it to a bogus number
            except ValueError:
                self.Rv=99.9
            
            # if there is no received power, set it to a bogus number
            if rv==(""):
                rv="99";
            
            try:
                # float received frequency
                self.RvF=float(self.rvf)/1000000.0
                # round received frequency
                self.RvF=round(self.RvF,3)
            except ValueError:
                self.RvF=99.9
  
            # if there is no received frequency, set it to a bogus number
            if self.rvf==(""):
                self.rvf="99";
            
            # print the power and frequency
            print("Pwr, Freq =",self.Rv,'\t',self.RvF)
            
            # radio button SpurNB is to find narrow band spurs and radio button SpurWB is wide band spurs
            if self.bits.rbtn_SpurNB.isChecked() or self.bits.rbtn_SpurWB.isChecked():
                delta=self.findSpurs()
            
            time.sleep(5)
            # set the row for frequency
            row=1        
            # write to xlsx file what row, column, and frequency 
            self.excelUtil.writeData(row,self.col,f2)
            # set the row for power
            row=2  
            #write to xlsx file what row, column, and frequency 
            self.excelUtil.writeData(row,self.col,self.RvF)
            
            # row 3 is the error of the frequency entered and what frequency acutally is put out
            row=3   
            if self.bits.cbox_Div64.isChecked()==True: 
                err=self.RvF-F
                # add 20 to compensate for attenuator at the output of the PLL frequency synth.
                self.Rv=20+self.Rv 
            if self.bits.cbox_Div64.isChecked()==False: 
                err=self.RvF-f2
                # add 30 to compensate for attenuator at the output of the PLL frequency synth.
                self.Rv=30+self.Rv 
            # write to the xlsx file the error
            self.excelUtil.writeData(row,self.col,err)
            # set row 4 for the received power
            row=4                          
            # write to the xlsx file the received power
            self.excelUtil.writeData(row,self.col,self.Rv)
            # set row 5 for the spurs 
            row=5
            if self.bits.rbtn_SpurNB.isChecked() or  self.bits.rbtn_SpurWB.isChecked():
                # if the absolute value of delta is greater than 1 write to the file delta
                if abs(delta)>1:
                    self.excelUtil.writeData(row,self.col,delta)
            # add another column
            self.col=self.col+1
            
            # repeat first freq read
            if count<1:
                self.f=minf
                self.col=1
               
            else:
                # add the stepsize to the frequency
                self.f += stepsize
                
            count=count+1
        print('Sweep Has Been Completed')
        
        # create the graph and then close the file
        self.excelUtil.createExcelChart()
        self.excelUtil.closeFile()
    
    def t_findBits(self):
        t = threading.Thread(target=self.findBits)
        t.start()          
    
    # set VCO frequency
    def findBits(self, frequency):      
        # get the frequency        
        Frequency = self.bits.ledit_freq.text()
        
        # change it to an integer
        frequency = int(Frequency)
        
        # 944 is subtracted from the frequency as a starting/reference point when all bits are set to 0, 944 is the minimum frequency of the PLL Frequency Synthesizer
        d=frequency - 944
        
        # this part is for programming the programmable divider
        self.TestA8b = d / 256
        done=False
        while(not done):         
            # if d/256 is greater than or equal to 1, set that bit to 1, subtract 256 from it and check the check box
            if d/256 >= 1:
                self.TestA8b  = 1
                d=d-256
                self.A8 = 1
                print("A8=",self.A8b)
                print("d=",d)
                self.bits.cbox_bit256.setChecked(True)
            else:
                # else keep the bit as 0
                print('Not A8')
                self.A8 = 0
            
            # if d/128 is greater than or equal to 1, set that bit to 1, subtract 128 from it and check the check box
            if d/128>= 1:
                self.TestA7b = 1               
                d=d-128
                self.A7 = 1
                print("A7=",self.A7b)   
                self.bits.cbox_bit128.setChecked(True)
            else:
                # else keep the bit as 0
                print('Not A7')
                self.A7 = 0
            
            # if d/64 is greater than or equal to 1, set that bit to 1, subtract 64 from it and check the check box    
            if d/64 >= 1:
                self.TestA6b = 1                
                d = d - 64
                self.A6 = 1
                print('A6=', self.A6b)
                self.bits.cbox_bit64.setChecked(True)
            else:
                # else keep that bit as 0
                print('Not A6')
                self.A6 =0
                
            # if d/32 is greater than or equal to 1, set that bit to 1, subtract 32 from it and check the check box    
            if d/32 >= 1:
                self.TestA5b = 1
                d = d - 32
                self.A5 = 1  
                print('A5=', self.A5b)  
                self.bits.cbox_bit32.setChecked(True)
            else:
                # else keep that bit as 0
                print('Not A5')
                self.A5 = 0
            
            # if d/16 is greater than or equal to 1, set that bit to 1, subtract 16 from it and check the check box    
            if d/16 >= 1:
                self.TestA4b = 1
                d = d - 16
                self.A4 = 1 
                print('A4=', self.A4b)
                self.bits.cbox_bit16.setChecked(True)
            else:
                # else keep that bit as 0
                print('Not A4')
                self.A4 =0
                
            # if d/8 is greater than or equal to 1, set that bit to 1, subtract 8 from it and check the check box
            if d/8 >= 1:
                self.TestA3b = 1
                d = d - 8
                self.A3 = 1
                print('A3=', self.A3b)
                self.bits.cbox_bit8.setChecked(True)
            else:
                # else keep that bit as 0
                print('Not A3')
                self.A3=0
                
            # if d/4 is greater than or equal to 1, set that bit to 1, subtract 4 from it and check the check box
            if d/4 >= 1:
                self.TestA2b = 1
                d = d - 4
                self.A2 = 1 
                print('A2=', self.A2b)
                self.bits.cbox_bit4.setChecked(True)
            else:
                # else keep that bit as 0
                print('Not A2')
                self.A2 =0
                
            # if d/2 is greater than or equal to 1, set that bit to 1, subtract 2 from it and check the check box            
            if d/2 >= 1:    
                self.TestA1b = 1
                d = d - 2
                self.A1 = 1 
                print('A1=', self.A1b)
                self.bits.cbox_bit2.setChecked(True)
            else:           
                # else keep that bit as 0
                print('Not A1')
                self.A1= 0
            
            # if d/1 is greater than or equal to 1, set that bit to 1, subtract 1 from it and check the check box
            if d/1 >= 1:
                self.TestA0b = 1
                d = d - 1    
                self.A0 = 1
                print('A0=', self.A0b)
                self.bits.cbox_bit1.setChecked(True)
            else:
                # else keep that bit as 0
                print('Not A0')   
                self.A1=0
                
            print("RPI freq=",Frequency)           
            
            # send to RP2040 the frequency
            self.connector_SerialPort.send_to_microcontroller(Frequency)
            done=True
        
    def setFrequency(self, frequency):              
        Frequency = int(frequency)
            
        d=frequency - 944
        
        
        self.TestA8b = d / 256
        done=False
        while(not done):         
            
            if d/256 >= 1:
                
                d=d-256
                self.A8 = 1
                print("A8=",self.A8b)
                print("d=",d)
                self.bits.cbox_bit256.setChecked(True)
            else:
                print('Not A8')
                self.A8=0
                
            if d/128>= 1:
                self.TestA7b = 1               
                d=d-128
                self.A7 = 1
                print("A7=",self.A7b)   
                self.bits.cbox_bit128.setChecked(True)
            else:
                print('Not A7')
                self.A7=0
            if d/64 >= 1:
                self.TestA6b = 1                
                d = d - 64
                self.A6 = 1
                print('A6=', self.A6b)
                self.bits.cbox_bit64.setChecked(True)
            else:
                print('Not A6')
                self.A6=0
            if d/32 >= 1:
                self.TestA5b = 1
                d = d - 32
                self.A5 = 1  
                print('A5=', self.A5b)  
                self.bits.cbox_bit32.setChecked(True)
            else:
                print('Not A5')
                self.A5=0
                
            if d/16 >= 1:
                self.TestA4b = 1
                d = d - 16
                self.A4 = 1 
                print('A4=', self.A4b)
                self.bits.cbox_bit16.setChecked(True)
            else:
                print('Not A4')
                self.A4=0
            if d/8 >= 1:
                self.TestA3b = 1
                d = d - 8
                self.A3 = 1
                print('A3=', self.A3b)
                self.bits.cbox_bit8.setChecked(True)
            else:
                print('Not A3')
                self.A3=0
            if d/4 >= 1:
                self.TestA2b = 1
                d = d - 4
                self.A2 = 1 
                print('A2=', self.A2b)
                self.bits.cbox_bit4.setChecked(True)
            else:
                print('Not A2')
                self.A2=0
            if d/2 >= 1:    
                self.TestA1b = 1
                d = d - 2
                self.A1 = 1 
                print('A1=', self.A1b)
                self.bits.cbox_bit2.setChecked(True)
            else:                
                print('Not A1')
                self.A1=0
                
            if d/1 >= 1:
                self.TestA0b = 1
                d = d - 1    
                self.A0 = 1
                print('A0=', self.A0b)
                self.bits.cbox_bit1.setChecked(True)
            else:
                print('Not A0')  
                self.A0=0
                
            print(Frequency)           
            
            # send to RP2040
            self.connector_SerialPort.send_to_microcontroller(Frequency)
            done=True              
            
if __name__=='__main__':
    
    app=qtw.QApplication([])
    
    widget=Main()
    widget.show()
    

    
    app.exec_()