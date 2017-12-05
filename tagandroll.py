#!/usr/bin/python3

import nltk
import json
from pattern.en import conjugate

# Refer to https://www.clips.uantwerpen.be/pages/pattern-en#conjugation
formaliases = ["inf", "1sg", "2sg", "3sg", "pl", "part", "1sgp", "2sgp", "3sgp", "ppl", "ppart"]

# This comes from First group in some way
intext = "The dog walks away."

# Create sentance given tagged text, the word to be changed and the index of it
def createsentence(sentance, wordformed, index):
    out = ""
    i = 0
    for word in sentance:
        
        # If the current word is subject to change, change it
        if i == index:
            out+=" "+wordformed
        
        # Dont add space before punctiation
        elif word[1] == '.':
            out+=word[0]

        # Every other word just write it down
        else:
            out+=" "+word[0]

        i+=1    
    out = out[1:]
    return out 

# Function to create a list of sentences with changed verbs
def inflictverbs(sentencestocheck):
    outlist = []
    #For all sentences to change
    for sentence in sentencestocheck:
        i = 0
        # Check every tag of sentence
        for word in sentencestocheck[sentence]:
            # Look for Verbs
            if word[1][0] == 'V':
                for alias in formaliases:
                    outlist.append(createsentence(sentencestocheck[sentence], conjugate(word[0], alias), i))
            i = i + 1

    return outlist

# This will generate this list of sentences (curently only changed verbs. Will do other stuff later)
def genlist(sentencestocheck):
    listofsentences = {}
    listofsentences = inflictverbs(sentencestocheck)


    return listofsentences
    
def main():
    #Check for missing resources
    try:
        nltk.data.find("averaged_perceptron_tagger")
    except:
        print("Loading missing libraries.")
        nltk.download("averaged_perceptron_tagger")


    #Tag input Text
    taggedtext = nltk.word_tokenize(intext)
    taggedtext = nltk.pos_tag(taggedtext)
    
    # Generate variations of sentence
    sentencestocheck = {intext : taggedtext}
    sentenceforms = genlist(sentencestocheck)

    # This goes to next group
    print(sentenceforms)


if __name__ == "__main__":
        main()