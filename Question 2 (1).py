#!/usr/bin/env python
# coding: utf-8

# In[33]:


import random
import math
import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt
import time
import datetime
from scipy.stats import norm


# In[70]:


def gaussian(mean = 0, stdDeviation = 1):
    s = 1.0
    
    while( s >= 1 ):

        temp1 = 2*random.random() -1
        temp2 = 2*random.random() -1
        
        s = (temp1**2) + (temp2 **2)

    temp3 = np.sqrt(-2.0*np.log(s)/s)

    return (stdDeviation * temp1 * temp3)


# In[71]:


def plotPDFofGenerator(sampleSpace, binSize):
    
    fig = plt.figure()
    plt.ylabel("Probability Density")
    plt.xlabel("Random Number")
    plt.title("PDF of Gaussian random number generator")
    plt.hist(sampleSpace, bins = binSize, density = True)
    
    fig = plt.figure()
    
    mu = 0
    variance = 1
    sigma = math.sqrt(variance)
    x = np.linspace(mu - 4*sigma, mu + 4*sigma, 100)
    plt.ylabel("Probability Density")
    plt.xlabel("Random Number")
    plt.title("PDF of Gaussian random number generator")
    plt.plot(x, stats.norm.pdf(x, mu, sigma))


# In[72]:


def simulateQ2(sampleSize=10000000, binSize=200,):
    sampleSpace = [] 

    for x in range(0, sampleSize):
        sampleSpace.append(gaussian())
    
    plotPDFofGenerator(sampleSpace, binSize)

    print("The mean of the Gaussian random number generator is: " + str(np.mean(sampleSpace)))
    print("The variance of the  Gaussian number generator is: " + str(np.var(sampleSpace)))
    print("The standard deviation of the Gaussian random number generator is: " + str(np.std(sampleSpace)))


# In[73]:


simulateQ2(1000000,200)

