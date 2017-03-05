# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 12:27:18 2017

@author: stevejsmith567@gmail.com

"""


#===========================

# processing 24 Season 1

#===========================

import srtTools as st

root = r'D:\Data\Subs\24'
tokens = st.dirParse(root, tokens=True)

from nameTools import process, getFullNames, topCharacters, getGenders, families


process(tokens)

getFullNames()
topCharacters(n=30)
getGenders()
families()


