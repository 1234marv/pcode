#!/usr/bin/env python
# coding: utf-8

# In[94]:


import random
import numpy as np
import matplotlib.pyplot as plt
import time
import datetime
from scipy.stats import norm


# In[195]:


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


# In[ ]:





# In[196]:


def gaussian(mean = 0, stdDeviation = 1):
    s = 1.0
    
    while( s >= 1 ):

        temp1 = 2*random.random() -1
        temp2 = 2*random.random() -1
        
        s = (temp1**2) + (temp2 **2)

    temp3 = np.sqrt(-2.0*np.log(s)/s)

    return (stdDeviation * temp1 * temp3)


# In[15]:


# print(np.round(0.50))


# In[197]:


# Question 3.1
def generateBits(numOfBits):
    bits = []
    for i in range(0, numOfBits):
        bit = WichmannHill()
        if(bit < 0.5):
            bits.append(0)
        else:
            bits.append(1)
    return bits


# In[198]:


# Question 3.2
def BPSKModulationMap(bit):
    to_return = None
    if(bit == 1):
        to_return = 1
    elif(bit == 0):
        to_return = -1
        
    return to_return
    
    
    
def BPSK_map_bits_to_symbols(OGBits):
    mappedBitsToSymbols = []
    for i in range(0, len(OGBits)):
        mappedBitsToSymbols.append(BPSKModulationMap(OGBits[i]))
#     print(mappedBitsToSymbols)
    return mappedBitsToSymbols


# In[199]:


# Question 3.3

def stdCalc(SNR, fbit):
    return 1/np.sqrt(np.power(10,SNR/10) * 2 *fbit)



def addNoise(SNR, symbols,noise):
#     rk = sk + nk , sk = kth symbol, nk = std * gaussian
    r = []
    
    std = stdCalc(SNR, 1)

    
    for k in range(0, len(symbols)):
        nk = noise[k] * std
        rk = symbols[k] +  nk
        r.append(rk)
        
    return r


# In[200]:


# ****** Question 3.4 *****
def constellation_mapping(symbols):
    detected_symbols = []
    for i in range(0, len(symbols)):  
        if(symbols[i] > 0):
            detected_symbols.append(1)
        elif(symbols[i] < 0):
            detected_symbols.append(-1)
    return detected_symbols


# In[201]:


# Question 3.5
def convert_symbol_to_bits(symbols):
    final_bits = []
    for i in range(0, len(symbols)):
        if(symbols[i] == 1):
            final_bits.append(1)
        else:
            final_bits.append(0)
    return final_bits


# In[202]:


# Question 3.6 compare transmitted bits to received bits and count the bit errors

def gaussianNoise(n):
    nums = []
    for i in range(0,n):
        nums.append(gaussian())
    return nums

noise = gaussianNoise(10000)

def q3():
    random_bits = generateBits(10000)
    

    
    BERs = []
    for SNR in range(-4,9):
        
        bits_to_send_to_symbol = BPSK_map_bits_to_symbols(random_bits)


        r = addNoise(SNR, bits_to_send_to_symbol,noise)


        received_symbols = constellation_mapping(r)


        received_bits = convert_symbol_to_bits(received_symbols)
        
        errors = 0

        for i in range(0, len(random_bits)):
            if(random_bits[i] != received_bits[i]):
                errors += 1

        BER = errors / len(random_bits)
        BERs.append(BER)        
    
    plotq3(BERs)
    
def plotq3(BERs):
    SNR = np.linspace(-4,8,13)
    fig = plt.figure()
    plt.semilogy(SNR, BERs)
    plt.title("A graph of BER vs Eb/No")
    plt.xlabel("Eb/No")
    plt.ylabel("BER")
    plt.show


# In[203]:


q3()


