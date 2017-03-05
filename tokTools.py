# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 14:05:53 2017

@author: Steve
"""

#===========================================

## Contains tools that can be carried out
# upon tokens


import nltk



def contentFraction(tokens):
    """Given a list of tokens, this function will give a fraction of words in the list 
    of tokens that are not common stopwords
    
    Usage:
        content_fraction(txtObject)
    """
    stopwords = nltk.corpus.stopwords.words('english')
    content = [w for w in tokens if w.lower() not in stopwords]
    return len(content)/len(tokens)
    
#------------------------------------------------------------
f = r'D:\Data\Subs\24\24.1x02.1am-2am.DVDRip.XViD-FoV.EN.srt'

from srtTools import srtTokens

tokens = srtTokens(f)

contentFraction(tokens)
#---------------------------------------------------

#============================================================
def frequentWords(tokens, n):
    """This function finds the most frequent n
    words in a list of tokens after stripping non-alpha
    words and removing stopwords
    
    Usage: frequentWords(tokens, 50)
    
    returns: A list of the top 50 words and their frequencies
    """
    
        
    stpwords = nltk.corpus.stopwords.words('english')
 
    content = [w for w in tokens if w.lower() not in stpwords and w.isalpha()]
    
    fdist = nltk.FreqDist(content)
    top = fdist.most_common(n)
    return top   
   
#---------------------------------------------------
f = r'D:\Data\Subs\24\24.1x02.1am-2am.DVDRip.XViD-FoV.EN.srt'

from srtTools import srtTokens

tokens = srtTokens(f)

frequentWords(tokens, 20)
#-----------------------------------------------------

#==============================================================

def unusualWords(tokens):
    """
    Finds the unusual words in a text obj
    
    Uses nltk.corpus.words.words() as a comparison tool
        
        
    Outputs: A list of words deemed unusual, sorted
    """
    text_vocab = set(w.lower() for w in tokens if w.isalpha())
    english_vocab = set(w.lower() for w in nltk.corpus.words.words())
    unusual = text_vocab - english_vocab
    return sorted(unusual)

#-----------------------------------------------------
root = r'D:\Data\Subs\24'

from srtTools import dirParse

tokens = dirParse(root, tokens2=True, flat=True)

unusualWords(tokens)
#-----------------------------------------------------

#======================================================

def frequentBigrams(tokens, n):
    """
    This function outputs the n most frequent bigrams from a list of tokens
    
    Usage: frequentBigrams(tokens, n)
    
    Returns: list of the n most frequent bigrams
    """
    
    from nltk import bigrams
    
    
    stopwords = nltk.corpus.stopwords.words('english')
    
    content = [w for w in tokens if w.lower() not in stopwords and w.isalpha()]
        
    
    bigrams = list(bigrams(content))
    fdist = nltk.FreqDist(bigrams)
    top = fdist.most_common(n)
    return top
#---------------------------------------------------------

f = r'D:\Data\Subs\24\24.1x02.1am-2am.DVDRip.XViD-FoV.EN.srt'

from srtTools import srtTokens

tokens = srtTokens(f)

frequentBigrams(tokens, 20)

#------------------------------------------------------------

root = r'D:\Data\Subs\24'

from srtTools import dirParse

tokens = dirParse(root, tokens2=True, flat=True)

frequentBigrams(tokens, 20)

#--------------------------------------------------------------



#================================================================


