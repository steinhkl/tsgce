import json

class jsonGenerate():
    def __init__(self, userInput):
        self.__jsonDict = dict()
        self.__userInput = userInput
        self.__ngrams = []
        self.__tagged = []
        self.__forms = []

        self.__jsonDict["userInput"] = userInput
        self.__jsonDict["ngrams"] = self.__ngrams
        self.__jsonDict["tagged"] = self.__tagged
        self.__jsonDict["forms"] = self.__forms

        print(json.dumps(self.__jsonDict))

    # ngram : (dict(errorin_ ngram))
    def generate_ngram(self, n, ngram):
        print("generate_ngram")

        while len(self.__ngrams) < n:
            self.__ngrams.append([])

        self.__ngrams[n-1].append(ngram)


jg = jsonGenerate("hello world")
ngram = dict()
ngram["error_in"] = 2
ngram["ngram"] = []

jg.generate_ngram(1, ngram)


print(json.dumps(ngram))

