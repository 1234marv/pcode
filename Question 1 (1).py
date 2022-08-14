#!/usr/bin/env python
# coding: utf-8

# In[47]:


import random
import numpy as np
import matplotlib.pyplot as plt
import time
import datetime
from scipy.stats import norm


def WichmanHill():
    s1 = random.randint(1, 30000)
    s2 = random.randint(1, 30000)
    s3 = random.randint(1, 30000)

    s1 = 171 * (s1 % 177) - (2*(s1/177))
    
    if s1 < 0:
        s1 = s1 + 30269

    s2 = 172 * (s2 % 176) - (35*(s2/176))
    if s2 < 0:
        s2 = s2 + 30307

    s3 = 170 * (s3 % 178) - (63*(s2/178))
    if s3 < 0:
        s3 = s3 + 30323

    temp = s1/30269.0 + s2/30307.0 + s3/30323.0
    
    return (temp % 1.0) 
    
def plotPDFofGenerator(sampleSpace, binSize):

        
    fig = plt.figure()
    plt.ylabel("Probability Density")
    plt.xlabel("Random Number")
    plt.title("PDF of Wichmann-Hill random number generator")
    plt.hist(sampleSpace, bins = binSize, density = True)
    
    fig = plt.figure()
    
    data = np.random.uniform(0,1,len(sampleSpace))
    plt.hist(data, bins = binSize, density = True, color = "green")
    plt.ylabel("Probability Density")
    plt.xlabel("Random Number")
    plt.title("PDF of Python random number generator")


def simulateQ1(sampleSize, binSize):
    
    sampleSpace = []

    
    for x in range(0, sampleSize):
        sampleSpace.append(WichmanHill())

    plotPDFofGenerator(sampleSpace, binSize)
    
    
    print("The mean of the Wichman-Hill random number generator is: " + str(np.mean(sampleSpace)))
    print("The variance of the Wichman-Hill random number generator is: " + str(np.var(sampleSpace)))
    print("The standard deviation of the Wichman-Hill random number generator is: " + str(np.std(sampleSpace)))


    
simulateQ1(100000,250)


# In[53]:




