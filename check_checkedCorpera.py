#!/usr/bin/python3
import os
import threading
import nltk
from collections import namedtuple
from nltk.util import ngrams
from jsonGenerator import JsonGenerator

class CorpusCheckThread (threading.Thread):
    def __init__(self, corpus, input_sentence, outputList, is_sentence=True):
        threading.Thread.__init__(self)
        self.corpus = corpus
        self.input_sentence =  input_sentence
        self.outputList = outputList
        self.is_sentence = is_sentence
        self.ngrams_errors = dict()

    # Determine the execution flow
    # Checking sentence or ngrams of a given corpera
    def run(self):
        if self.is_sentence:
            self.run_is_sentence()
        else:
            self.run_is_ngram()

    # check each a s sentence for a specific ngram
    # generate n ngram from sentence
    # generate string representation of sentence ngram
    # and compare
    # return    true: ngram is in sentence
    #           false: ngram no in sentence
    def check_ngram_in_sentence(self, sentence, str_ngram, n):
        sentence_ngrams = list(ngrams(sentence, n))

        for sentence_ngram in sentence_ngrams:
            str_sentence_ngram = '#'.join(sentence_ngram).lower()
            if str_ngram == str_sentence_ngram:
                return True

        return False

    # check ngram in whole copera (all sentences in corpera)
    # return    true: ngram is in corpera
    #           false: ngram no in corpera
    def check_ngram_in_corpera(self, str_ngram):
        n = str_ngram.count('#') + 1
        ret = False

        # check each sentence in corpera for a ngram
        for sentence in self.corpus.sents():
            if self.check_ngram_in_sentence(sentence, str_ngram, n):
                ret = True
                break

        return ret

    # iterate through all ngram in input_sentence (in_ngrams)
    # and compare each tuple of in_grams with each ngram from sentence
    #  iterate over all ngrams in_sentence: (in_ngram)
    # generate a string representative for each in_ngram
    # and compare string representation of in_ngram with
    # each string representation of corpus_sentence
    def run_is_ngram(self):
        in_ngrams = self.input_sentence
        ngram_positive_dict = dict()
        ngram_negative_dict = dict()

        for idx, in_ngram in enumerate(in_ngrams):
            str_in_ngram = '#'.join(in_ngram)

            if str_in_ngram in ngram_negative_dict:
                continue

            if self.check_ngram_in_corpera(str_in_ngram):
                ngram_positive_dict[str_in_ngram] = True

            else:
                ngram_negative_dict[str_in_ngram] = True
                n_in_ngram = len(in_ngram)
                key = str(n_in_ngram)

                if not key in self.ngrams_errors:
                    self.ngrams_errors[key] = list()

                tmp = dict()
                tmp["error_at"] = idx
                tmp["ngram"] = in_ngram
                self.ngrams_errors[str(n_in_ngram)].append(tmp)
                self.outputList.append(in_ngram)


    # checks input sentence against each sentence in corpus
    def run_is_sentence(self):
        returnValue = False
        for s in self.corpus.sents():
            if self.input_sentence == s:
                returnValue = True
                break
        self.outputList.append(returnValue)

# Generates all ngrams from input and,
# spawns for each corpera, n threads,
# where n is the number n in ngram (n=number of threads)
def generate_N_ngrams_of_sentence(corpera, sentence_tokens, resultList):
    N_ngrams = list()
    threads = list()

    for i in range(len(sentence_tokens)):
        n = i+1

        ngram = list(ngrams(sentence_tokens, n))
        N_ngrams.append(ngram)
        for corpus in corpera:
            corpus_thread = CorpusCheckThread(corpus, ngram, resultList, is_sentence=False)
            corpus_thread.start()
            threads.append(corpus_thread)

        for check_threads in threads:
            check_threads.join()
            add_errors_to_dict(check_threads.ngrams_errors)

        for n_in_ngrams in errors_dict.keys():
            errors_dict[n_in_ngrams] = errors_dict[n_in_ngrams]

    return N_ngrams

# Sets path to nltk project dir
def set_nltk_data_dir():
	nltk_dir = os.getcwd() + '/nltk_data'
	nltk.data.path.append(nltk_dir)

# Contains all "error" ngrams as a key-value pair.
# Error ngrams are associated with ngrams, which arent found in the corpera.
# Error ngram dict structure:
#   key: n in ngram
#   value:  list of ngrams associated with n
errors_dict = dict()

# Adds all erros from an given dictonary to error dict.
# Error dict extends its corresponding ngram list
def add_errors_to_dict(d):
    for n_in_ngram, ngrams in d.items():
        if n_in_ngram not in errors_dict: errors_dict[n_in_ngram] = list()
        errors_dict[n_in_ngram].extend(ngrams)

#Removes the duplicates which were created due to the using of threads
def remove_duplicates(errorsDict):
    for key in errorsDict:
        new_l = []
        seen =[]
        for d in errorsDict.get(key):
            error_at = d.get('error_at')
            if error_at not in seen:
                seen.append(error_at)
                new_l.append(d)
        errorsDict[key]=new_l

def main(inputtext):
    if inputtext !="":
        userInput = inputtext.lower()
    else:
        print("Please give me the sentence you want to get checked:")
        userInput = input().lower()

    set_nltk_data_dir()

    resultList = []
    threads = []
    jsonGenerator = JsonGenerator(userInput)
    sentence_tokens = nltk.word_tokenize(userInput)
    corpera = [nltk.corpus.brown, nltk.corpus.masc_tagged]

    print("Performing the initial Error check")
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
        resultList = []

        generate_N_ngrams_of_sentence(corpera, sentence_tokens, resultList)
        remove_duplicates(errors_dict)
        print(errors_dict)
        jsonGenerator.generate_json_ngram(errors_dict)
        # DEBUG: Uncomment to print JSON after Group 1
        # jsonGenerator.print_json()
        jsonGenerator.save()

        print("I found an Error! Function of second group will be called")
        return 1

if __name__ == "__main__":
        main("")
