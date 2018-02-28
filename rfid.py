import serial as s
import time as t

def readcard():
    data=s.Serial("/dev/ttyUSB0",9600,timeout=1) #tty ports(speed of transmission - 9600) , ttyUSB0 appears rfid reader is connected 
    x=data.readline()
    print (x)
    #if x == "":
     #   print("")
    
while True:
    readcard()
