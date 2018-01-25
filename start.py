#!/usr/bin/python3
import os
import sys
import ast
from collections import OrderedDict
import check_checkedCorpera
import tagandroll
import biggercorpora
import json

def main(userInput):

    if userInput !="":
        userInput = userInput.lower()
    else:
        print("Please give me the sentence you want to get checked:")
        userInput = input().lower()

    #TODO: Clean up this mess...


    result1 = check_checkedCorpera.main(userInput)
    
    if result1 == 1:
        json2 = {}
        with open("./tmp/results.json") as json1_data:
            json1 = json.load(json1_data)
            json2 = tagandroll.main(json1)
        
        result = biggercorpora.main(json2)
        print(result)
        return result


if __name__ == "__main__":
    if len(sys.argv) > 1:
        userInput = sys.argv[1]
    else:
        userInput = ""
    main(userInput)
