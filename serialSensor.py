import serial
import string
import time

# Open serial port
ser=serial.Serial('/dev/ttyACM0',115200)


while True:
    serialdata=ser.readline()
    print(serialdata)

