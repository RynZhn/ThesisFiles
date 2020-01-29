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
    len(transform)