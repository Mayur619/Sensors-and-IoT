import serial

def LocalTime(time):
        h1=int(time[0:2])+5
        m1=int(time[2:4])+30
        if m1>60:
                h1+=1
                m1-=60
        print "IST:",h1%12,":",m1,":",time[4:]

def read():
	gps=serial.Serial("/dev/ttyACM0",9600,timeout=1)
	x=gps.readline()
	y=x.split(",")
#	print x , "\n", y , "\n" 
	
	if y[0]=="$GPRMC":
	   if y[2]=="A":
	      print "GMT", y[1][0:2], ":", y[1][2:4], ":",y[1][4:]
	      LocalTime(y[1])
	      print "latitude:" ,y[3][0:2],"*",y[3][2:4],"'",y[3][4:],"\""
	      print "longitude:",y[5][0:2],"*",y[5][2:4],"'",y[5][4:],"\""
	      print "date", y[9][0:2], "/", y[9][2:4], "/",y[9][4:],"\n"
	      

while True:
	read()
