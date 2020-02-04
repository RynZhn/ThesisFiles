import serial
import csv
import datetime 

#Grab today's date and create a file using it.
today = datetime.datetime.now()
filename = str(today).replace(" ","_")
filename = filename.replace(':','_')
filename = filename.replace('.','_')

dataFile = open(filename+'.txt',"w")

#open serial connection.
ser = serial.Serial() #Remember to put in the address.
ser.open()
ser.reset_input_buffer() #might also be:
#ser.flushInput()

while True:
    if(ser.in_waiting() > 0):
        data = ser.readLine()
        dataFile.write(str(data))


