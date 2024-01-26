# RaspberryPi-RP2040
This program is for controlling frequency of PLL Frequency Synthesizer.
For this program to work, you need to load micropython on an RP2040 microcontroller, then save "serverForVcoClient.py" onto the RP2040.
Next, connect the RP2040 based device to a USB port of a Raspberry Pi, then go to, either, PuTTY and open /dev/ttyACM0, run the command execFile("serverForVcoClient.py"), or open Thonny, and select the interpreter to MicroPython (Raspberry Pi Pico), and run serverForVcoClient.py.

To connect a RIGOL DSA832 Spectrum Analyzer for the program, go to the upper right corner of the GUI, where it says "Connect to DSA832E", enter the IP, Port, and press the button "connect". When you press "connect" it creates a socket server, from there you can do the sweep, and then the options of div 64, NB spurs, WB spurs, set the center frequency, and set the span.

Now open a python IDE, and run main.py, from there, you can set the fixed frequency, if you are using the RIGOL DSA832E (I'm not sure if all DSA800 series Spectrum Analyzer work with this program), it will set the center frequency so the frequency you entered will be in the center. If you want to sweep you will have to have DSA832E Spectrum Analyzer connected, also, you have the choice of having the Divide by 64, Narrow Band Spurs, and Wide Band Spurs, in the Sweep options. Through out the sweep, the signal will always be in the center of the Spectrum Analyzer.

During the sweep, div 64, NB Spurs, WB Spurs, will be written to an xlsx file, the xlsx file will write the results of the sweep. In the xlsx file it will have 5 things, a row for the frequency entered, row for frequency read, row for the error, row for the power, and a graph of the results.

When the xlsx file is writen, it will have a time stamp of when it was written, and also will be written to the directory, the user sets it to.

To clone this repository, copy: git clone https://github.com/Alex-Czerniewski/RaspberryPi-RP2040.git
