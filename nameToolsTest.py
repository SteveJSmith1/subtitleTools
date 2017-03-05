# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 14:19:46 2017

@author: Steve
"""


import nameTools as nt

import srtTools as st

#=======================

# Test on single file

#=======================


file = r'D:\Data\Subs\24\Season 1\24.1x13.12pm-1pm.DVDRip.XViD-FoV.EN.srt'

tokens = st.srtParse(file, tokens=True)

ep13names = nt.parseNames(tokens)

ep13names
"""
...
 'Roger',
 'Jack',
 'Jack',
 'Jamey',
 'Wait',
 'Palmer']
"""

nt.topCharacters(ep13names)
"""
Out[4]: 
[('Jack', 14),
 ('Kim', 12),
 ('Kyle', 10),
 ('David', 9),
 ('Rick', 5),
 ...
"""

nt.fullNames(ep13names, tokens)
"""
Out[11]: [('Jack', 'Bauer'), ('Jamey', 'Farrell'), ('Maureen', 'Kingsley')]
"""

nt.getGenders(ep13names)
"""
 ('Roger', 'male'),
 ('See', 'male'),
 ('Sherry', 'female'),
 ('Son', 'male'),
 ('Teri', 'female'),
 ('Wait', 'male')]
"""

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


#==================================

# Test on directory

#==================================

import nameTools as nt

import srtTools as st

root = r'D:\Data\Subs\24\Season 1'

s1_24_tokens = st.dirParse(root, tokens=True, flat=True)

s1_24_names = nt.parseNames(s1_24_tokens)

s1_24_tc = nt.topCharacters(s1_24_names)

s1_24_fn = nt.fullNames(s1_24_names, s1_24_tokens)


#==================================

root = r'D:\Data\Subs\24\Season 2'

s2_24_tokens = st.dirParse(root, tokens=True, flat=True)

s2_24_names = nt.parseNames(s2_24_tokens)

s2_24_tc = nt.topCharacters(s2_24_names)

s2_24_fn = nt.fullNames(s2_24_names, s2_24_tokens)

#===================================

root = r'D:\Data\Subs\24\Season 3'

s3_24_tokens = st.dirParse(root, tokens=True, flat=True)

s3_24_names = nt.parseNames(s3_24_tokens)

s3_24_tc = nt.topCharacters(s3_24_names)

s3_24_fn = nt.fullNames(s3_24_names, s3_24_tokens)

#===================================

root = r'D:\Data\Subs\24\Season 4'

s4_24_tokens = st.dirParse(root, tokens=True, flat=True)

s4_24_names = nt.parseNames(s4_24_tokens)

s4_24_tc = nt.topCharacters(s4_24_names)

s4_24_fn = nt.fullNames(s4_24_names, s4_24_tokens)

#=====================================

root = r'D:\Data\Subs\24\Season 5'

s5_24_tokens = st.dirParse(root, tokens=True, flat=True)

s5_24_names = nt.parseNames(s5_24_tokens)

s5_24_tc = nt.topCharacters(s5_24_names)

s5_24_fn = nt.fullNames(s5_24_names, s5_24_tokens)

#======================================

root = r'D:\Data\Subs\24\Season 6'

s6_24_tokens = st.dirParse(root, tokens=True, flat=True)

s6_24_names = nt.parseNames(s6_24_tokens)

s6_24_tc = nt.topCharacters(s6_24_names)

s6_24_fn = nt.fullNames(s6_24_names, s6_24_tokens)


s1_24_top50 = nt.topCharacters(s1_24_names)
s1_24_top50

s2_24_top50 = nt.topCharacters(s2_24_names)
s2_24_top50

s3_24_top50 = nt.topCharacters(s3_24_names)
s3_24_top50

s4_24_top50 = nt.topCharacters(s4_24_names)
s4_24_top50

s5_24_top50 = nt.topCharacters(s5_24_names)
s5_24_top50

s6_24_top50 = nt.topCharacters(s6_24_names)
s6_24_top50

#======================================

## processing full series on a season by season basis

#======================================

from srtTools import seriesParse

series_tokens = seriesParse(r'D:\Data\Subs\TEST', tokens=True, flat=True)

from nameTools import parseSeriesNames

seasoned_chars = parseSeriesNames(series_tokens)


from nameTools import nameSeriesFreq
nameSeriesFreq('Gael', seasoned_chars)
   
from nameTools import seasonFreqs
freqs = seasonFreqs(seasoned_chars)

from nameTools import charSeasonPlot

names = ['Jack', 'Mason', 'Joe', 'Chloe']
charSeasonPlot(names, freqs)      


#============================================================

# Fetching characters per episide per series



#============================================================

import srtTools as st

ep_by_season = st.seriesParse(r'D:\Data\Subs\24', tokens=True)

import nameTools as nt


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

series_tokens = st.seriesParse(r'D:\Data\Subs\24', tokens=True, flat=True)

series_names = nt.parseSeriesNames(series_tokens)

flat_series_tokens = st.flatten(series_tokens)
flat_series_names = st.flatten(series_names)

nt.fullNames(flat_series_names, flat_series_tokens, n=100)

nt.families(flat_series_names, flat_series_tokens)

nt.topCharacters(flat_series_names, n=100)

nt.whoDied(flat_series_names, flat_series_tokens)

freqs = nt.seasonFreqs(series_names)


nt.charSeasonPlot(['Edgar', 'Chloe', 'Milo', 'Gael', 'Christopher'], freqs)



#=================================================

## Attempting plot



import matplotlib.pyplot as plt

"""
need to get the season length, 6 from namefreqs
"""

len(namefreqs[1] - 1)

"""
need to get number of episodes in a series
"""
len(namefreqs[0][1])


# x axis ticks

ticks = ['Ep-%d' % (i + 1) for i in range(len(namefreqs[0][1]))]


"""
season 4
"""

fig, ax = plt.subplots()
ax.plot(namefreqs[0][4], label = namefreqs[0][0])
ax.plot(namefreqs[1][4], label = namefreqs[1][0])

box = ax.get_position()
ax.set_position([box.x0, box.y0 + box.height * 0.1,
                     box.width, box.height * 0.9])
    
ax.legend(loc='best', bbox_to_anchor=(0.5, -0.05),
              fancybox=True, shadow=True, ncol=5)


# extracting all jack frequencies

no_of_seasons = len(namefreqs[1] - 1)


from srtTools import flatten

jackvals = []
for i in range(1, no_of_seasons + 1):
    jackvals.append(namefreqs[0][i])
jackvalsflat = flatten(jackvals)

fig, ax = plt.subplots()
ax.plot(jackvalsflat, label = namefreqs[0][0])


box = ax.get_position()
ax.set_position([box.x0, box.y0 + box.height * 0.1,
                     box.width, box.height * 0.9])
    
ax.legend(loc='best', bbox_to_anchor=(0.5, -0.05),
              fancybox=True, shadow=True, ncol=5)


""" to do, enable plotting for all names in namesfreq """
""" switch xticks to season names """
