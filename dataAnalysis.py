import matplotlib.pyplot as plt
import numpy.fft as fft
import numpy as np
import os

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
#Getting the power spectra

#The following commented code is wrong. I'm not sure why buy it returns a power spectra with negative values which is impossible
""" plt.figure(1)
sp = (fft.rfft(xacel[2]))**2
freqrange = np.linspace(0, 50/2, len(sp))
plt.plot(freqrange,sp)
 """
plt.figure(1)
#Use numpy's libraries to calculate the FFT and then squre it to get the pwoer spectra.
psx = np.abs((fft.fft(xacel[2])))**2
freq = fft.fftfreq(len(xacel[2]),d=.02)
plt.plot(freq,psx)

#create power spectrum for y axis.
plt.figure(2)
psy = np.abs((fft.fft(yacel[2])))**2
plt.plot(freq,psy)

#create power spectrum for z axis. 
plt.figure(3)
psz = np.abs((fft.fft(zacel[2])))**2
plt.plot(freq,psz)

plt.figure(4)
plt.plot(zacel[2])
plt.show()



"""
The result of this power spectrum has some kind of artefact where there's a huge spike 
in the begining. I remember that there was a reason for this but I need to find where 
I read it. I believe it has something to do with the phase of the signal?
"""