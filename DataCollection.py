import serial
import csv
import datetime 
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('serPort', help='the serial adress 1 refers to port 1 2 to port 2')

args = parser.parse_args()
#Grab today's date and create a file using it.
today = datetime.datetime.now()
filename = str(today).replace(" ","_")
filename = filename.replace(':','_')
filename = filename.replace('.','_')


#open serial connection.
ser = serial.Serial(arg.SerPort) #Remember to put in the address.
ser.open()
ser.reset_input_buffer() #might also be:
#ser.flushInput()

dataFile = open()
with open(filename+'.txt',"w") as textfile:
#serialAddress = arg.serPort
    while True:
        if(ser.in_waiting() > 0):
            data = ser.readLine()
            dataFile.write(str(data))
            print("Wrote a line!")
            #I'm not sure what the end of line char is so I'm just going to write a line after
            if data[0]=='$':
                dataFile.write(str(today)+'\n') #write time stamp
                print("Wrote Time Stamp")
            


