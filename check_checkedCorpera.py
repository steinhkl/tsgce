#!/usr/bin/python3

import threading
import nltk
import sys  
from nltk.util import ngrams

class CorpusCheckThread (threading.Thread):
    def __init__(self, corpus, input_sentence, outputList):
        threading.Thread.__init__(self)
        self.corpus = corpus
        self.input_sentence =  input_sentence
        self.outputList = outputList
    def run(self):
        return_Value = False
        for s in self.corpus.sents():
            if self.input_sentence == s:
                return_Value = True
                break
        self.outputList.append(return_Value)


def generate_N_ngrams_of_sentence(word_tokens):
    N_ngrams = list()
    
    for i in range(len(word_tokens)):
        n = i+1
        N_ngrams.append(ngrams(word_tokens, n))

    return N_ngrams

def main(inputtext):
    resultList = []
    threads = []
    if inputtext !="":
        userInput = inputtext
    else:
        print("Please give me the sentence you want to get checked:")
        userInput = input()
    
    try:
        nltk.data.find("tokenizers/punkt")
        nltk.data.find("corpora/brown")
        nltk.data.find("corpora/masc_tagged.zip")
    except:
        print("Loading missing libraries.")
        nltk.download("punkt")
        nltk.download("brown")
        nltk.download("masc_tagged")
        print("Finished downloading.")
        sentence_tokens = nltk.word_tokenize(userInput)
        corpera = [nltk.corpus.brown, nltk.corpus.masc_tagged]
  
    sentence_tokens = nltk.word_tokenize(userInput)
    corpera = [nltk.corpus.brown, nltk.corpus.masc_tagged]
 
    print("Performing the check")
    for corpus in corpera:
        corpus_thread = CorpusCheckThread(corpus, sentence_tokens, resultList)
        corpus_thread.start()
        threads.append(corpus_thread)

    for check_threads in threads:
        check_threads.join()
    
    if True in resultList:
        print("Your sentence is correct")
        return 0
    else:
        print("Function of second group will be called")
        return 1

if __name__ == "__main__":
        main("")
