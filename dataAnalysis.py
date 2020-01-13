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
#Getting the power spectra

#for each set of data take the fft and add it to the average
PSAveX = np.empty(1024)
count = 0 #Number of valid power spectrum calculations that we can average. 
for xset in xacel:
    #for every set of data, calculate the power spectra
    #when calculating the power spectra, find the average of the set and remove it
    mean = sum(xset)/len(xset)
    xset = [x-mean for x in xset]
    psx = np.abs((fft.fft(xset)))**2
    # we only want sets of data that we can average so check their lengths
    if len(psx) == 1024:
        #if this set has the right length, add it to the overal power spectra list to be averaged
        i = 0
        for val in psx:

            PSAveX[i] = val
            i += 1
        #increment count to keep track of how many valid power spectra there are
        count += 1
        #calc the frequency bins using only valid datasets
        #the current placement of this isnt optimal but what are you going to do?
    
        freq = fft.fftfreq(len(xset),d=.02)
print(count)
"""     if len(psx) == 1024:
        i = 0
        for val in psx:
            PSAveX[i] += val
            i += 1
        count += 1 """
PSAveX = [x/count for x in PSAveX]

#PSAveX = [x/count for x in PSAveX]
plt.figure(0)
""" freq = fft.fftfreq(len(xacel[2]),d=.02) """
plt.plot(freq,PSAveX)

plt.figure(5)
[ps1,freq1] = CalcPowerSpec(xacel[200],.02)
plt.plot(freq1,ps1)

plt.figure(6)
psx2= np.abs((fft.fft(xacel[200])))**2
freq = fft.fftfreq(len(xacel[200]),d=.02)
plt.plot(freq,psx2)

""" plt.figure(1)
#Use numpy's libraries to calculate the FFT and then squre it to get the pwoer spectra.
#psx = np.abs((fft.fft(xacel[316])))**2
freq = fft.fftfreq(len(xacel[2]),d=.02)
plt.plot(freq,PSAveX)
print(len(psx))
 """
#create power spectrum for y axis.
plt.figure(2)
psy = np.abs((fft.fft(yacel[2])))**2
plt.plot(freq,psy)

#create power spectrum for z axis. 
"""
because the z axis has a 1 unit bias due to gravity, the FFT has a huge 0
value. To counter this, remove 1 from the dataset.

"""
zacel[2] = [x-1 for x in zacel[2]]
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