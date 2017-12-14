#!/usr/bin/python3
import os
import threading
import nltk
from nltk.util import ngrams
from jsonGenerator import jsonGenerate


class CorpusCheckThread (threading.Thread):
    def __init__(self, corpus, input_sentence, outputList, is_sentence=True):
        threading.Thread.__init__(self)
        self.corpus = corpus
        self.input_sentence =  input_sentence
        self.outputList = outputList
        self.is_sentence = is_sentence

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
            str_sentence_ngram = '#'.join(sentence_ngram)
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
        l = len(in_ngrams[0])

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
                ngram_negative_dict[str_in_ngram] = False
                self.outputList.append(in_ngram)
        '''
        for s in self.corpus.sents():
            s_ngrams = list(ngrams(s, l))
            for s_ngram in s_ngrams:
                str_s_ngram = ''.join((s_ngram))
                for ngram in in_ngrams:
                    str_ngram = ''.join(ngram)
                    if str_ngram in ngram_positive_dict:
                        continue
                    if str_ngram == str_s_ngram:
                        ngram_positive_dict[str_ngram] = True
                        break
                    else:
                        if not str_ngram in ngram_negative_dict:
                            ngram_negative_dict[str_ngram] = True
                            self.outputList.append(ngram)
        '''

    def run_is_sentence(self):
        return_Value = False
        for s in self.corpus.sents():
            if self.input_sentence == s:
                return_Value = True
                break
        self.outputList.append(return_Value)


def generate_N_ngrams_of_sentence(corpera, sentence_tokens, resultList):
    N_ngrams = list()
    threads = list()

    for i in range(len(sentence_tokens)):
        n = i+1

        ngram =  list(ngrams(sentence_tokens, n))
        N_ngrams.append(ngram)
        for corpus in corpera:
            corpus_thread = CorpusCheckThread(corpus, ngram, resultList, is_sentence=False)
            corpus_thread.start()
            threads.append(corpus_thread)

        for check_threads in threads:
            check_threads.join()

    return N_ngrams

def set_nltk_data_dir():
	nltk_dir = os.getcwd() + '/nltk_data'
	nltk.data.path.append(nltk_dir)

def main(inputtext):
    resultList = []
    threads = []
    if inputtext !="":
        userInput = inputtext
    else:
        print("Please give me the sentence you want to get checked:")
        userInput = input()

    set_nltk_data_dir()

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
        for result in resultList:
            print(result)
        print("Function of second group will be called")
        return 1

if __name__ == "__main__":
        main("")
