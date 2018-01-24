#!/usr/bin/python3

import nltk
import itertools
import json
from pattern.en import conjugate

# Refer to https://www.clips.uantwerpen.be/pages/pattern-en#conjugation
formaliases = ["inf", "1sg", "2sg", "3sg", "pl", "part", "1sgp", "2sgp", "3sgp", "ppl", "ppart"]


def retaglist (jsonlist):
    
    for idx, form in enumerate(jsonlist["forms"]):
        #Tag Text
        taggedtext = nltk.word_tokenize(form["userInput"])
        taggedtext = nltk.pos_tag(taggedtext)
        jsonlist["forms"][idx]["tagged"] = taggedtext

    return jsonlist

# Create sentence given tagged text, the word to be changed and the index of it
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
def arrayToSentence(sentence):
    out = ""
    i = 0
    for word in sentence:
        # Dont add space before punctiation
        if word == '.':
            out+=word

        # Every other word just write it down
        else:
            out+=" "+word

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

def permutengrams(jsonsentence):
    outlist =  []
    tokenized_sentence = []
    # Save original tokenized sentence
    for token in jsonsentence["tagged"]:
        tokenized_sentence.extend([token[0]])
    
    # For every Ngram size
    
    for ngramsize in jsonsentence["ngrams"]:
        if ngramsize["length"] > 5:
            continue

        # For Every Ngram in Ngramsize
        for ngram in ngramsize["ngram"]:
            #Permute List
            permOfNgram = list(itertools.permutations(list(ngram["ngram"])))
            
            #for every created permutation create the new sentence
            for perm in permOfNgram:
                i = ngram["error_at"]
                tmp_tok_sent = []
                
                for token in jsonsentence["tagged"]:
                    tmp_tok_sent.extend([token[0]])
               
                # For every word in permutation
                for swappedword in perm:
                    
                    tmp_tok_sent[i] = swappedword
                    i += 1

                outlist.extend([{"sentence":arrayToSentence(tmp_tok_sent)}])
    
    return outlist

            

# This will generate this list of sentences (curently only changed verbs. Will do other stuff later)
def genlist(jsonsentence):
    out ={}
    listofsentences = []
    out  = inflictverbs(jsonsentence) 

    #Permutate Ngrams
    out.extend(permutengrams(jsonsentence))
    return out

def main(injson):
    #Check for missing resources

    #injson["sentence"] = injson["userInput"]
    try:
        nltk.data.find("taggers/averaged_perceptron_tagger")
    except:
        print("Loading missing libraries.")
        nltk.download("averaged_perceptron_tagger")

    
    #Tag input Text
    taggedtext = nltk.word_tokenize(injson["userInput"])
    taggedtext = nltk.pos_tag(taggedtext)
    injson["tagged"] = taggedtext
    
    # Generate variations of sentence

    injson["forms"] = genlist(injson)

    
    # This goes to next group
    #print(jsonout)
    return injson


if __name__ == "__main__":
    main(inputtext)
