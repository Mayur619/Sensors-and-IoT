# vcc trig- out  echo- in  gnd

import time
import RPi.GPIO as GPIO

def measure():
  # This function measures a distance
  GPIO.output(GPIO_TRIGGER, True)
  time.sleep(0.00001)
  GPIO.output(GPIO_TRIGGER, False)
  start = time.time()

  while GPIO.input(GPIO_ECHO)==0:
    start = time.time()

  while GPIO.input(GPIO_ECHO)==1:
    stop = time.time()

  elapsed = stop-start
  distance = (elapsed * 34300)/2

  return distance

def measure_average():
  # This function takes 3 measurements and
  # returns the average.
  distance1=measure()
  time.sleep(0.1)
  distance2=measure()
  time.sleep(0.1)
  distance3=measure()
  distance = distance1 + distance2 + distance3
  distance = distance / 3
  return distance

GPIO.setmode(GPIO.BCM)

# Define GPIO to use on Pi
GPIO_TRIGGER = 23
GPIO_ECHO    = 24

print("Ultrasonic Measurement")

# Set pins as output and input
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  # Trigger
GPIO.setup(GPIO_ECHO,GPIO.IN)      # Echo
GPIO.setup(12,GPIO.OUT)

# Set trigger to False (Low)
GPIO.output(GPIO_TRIGGER, False)

try:
  while True:
   # g.setup(36,g.OUT)
    distance = measure_average()    
    print("Distance : %.1f" % distance)
    if distance < 10:
        GPIO.output(12,True)
        time.sleep(0.5)
        GPIO.output(12,False)
        time.sleep(0.5)

except KeyboardInterrupt:
  GPIO.cleanup()
