import matplotlib.pyplot as plt
import numpy.fft as fft
import numpy as np
import os
import seaborn as sb
from PowerSpectrumLib import CalcPowerSpec, CalcBiSpec, ReadMatlabFile

# create a list for the different accelleration data
xacel, yacel, zacel = [[]],[[]],[[]]

#list for the rotor speed data
rotorspeed = [[]]

# read the data file
data_file = open("..\Data\\7-23-2020\80rpm\Test-80rpm-100g-7-23-2020.txt","r")

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
        except ValueError:
            print("Had a value error in dataset: ",dataSet)




data_file.close()

print("Total amount of data sets: ",dataSet)

CalcBiSpec(xacel[2])

startIndex,endIndex = input("Enter which data sets you would like to get the PS [ x , y ] (sets x to y) ").split(",")

startIndex = int(startIndex)
endIndex = int(endIndex)

#try and average the above power spectrums
validSets = 0 #keeps track of the number of valid data sets so we know how to average
PSXAve = [0]*1024
PSYAve = [0]*1024
PSZAve = [0]*1024

currentIndex = startIndex
for i in range(startIndex,endIndex+1):
    [psx,freqx] = CalcPowerSpec(xacel[i],.02)                             #get the power spectrum
    [psy,freqy] = CalcPowerSpec(yacel[i],.02)
    [psz,freqz] = CalcPowerSpec(zacel[i],.02)
    if len(psx) == 1024 and len(psy) == 1024 and len(psz) == 1024:        #check to see if power spectrum is valid length
        validSets += 1                                                      #if it is, incrememnt the count
        PSXAve = [x + y for x,y in zip(PSXAve,psx)]                      #and add the new ps to the total sum
        PSYAve = [x + y for x,y in zip(PSYAve,psy)]  
        PSZAve = [x + y for x,y in zip(PSZAve,psz)]  
        freq = freqz
    else:
        print("Bad length at index: ",currentIndex)
    currentIndex += 1
PSXAve = [x/validSets for x in PSXAve]                                      #divide each element by the total amount to get the average
PSYAve = [x/validSets for x in PSYAve]
PSZAve = [x/validSets for x in PSZAve]

####################################### MATLAB SECTION
# Read matlab file and calculate the power spectrum
matlabSignalDS = ReadMatlabFile("..\Data\SimulationOutput_Downsampled.txt")
[psmatlabDS, freqmatlabDS]=CalcPowerSpec(matlabSignalDS,.02)

fig1 = plt.figure(7)
fig1.suptitle("Powerspectrum of MATLAB Simulation (Downsampled)")
plt.ylabel("Magnitude")
plt.xlabel("Frequency [hz]")
plt.plot(freqmatlabDS,psmatlabDS)

matlabSignal = ReadMatlabFile("..\Data\SimulationOutput.txt")
[psmatlab, freqmatlab]=CalcPowerSpec(matlabSignal,.00001)

fig1 = plt.figure(8)
fig1.suptitle("Powerspectrum of matlab simulation")
plt.ylabel("Magnitude")
plt.xlabel("Frequency [hz]")
plt.plot(freqmatlab,psmatlab)

###################################### REAL DATA
fig1 = plt.figure(1)
fig1.suptitle("Averaged Power Spectrum for X")
plt.ylabel("Magnitude")
plt.xlabel("Frequency [hz]")
plt.plot(freq[0:511],PSXAve[0:511])

fig2 = plt.figure(2)
fig2.suptitle("Averaged Power Spectrum for Y")
plt.ylabel("Magnitude")
plt.xlabel("Frequency [hz]")
plt.plot(freq[0:511],PSYAve[0:511])


fig3 = plt.figure(3)
fig3.suptitle("Averaged Power Spectrum for Z")
plt.ylabel("Magnitude")
plt.xlabel("Frequency [hz]")
plt.plot(freq[0:511],PSZAve[0:511])


###################################### BISPECTRUM

bispec = CalcBiSpec(yacel[5])
print(len(bispec))
for i in bispec:
    if len(i) != 256:
        print(len(i))
plt.figure(9)
heatmap,ax = sb.heatmap(bispec)
heatmap.set(xlim=(0,25),ylim=(0,25))
ax.set
# fig, ax = plt.subplots()

# im = ax.imshow(bispec)

plt.show()
