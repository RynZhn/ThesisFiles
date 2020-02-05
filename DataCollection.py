import serial
import csv
import datetime 
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('serPort', type = int, 
    help='the serial adress 1 refers to port 1 2 to port 2')

args = parser.parse_args()
#Grab today's date and create a file using it.
today = datetime.datetime.now()
filename = str(today).replace(" ","_")
filename = filename.replace(':','_')
filename = filename.replace('.','_')

dataFile = open(filename+'.txt',"w")

serialAddress = ""
if(args.serPort == 1):
    serialAddress = "/dev/ttyUSB1"
elif(args.serPort ==2):
    serialAddress = "/dev/ttyUSB2"

#open serial connection.
ser = serial.Serial("/dev/ttyUSB1") #Remember to put in the address.
ser.open()
ser.reset_input_buffer() #might also be:
#ser.flushInput()

while True:
    if(ser.in_waiting() > 0):
        data = ser.readLine()
        dataFile.write(str(data))
        print("Wrote a line!")


