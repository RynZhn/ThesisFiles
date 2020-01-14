import matplotlib.pyplot as plt
import numpy.fft as fft
import numpy as np
import os

from PowerSpectrumLib import CalcPowerSpec

# create a list for the different accelleration data
xacel, yacel, zacel = [[]],[[]],[[]]

#list for the rotor speed data
rotorspeed = [[]]

# read the data file
data_file = open("../Data/wind-vibes-2019-Nov-5.txt","r")

# Variables to keep track of which data set we're on and which line of data
dataSet = 0 

# read through each line in the file
for line in data_file:
    
    if(line[0]=='$'):
        dataSet += 1
        xacel.append([])
        yacel.append([])
        zacel.append([])
        rotorspeed.append([])
    elif(line[0]=='~'):
        try:
            #if there's a short line of data due to erroneous data collection
            #then let us know
            xacel[dataSet].append((float)(line.split(",")[1])/(16*1024))
            yacel[dataSet].append((float)(line.split(",")[2])/(16*1024))
            zacel[dataSet].append((float)(line.split(",")[3])/(16*1024))
            rotorspeed[dataSet].append((float)(line.split(",")[4])/(16*1024))
        except IndexError:
            print("Had an index error in dataset: ",dataSet)



data_file.close()

print("Total amount of data sets: ",dataSet)

startIndex,endIndex = input("Enter which data sets you would like to get the PS [ x , y ] (sets x to y) ").split(",")

startIndex = int(startIndex)
endIndex = int(endIndex)

#try and average the above power spectrums
validSets = 0 #keeps track of the number of valid data sets so we know how to average
PSXAve = [0]*1024
currentIndex = startIndex
for dataSet in xacel[startIndex:endIndex]:
    [ps,freq] = CalcPowerSpec(dataSet,.02)                             #get the power spectrum
    if len(ps) == 1024:                                                 #check to see if power spectrum is valid length
        validSets += 1                                                      #if it is, incrememnt the count
        PSXAve = [x + y for x,y in zip(PSXAve,ps)]                      #and add the new ps to the total sum
    else:
        print("Bad length for index: ",currentIndex)
    currentIndex += 1
PSXAve = [x/validSets for x in PSXAve]                                      #divide each element by the total amount to get the average


plt.figure(5)
plt.plot(freq,PSXAve)

plt.show()
