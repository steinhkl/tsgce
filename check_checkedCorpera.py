#!/usr/bin/python3
import os
import threading
import nltk
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

    def run(self):
        if self.is_sentence:
            self.run_is_sentence()
        else:
            self.run_is_ngram()

    # check each a s sentence for a specific ngram
    # generate n ngram from sentence
    # generate string representation of sentence ngram
    # and compare
    def check_ngram_in_sentence(self, sentence, str_ngram, n):
        sentence_ngrams = list(ngrams(sentence, n))

        for sentence_ngram in sentence_ngrams:
            str_sentence_ngram = '#'.join(sentence_ngram).lower()
            if str_ngram == str_sentence_ngram:
                return True

        return False

    # check ngram in whole copera (all sentences in corpera)
    def check_ngram_in_corpera(self, str_ngram):
        n = str_ngram.count('#') + 1
        ret = False

        # check each sentence in corpera for a ngram
        for sentence in self.corpus.sents():
            if self.check_ngram_in_sentence(sentence, str_ngram, n):
                ret = True
                break

        return ret

    def run_is_ngram(self):
        in_ngrams = self.input_sentence
        ngram_positive_dict = dict()
        ngram_negative_dict = dict()

        # iterate through all ngram in input_sentence (in_ngrams)
        # and compare each tuple of in_grams with each ngram from sentence
        # iterate over all ngrams in_sentence: (in_ngram)
        # generate a string representative for each in_ngram
        # and compare string representation of in_ngram with
        # each string representation of corpus_sentence

        for in_ngram in in_ngrams:
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

                self.ngrams_errors[str(n_in_ngram)].append(in_ngram)
                self.outputList.append(in_ngram)

    def run_is_sentence(self):
        returnValue = False
        for s in self.corpus.sents():
            if self.input_sentence == s:
                returnValue = True
                break
        self.outputList.append(returnValue)


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
            errors_dict[n_in_ngrams] = list(set(errors_dict[n_in_ngrams]))

    return N_ngrams

def set_nltk_data_dir():
	nltk_dir = os.getcwd() + '/nltk_data'
	nltk.data.path.append(nltk_dir)

errors_dict = dict()
def add_errors_to_dict(d):
    for n_in_ngram, ngrams in d.items():
        if n_in_ngram not in errors_dict: errors_dict[n_in_ngram] = list()
        errors_dict[n_in_ngram].extend(ngrams)

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
        resultList = []

        generate_N_ngrams_of_sentence(corpera, sentence_tokens, resultList)
        jsonGenerator.generate_json_ngram(errors_dict)
        jsonGenerator.print_json()
        jsonGenerator.save()

        print("Function of second group will be called")
        return 1

if __name__ == "__main__":
        main("")
