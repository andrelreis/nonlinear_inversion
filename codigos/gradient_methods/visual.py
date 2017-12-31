# -*- coding: utf-8 -*-
"""
Created on Sat Feb 21 03:35:33 2015

@author: Marlon
"""

#histogram equalization of the data for viazualization
def histeq(data):
    from numpy import histogram, interp, max, size, sqrt
    nbins=int(sqrt(size(data)))   
    # Histogram
    hist,bins = histogram(data.flatten(),nbins,normed=True)
    cdf = hist.cumsum() # Cumulative distribution function
    cdf = max(data) * cdf / cdf[-1] # Normalize
    #interpolation
    return interp(data.flatten(),bins[:-1],cdf).ravel()   

