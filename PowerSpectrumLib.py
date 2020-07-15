import numpy.fft as fft
import numpy as np

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

def CalcBiSpec (dataArray):
    """ This function removes the mean of the data set and 
    calculates the bispectrum and puts it into an array.
    Output should be just an array."""
   
   
    mean = sum(dataArray)/len(dataArray)
    correctedArray = [x-mean for x in dataArray]
    transform = fft.fft(correctedArray)
    biSpecArray = [[]]
    print( range(int(len(transform))) )
    for f1 in range(int(len(transform)/4)):
        for f2 in range(int(len(transform)/4)):
            biSpecArray[f1].append(transform[f1].real*transform[f2].real*np.conjugate(transform[f1+f2]).real)
        biSpecArray.append([])
    del biSpecArray[-1]
    return biSpecArray

def ReadMatlabFile(address):
    ''' This function will read the output of the TowerModel MATLAB 
    script and process it in a way that is similar to the real lfie 
    data.'''

    with open(address,'r') as towerData:
        outputList = towerData.read().splitlines()
    outputList = [float(x) for x in outputList]
    return outputList