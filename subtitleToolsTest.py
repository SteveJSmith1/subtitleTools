# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 14:19:46 2017

@author: SteveJSmith1

Requirements:
    
nltk 
re

subtitle files in the following directory format

seriesDir -> seasonDirs -> epsiodes.srt

a csv list of surnames in the subtitleTools directory

for further info read the function strings
"""

#===================================================

## Importing modules and their dependencies

#===================================================

import nameTools as nt

import srtTools as st


#===================================================

# Testing tools on a single file

#===================================================


file = r'D:\Data\Subs\24\Season 1\24.1x13.12pm-1pm.DVDRip.XViD-FoV.EN.srt'

# Creating a list of tokens

tokens = st.srtParse(file, tokens=True)

# Extracting possible character names from the tokens

ep13names = nt.parseNames(tokens)

ep13names
"""
Outputs a list, unsorted and not in a set of names found:
    
    
...
 'Roger',
 'Jack',
 'Jack',
 'Jamey',
 'Wait',
 'Palmer']
"""

# passing the list of names to the topCharacters module

nt.topCharacters(ep13names)
"""
Outputs a frequency distribution.
A list of tuples of type [('name', freq), ...]

Out[4]: 
[('Jack', 14),
 ('Kim', 12),
 ('Kyle', 10),
 ('David', 9),
 ('Rick', 5),
 ...
"""

# Extracting possible surnames from the tokens
# requires a csv file containing last names.
# passes the list of names and the tokens

# it is required to have a file of last names
# in the same directory called last_names.csv

nt.fullNames(ep13names, tokens)
"""

Out[11]: [('Jack', 'Bauer'), ('Jamey', 'Farrell'), ('Maureen', 'Kingsley')]
"""

# Get the genders for the list of names

nt.getGenders(ep13names)
"""
 ('Roger', 'male'),
 ('See', 'male'),
 ('Sherry', 'female'),
 ('Son', 'male'),
 ('Teri', 'female'),
 ('Wait', 'male')]
"""

# Attempts to find those with the same surname

nt.families(ep13names, tokens)
"""
----------------------------------------
Surname: Bauer
Family Members: ['Jack']
----------------------------------------
Surname: Farrell
Family Members: ['Jamey']
----------------------------------------
Surname: Kingsley
Family Members: ['Maureen']
"""

# Extracting timings:
    
file = r'D:\Data\Subs\24\Season 1\24.1x13.12pm-1pm.DVDRip.XViD-FoV.EN.srt'

st.srtParse(file, times=True)

"""
output:
 '00:40:56,478 --> 00:40:58,721',
 '00:41:00,320 --> 00:41:02,272',
 '00:41:03,305 --> 00:41:09,552']
"""

# basic time analysis

st.filmLength(file)
"""
Out[11]: '00:41:09'
"""

st.timeAverages(file)
"""
    For the srt file with filename:
        D:\Data\Subs\24\Season 1\24.1x13.12pm-1pm.DVDRip.XViD-FoV.EN.srt
Words spoken per minute: 95.77
Unique words spoken per minute: 20.12

Out[12]: 
['D:\\Data\\Subs\\24\\Season 1\\24.1x13.12pm-1pm.DVDRip.XViD-FoV.EN.srt',
 95.771567436209,
 20.121506682867558]
"""



#==================================

# Test on directory, i.e. Season

#==================================

import nameTools as nt

import srtTools as st

# definine the directory containing the .srt files
# by episode

root = r'D:\Data\Subs\24\Season 1'

# Extracting the tokens, specifying flat=True to flatten the list into a single list rather than a list of lists

s1_24_tokens = st.dirParse(root, tokens=True, flat=True)

# passing the tokens to parseNames (this takes a while to execute)

s1_24_names = nt.parseNames(s1_24_tokens)

# extracting the character names for the entire season
s1_24_tc = nt.topCharacters(s1_24_names)
s1_24_tc
"""
Out[17]: 
[('Jack', 530),
 ('Kim', 324),
 ('Palmer', 193),
 ('Nina', 166),
 ('Teri', 142),
 ...
 
"""

# Extracting possible full names

s1_24_fn = nt.fullNames(s1_24_names, s1_24_tokens)
s1_24_fn
"""
Out[18]: 
[('Alan', 'Hayes'),
 ('Alan', 'Morgan'),
 ('Alan', 'York'),
 ('Carl', 'Webb'),
 ('David', 'Palmer'),
...
"""

# Extracting families

s1_24_families = nt.families(s1_24_names, s1_24_tokens)
"""
---------------------------------------
Surname: Allard
Family Members: ['Frank']
----------------------------------------
Surname: Almeida
Family Members: ['Tony']
----------------------------------------
Surname: Ames
Family Members: ['Frank']
----------------------------------------
Surname: Bauer
Family Members: ['Jack', 'Kim', 'Kimberly', 'Teri']
----------------------------------------
"""

# Calculations on the times

root = r'D:\Data\Subs\24\Season 1'

# extracting filenames

filenames = st.getFilenames(root)

# passing filmLength() the files

[st.filmLength(f) for f in filenames]
"""
Out[26]: 
['00:39:46',
 '00:40:09',
 '00:41:22',
 '00:40:25',
...
"""

[st.timeAverages(f) for f in filenames]
"""

...
    For the srt file with filename:
        D:\Data\Subs\24\Season 1\24.1x23.10pm-11pm.DVDRip.XViD-FoV.EN.srt
Words spoken per minute: 113.21
Unique words spoken per minute: 20.85

    For the srt file with filename:
        D:\Data\Subs\24\Season 1\24.1x24.11pm-12am.DVDRip.XViD-FoV.EN.srt
Words spoken per minute: 99.25
Unique words spoken per minute: 20.07
Out[27]: 
[['D:\\Data\\Subs\\24\\Season 1\\24.1x01.12am-1am.DVDRip.XViD-FoV.EN.srt',
  120.22632020117352,
  23.185247275775357],
 ['D:\\Data\\Subs\\24\\Season 1\\24.1x02.1am-2am.DVDRip.XViD-FoV.EN.srt',
  101.22042341220424,
  20.523038605230386],
  
...

"""



#==================================

# Test on a full series 

#==================================

import nameTools as nt

import srtTools as st

# definine the directory containing the season directories



root = r'D:\Data\Subs\24'

# extracting the tokens for the complete series

series_tokens = st.seriesParse(root, tokens=True, flat=True)

# parse the names for the entire series

series_chars = nt.parseSeriesNames(series_tokens)

# Returning a frequency for a name, per season in the entire Series


nt.nameSeriesFreq('Gael', series_chars)
"""
Out[34]: ['Gael', [0, 0, 69, 0, 0, 0]]
"""

# Extracting the frequencies, per character, per 
# season in the # entire series


char_freqs = nt.seasonFreqs(series_chars)

# plotting the frequencies for a given list of names
# in the series

names = ['Jack', 'Mason', 'Joe', 'Chloe']
nt.charSeasonPlot(names, char_freqs)      


#=====================================================
# Fetching characters per episide per series


#=====================================================

import srtTools as st
import nameTools as nt

# extracting characters, note the default flat = False
# is used
 
ep_by_season = st.seriesParse(r'D:\Data\Subs\24', tokens=True)


# extracting occurences of 'Jack'

jacklist = nt.seriesFreqs('Jack', ep_by_season)
jacklist[0]
"""
returns name


"""
jacklist[1]
"""
returns freqs in each episode in Season 1
"""

jacklist[2]
"""
returns freqs in each episode in Season 2
"""

# extracting mentions per ep_by_season for a list of names


names = ['Jack', 'Chloe']
namefreqs = [nt.seriesFreqs(name, ep_by_season) for name in names]

namefreqs[0]
"""
returns
Out[129]: 
['Jack',
 [22,
  22, ...
  ]]
"""

namefreqs[0][0]
"""
Out[131]: 'Jack'
"""

namefreqs[1][0]
"""
Out[132]: 'Chloe'
"""

namefreqs[0][1]
"""
returns the frequencies for jack in season 1
"""

namefreqs[1][4]
"""
returns the frequencies for Chloe in season 4
"""

# extracting full names from the series

series_tokens = st.seriesParse(r'D:\Data\Subs\24', tokens=True, flat=True)

series_chars = nt.parseSeriesNames(series_tokens)

# flatten the lists to pass to fullnames(), families()
# topCharacters() and whoDied()

flat_series_tokens = st.flatten(series_tokens)
flat_series_names = st.flatten(series_chars)

# getting the full names

nt.fullNames(flat_series_names, flat_series_tokens, n=100)

"""
out:
    ...
     ('Victor', 'Rovner'),
 ('Walt', 'Cummings'),
 ('Wayne', 'Palmer'),
 ('Will', 'Tom')]
"""

# finding characters with common surnames

nt.families(flat_series_names, flat_series_tokens)

"""
out:
    ...
    ----------------------------------------
Surname: Bauer
Family Members: ['Jack', 'Kim', 'Teri']
----------------------------------------
    ...
    ----------------------------------------
Surname: Palmer
Family Members: ['David', 'Sherry', 'Wayne']
----------------------------------------
...

"""

# finding the top 100 characters

nt.topCharacters(flat_series_names, n=100)
"""
out:
    Out[53]: 
[('Jack', 3409),
 ('Tony', 1382),
 ('Kim', 926),
 ('Bill', 742),
 ('Palmer', 641),
 ('Chloe', 595),
 ('David', 571),
"""

# attempting to ascertain who died

nt.whoDied(flat_series_names, flat_series_tokens)
"""
Out[54]: 
{('Alan', 'Milliken', 'died'),
 ('Alan', 'Milliken', 'is', 'dead'),
 ('Alan', 'York', 'is', 'dead'),
 ('Alexis', 'is', 'dead'),
 ('Ali', 'has', 'killed'),
 ('Ali', 'was', 'killed'),
 ('Audrey', "'s", 'dead'),
...
"""


# extracting the name and frequency per season
freqs = nt.seasonFreqs(series_chars)

# plotting a list of characters
nt.charSeasonPlot(['Edgar', 'Chloe', 'Milo', 'Gael', 'Christopher'], freqs)



#=================================================

## Attempting to plot character frequencies per
# episode over an entire series



import matplotlib.pyplot as plt

