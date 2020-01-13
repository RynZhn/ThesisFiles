import matplotlib.pyplot as plt
import numpy.fft as fft
import numpy as np
import os

def CalcPowerSpec (dataArray,dataRate):
    """ This function removes a fixed bias from the data
    and calculates the power spectrum and frequency range of the dataset.
    The output is two arrays. Input is data array and time between datapoints
    """
    mean = sum(dataArray)/len(dataArray)
    correctedArray = [x-mean for x in dataArray]
    ps = np.abs((fft.fft(correctedArray)))**2
    freq = fft.fftfreq(len(correctedArray),d=dataRate)
    return [ps,freq]


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

print("Total amount of data sets: ",dataSet+1)


plt.figure(3)
[ps1,freq1] = CalcPowerSpec(xacel[300],.02)
plt.plot(freq1,ps1)

plt.figure(1)
[ps2,freq] = CalcPowerSpec(xacel[113],.02)
plt.plot(freq,ps2)

plt.figure(2)
[ps3,freq1] = CalcPowerSpec(xacel[7],.02)
plt.plot(freq1,ps3)

psAve = [(x + y + z)/3 for x,y,z in zip(ps3,ps1,ps2)]
plt.figure(4)
plt.plot(freq1,psAve)


#try and average the above power spectrums
validSets = 0 #keeps track of the number of valid data sets so we know how to average
PSXAve = [0]*1024
for dataSet in xacel:
    [ps,freq] = CalcPowerSpec(dataSet,.02)                             #get the power spectrum
    if len(ps) == 1024:                                                 #check to see if power spectrum is valid length
        validSets += 1                                                      #if it is, incrememnt the count
        PSXAve = [x + y for x,y in zip(PSXAve,ps)]                      #and add the new ps to the total sum

PSXAve = [x/validSets for x in PSXAve]                                      #divide each element by the total amount to get the average


plt.figure(5)
plt.plot(freq1,PSXAve)
plt.show()