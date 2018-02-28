import RPi.GPIO as g
import time

g.setmode(g.BOARD) #BCM
g.setup(40,g.OUT)

while True:
    g.output(40,True)
    time.sleep(0.05)
    g.output(40,False)
    time.sleep(0.05)
    
