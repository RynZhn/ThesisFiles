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

def CalcBiSpec (dataArray,dataRate):
    """ This function removes the mean of the data set and 
    calculates the bispectrum and puts it into an array.
    Output should be just an array."""
    mean = sum(dataArray)/len(dataArray)
    correctedArray = [x-mean for x in dataArray]
    transform = fft.fft(correctedArray)
    biSpecArray = [[]]
    for f1 in range(len(transform)/2):
        for f2 in range(len(transform)/2):
            biSpecArray[f1].append(transform(f1)*transform(f2)*transform(f1+f2+512))