''' The purpose of this script is to plot the raw data 
of an entire dataset.'''

import matplotlib.pyplot as plt
import numpy.fft as fft
import numpy as np
import os

# create a list for the different acceleration data
xacel, yacel, zacel = [],[],[]
rotorSpeed = []

file = "..\Data\\7-23-2020\80rpm\Test-80rpm-100g-7-23-2020.txt"

data_file = open(file,"r")

# Variables to keep track of which data set we're on and which line of data
dataSet = 0 

# read through each line in the file
for line in data_file:
    
    
    if(line[0]=='~'):
        try:
            #if there's a short line of data due to erroneous data collection
            #then let us know
            xacel.append((float)(line.split(",")[1])/(16*1024))
            yacel.append((float)(line.split(",")[2])/(16*1024))
            zacel.append((float)(line.split(",")[3])/(16*1024))
            rotorSpeed.append((float)(line.split(",")[4])/(16*1024))
        except IndexError:
            print("Had an index error in dataset: ",dataSet)
        except ValueError:
            print("Had a value error in dataset: ",dataSet)


data_file.close()

##################################### GENERATE PLOTS
fig1 = plt.figure(1)
fig1.suptitle("Acceleration Response X")
plt.ylabel("Magnitude [g's]")
plt.xlabel("Index")
plt.plot(xacel)

fig2 = plt.figure(2)
fig2.suptitle("Averaged Power Spectrum for Y")
plt.ylabel("Magnitude [g's]")
plt.xlabel("Index")
plt.plot(yacel)


fig3 = plt.figure(3)
fig3.suptitle("Averaged Power Spectrum for Z")
plt.ylabel("Magnitude [g's]")
plt.xlabel("Index")
plt.plot(zacel)


plt.show()