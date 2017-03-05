# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 13:53:19 2017

@author: Steve
"""

## Freq Dist Tools

import nltk


def filterFd(freqDist, start=None, end=None):
    """
    takes an nltk.FreqDist object and filters it to provide words that
    have the given range of occurences
    """
    
    try:
        return list(filter(lambda x: x[1] <= end and x[1] >= start,fd.items()))
    except:
        raise ValueError("Must give two values, a start and an end, for single values use filterFd(freqDist, 20, 20) ")
        
#---------------------------------------------   
f = r'D:\Data\Subs\24\24.1x02.1am-2am.DVDRip.XViD-FoV.EN.srt'

from srtTools import srtTokens

fd = nltk.FreqDist(srtTokens(f)) 
filterFd(fd, 19, 25)
#----------------------------------------------

from srtTools import dirParse

root = r'D:\Data\Subs\24'
season1_tokens = dirParse(root, tokens2=True, flat=True)
fd = nltk.FreqDist(season1_tokens)
filterFd(fd, 300, 350)
#===========================================

