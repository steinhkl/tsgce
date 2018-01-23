import json

# Abstracts specified JSON structure
class JsonGenerator():
    def __init__(self, userInput):

        # contains specified json structure of top-level JSON members
        self.__jsonDict = dict()
        self.__userInput = userInput
        self.__ngrams = []
        self.__tagged = []
        self.__forms = []

        self.__jsonDict["userInput"] = userInput
        self.__jsonDict["ngrams"] = self.__ngrams
        self.__jsonDict["tagged"] = self.__tagged
        self.__jsonDict["forms"] = self.__forms

    # Generate the specified JSON structure of a given ngram dict
    # Stores the generated JSON.
    def generate_json_ngram(self, ngrams_dict):
        for n_in_ngram, ngrams in ngrams_dict.items():
           tmp = dict()
           tmp["length"] = int(n_in_ngram)
           tmp["ngram"] = ngrams
           self.__jsonDict["ngrams"].append(tmp)

    # Saves JSON as a file in tmp/results.json
    # Exisiting files will be overwritten
    def save(self):
        path="tmp/results.json"
        with open(path,"w") as f:
            f.write(self.print_json(False))

    # Outputs JSON structure
    # return: String representation of JSON structure
    def print_json(self, output=True):
        ret = json.dumps(self.__jsonDict, indent=4)
        if output:
            print(ret)
        return ret

