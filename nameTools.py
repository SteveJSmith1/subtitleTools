# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 12:27:18 2017

@author: stevejsmith567@gmail.com

#===============================================
This module extracts information about names in a list of tokens
#===============================================
limitations:
    
    Surnames will not be found if they contain
    non alpha characters. e.g. o'brian, smith-jones
    if these haven't been tokenized as full words
    
#===============================================
Requirements:
    
    This module requires a list of tokens, nltk.word_tokenize is recommended
    
    nltk and nltk.corpus.names is also required

#===============================================
Usage:

    
    parseNames(tokens) should be used first

Then use:
    
    topCharacters(name_list, n=30) to find the top 30 characters
    
    fullNames(name_list, tokens, n=30) to find estimates of the full name of a character
    
    getGenders(name_list) to estimate the genders of the characters
    
    families(name_list) to group people by surname
#===============================================
"""



import nltk
from nltk.corpus import names


def parseNames(tokens):
    """
    Parses a list of tokens looking for
    names
    """
    labelled_names = _genderedNames()
    print('-'*30)
    print("Parsing names...")
    print('-'*30)
    
    # find the names in the tokens

    char_names = [item for item in tokens for name,_ in labelled_names if item == name]
    
    return char_names
    


#----------------------------------------

def _surnameList():
    """
    Called to extract a list of surnames
    from a given csv file.
    
    Note: To use, alter 'filepath' to insert your
    own csv list
    
    returns a list of surnames
    """
    
    import csv

    filepath = r'Last_Names.csv'
    with open(filepath, 'r', errors='ignore') as csvfile:
        surnames = list(csv.reader(csvfile))
    
    from srtTools import flatten
    
    return flatten(surnames)
 
def _genderedNames():
    """
    Called to extract
    names and genders
    
    Uses nltk.corpus.names 
    
    
    returns a list [name, gender]
    """
    
    return ([(name, 'male') for name in names.words('male.txt')] + [(name, 'female') for name in names.words('female.txt')])
    

def topCharacters(name_list, n=30):
    """
    Used to find the top n characters based on name usage
    
    inputs: The returned list from parseNames(tokens)
            n = number of most common entries
    
    returns: frequency distribution
    """
    return nltk.FreqDist(name_list).most_common(n)
    

def fullNames(name_list, tokens, n=30):
    """
    Attempts to ascertain full names of the characters in the list of tokens
    
    inputs: the returned list from parseNames(tokens)
            tokens
            number of names to return
            
    returns: a sorted set of names
    """
    
    bgrams = list(nltk.bigrams(tokens))
    
    top_characters = topCharacters(name_list, n)
    top_char_names = [name for name,_ in top_characters]
    
    #filter bigrams by name +  following string

    poss_names = [(w,x) for (w,x) in bgrams if w in set(top_char_names)]
        
    # process poss_names to include following words that are capitalized
    
    stopwords = nltk.corpus.stopwords.words('english')
    
    surnames = _surnameList()
    
    processed_names = [(w, j) for (w, j) in poss_names if not j.islower() and j not in w and j.lower() not in stopwords and j.isalpha() and j in surnames]
    
    return sorted(set(processed_names))
    
    
def getGenders(name_list, n=30):
    """
    Used to ascertain the genders in a list of names
    
    inputs: returned list from parseNames(tokens)
    returns: list [first name, gender]
    """
    
    top_characters = topCharacters(name_list, n)
    top_char_names = [name for name,_ in top_characters]
    # search labelled names for the top characters and return the gender
    
    labelled_names = _genderedNames()
    
    return sorted(set([(i,j) for (i,j) in labelled_names if i in top_char_names]))


def families(name_list, tokens):
    """
    Matches characters with the same surname
    
    Inputs: Returned list from parseNames(tokens)
            tokens
            
    returns: print of surname with associated first names
    """
    
    processed_names = fullNames(name_list, tokens)

    # find relationships, i.e. matching surnames in list
    
    
    rev = sorted(nltk.FreqDist([(s,f) for (f, s) in processed_names]))


    surname_set = list(sorted(set(i for (i,j) in rev)))
    
    
    for i in range(len(surname_set)):
        print("-"*40)
        print("Surname: %s" % (surname_set[i]))
        
        
        print("Family Members: %s" % [j for (x,j) in rev if x == surname_set[i]])
    
    return

def parseSeriesNames(series_tokens):
    """
    This function parses names for each individual season in a series
    
    workflow:   from srtTools import seriesParse
                series_tokens = seriesParse(rootDir, tokens=True, Flat=True)
              -> 
                  from nameTools import parseSeriesNames
                  parseSeriesNames(series_tokens)
              
    input: series_tokens (which is a list of lists containing tokens per series)
    
    output: a list of lists containing characters in each season
              
    """
    import time
    print("-"*55)
    print("Parsing names from an entire series")
    print("takes a considerable amount of time")
    time.sleep(1)
    inp = str(input("Are you sure you wish to proceed? [y]es/[n]o: "))
    
    
    print("-"*55)
    if inp == 'y':
        time.sleep(1)
        print("Go make a coffee, have a poo or read reddit for a while")
        print("-"*55)
        time.sleep(3)
        
        seasoned_chars = []
        for season in series_tokens:
            print("Parsing folder %d...." % (series_tokens.index(season) + 1))
            print("-"*22)
            seasoned_chars.append(parseNames(season))
            
        print("Parsing names complete")
        print("-"*22)
        return seasoned_chars
    else:
        return
  
#=======================================================

def nameSeriesFreq(firstname, seasoned_chars, n=50):
    """
    This function is called to obtain the frequency of a given name per season 
    workflow:   from srtTools import seriesParse
                series_tokens = seriesParse(rootDir, tokens=True, Flat=True)
              -> 
                  from nameTools import parseSeriesNames
                  seasoned_chars = parseSeriesNames(series_tokens)
              ->
                  nameSeriesFreq('Jack', seasoned_chars)
              
    input: firstname as a string
           seasoned characters (which is a list of lists containing characters
           per season)
    
    output: a list of the form ['Jack', [44, 53, 44, 34, 57, 69]] 
    
    """
    
    from srtTools import flatten
    
    top_season_chars = [topCharacters(names, n) for names in seasoned_chars]
    
    
    name_freq = []
    
    # find firstname in each season and return the frequency
    # if not there return an empty list
    for i in range(len(seasoned_chars)):
        name_freq.append( [[freq for name, freq in top_season_chars[i] if name==firstname]])
    
    #replace empty lists with 0
    zeroed = []
    for i in range(len(name_freq)):
        zeroed.append([elem or [0] for elem in name_freq[i]])
    zeroed = flatten(flatten(zeroed))
    
    return [firstname] + [zeroed]
    
#=======================================================

def seasonFreqs(seasoned_chars, n=50):
    """
    This function collects the top 50 (default) characters in each season
    before finding the frequency of each name in each season.
    
    
    
    workflow:   from srtTools import seriesParse
                series_tokens = seriesParse(rootDir, tokens=True, Flat=True)
              -> 
                  from nameTools import parseSeriesNames
                  seasoned_char = parseSeriesNames(series_tokens)
              ->
                  from nameTools import seasonFreqs
                  seasonFreqs(seasoned_chars)
                  
    input: a list of characters returned obtained from
             parseSeriesNames(series_tokens)
    
    output: a list of the form ['name', [f1, f2, f3, ...] ]
            
    further analysis:
            freqs = seasonFreqs(seasoned_chars)
            extract names:
            [name for name in freqs if (freqs.index(name) + 1) % 2]
            extract freqs:
            [freq for freq in freqs if freqs.index(freq) % 2]
    """
    from srtTools import flatten
    char_set = set(flatten(seasoned_chars))
    
    return flatten([nameSeriesFreq(name, seasoned_chars) for name in char_set])

#=======================================================

def seriesFreqs(name, ep_by_season):
    
    
    
    no_of_seasons = len(ep_by_season)
    
    no_of_eps_per_season = [len(ep_by_season[i]) for i in range(len(ep_by_season))]
    
    season_freqs = []
    for j in range(no_of_seasons):
        """Issue now is all seasons are length 2
        as seen by no_eps_per_season[0]
        """
        season_length = no_of_eps_per_season[j]
        for i in range(season_length):
            fd = nltk.FreqDist(ep_by_season[j][i])
            season_freqs.append(fd[name])
    
    freqs = []
    count = 0
    for size in no_of_eps_per_season:
        freqs.append([season_freqs[i + count] for i in range(size)])
        count += size
    return [name] + freqs

#=======================================================    

def charSeasonPlot(names, freqs, save=False):
    """
    This function, when passed a list of names to plot,
    finds the frequency for each season for each name and plots
    
    workflow:   from srtTools import seriesParse
                series_tokens = seriesParse(rootDir, tokens=True, Flat=True)
              -> 
                  from nameTools import parseSeriesNames
                  seasoned_char = parseSeriesNames(series_tokens)
              ->
                  from nameTools import seasonFreqs
                  freqs = seasonFreqs(seasoned_chars)
              ->
                  names = ['Jack', 'Mason', 'Joe', 'Chloe']
                  charSeasonPlot(names, freqs)
                  
                  If save=True, prompts for a filename
    
    
    """
    
    import matplotlib.pyplot as plt
    
    ticks = ['Season-%d' % (i + 1) for i in range(len(freqs[1]))]
    
    name_locs =[freqs.index(name) for name in names]
     
    
    fig, ax = plt.subplots()
    
    for i in name_locs:
        ax.plot(freqs[i+1], label=freqs[i])
    box = ax.get_position()
    ax.set_position([box.x0, box.y0 + box.height * 0.1,
                     box.width, box.height * 0.9])
    
    # Put a legend below current axis
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
              fancybox=True, shadow=True, ncol=5)
    plt.xticks(range(len(ticks)), ticks, size='small')
    
    
    if save == True:
        filename = str(input("Enter a filename: "))
        plt.savefig('%s.png' % filename, dpi=800)
    
        
    plt.show()
    return 
    
#=======================================================
    
    
def whoDied(name_list, tokens):
    from nltk import ngrams
    """
    This function attempts to ascertain who dies in a passed tokenized text
    
    inputs: name_list from parseNames(tokens)
            tokens that were passed to parseNames(tokens)
            
    returns: list of characters who, quite possibly, have died
    """
    name_set = set(name_list)
    print('-'*30)
    print('Searching for possible deaths.')
    print('-'*30)
    bgrams = list(ngrams(tokens, 2))
    threegrams = list(ngrams(tokens, 3))
    fourgrams = list(ngrams(tokens, 4))
    
    death_words = ['dead', 'killed', 'died']
    iswas = ['is', 'was']
    poss_deaths1 = [(x,y,z) for (x,y,z) in threegrams if x in name_set and z in death_words]
    
    poss_deaths2 = [(x,y) for (x,y) in bgrams if x == 'killed' and y in name_set]
    
    poss_deaths3 = [(x,y,z) for (x,y,z) in threegrams if x in name_set and y == 'passed' and z == 'away']
    
    poss_deaths4 = [(w,x,y,z) for (w,x,y,z) in fourgrams if w in name_set and z in death_words and y in iswas]
    
    
    return set(poss_deaths1 + poss_deaths2 + poss_deaths3 + poss_deaths4)
    

 