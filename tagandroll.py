#!/usr/bin/python3

import nltk
import json
from pattern.en import conjugate

# Refer to https://www.clips.uantwerpen.be/pages/pattern-en#conjugation
formaliases = ["inf", "1sg", "2sg", "3sg", "pl", "part", "1sgp", "2sgp", "3sgp", "ppl", "ppart"]

# This comes from First group in some way
inputtext = "The dog walks away."

def retaglist (jsonlist):
    
    for idx, form in enumerate(jsonlist["forms"]):
        #Tag Text
        taggedtext = nltk.word_tokenize(form["sentence"])
        taggedtext = nltk.pos_tag(taggedtext)
        jsonlist["forms"][idx]["tagged"] = taggedtext

    return jsonlist

# Create sentance given tagged text, the word to be changed and the index of it
def createsentence(sentence, wordformed, index):
    out = ""
    i = 0
    for word in sentence:
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
def inflictverbs(jsonsentence):
    outlist = []
    verbfound = False
    ##For all sentences to change
    #for sentence in sentencestocheck:
    #    i = 0
    i = 0
    # Check every tag of sentence
    for word in jsonsentence["tagged"]:
        # Look for Verbs
        if word[1][0] == 'V':
            verbfound = True
            for alias in formaliases:
                sentenceformed = { "sentence" : createsentence(jsonsentence["tagged"], conjugate(word[0], alias), i)}
                outlist.append(sentenceformed)
        i += 1
    if verbfound == False:
        print("No verb found, returning empty list")

    return outlist

# This will generate this list of sentences (curently only changed verbs. Will do other stuff later)
def genlist(jsonsentence):
    listofsentences = []
    jsonsentence = inflictverbs(jsonsentence) 

    return jsonsentence

def main(intext):
    #Check for missing resources
    jsonout = {}
    jsonout["sentence"] = intext
    try:
        nltk.data.find("taggers/averaged_perceptron_tagger")
    except:
        print("Loading missing libraries.")
        nltk.download("averaged_perceptron_tagger")

    
    #Tag input Text
    taggedtext = nltk.word_tokenize(intext)
    taggedtext = nltk.pos_tag(taggedtext)
    jsonout["tagged"] = taggedtext

    # Generate variations of sentence

    jsonout["forms"] = genlist(jsonout)

    # This goes to next group
    return jsonout


if __name__ == "__main__":
        main(inputtext)
