import json

class JsonGenerator():
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

    def generate_json_ngram(self, ngrams_dict):
        for n_in_ngram, ngrams in ngrams_dict.items():
           tmp = dict()
           tmp["error_in"] = int(n_in_ngram)
           tmp["ngram"] = list(ngrams)
           self.__jsonDict["ngrams"].append(tmp)

    def save(self):
        path="tmp/results.json"
        with open(path,"w") as f:
            f.write(self.print_json(False))

    def print_json(self, output=True):
        ret = json.dumps(self.__jsonDict, indent=4)
        if output:
            print(ret)
        return ret

