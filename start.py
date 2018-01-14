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

 
    result1 = check_checkedCorpera.main(userInput)

    if result1 == 1:
        jsong2 = {}
        with open("./tmp/results.json") as jsong1_data:
            jsong1 = json.load(jsong1_data)
            jsong2 = tagandroll.main(jsong1)
        
        print("______________")
        print(jsong2)
        print("______________")
        listofsentences = []
        for sentence in jsong2["forms"]:
            listofsentences.append(sentence["sentence"])

        # start group 3
        # remove duplicates but keep order
        # source https://stackoverflow.com/questions/7961363/removing-duplicates-in-lists
        listwithoutduplicates = OrderedDict((x, True) for x in listofsentences).keys()
        # call group3 python program
        listofsentences = biggercorpora.main(listwithoutduplicates)
        print(listofsentences)
        return(listofsentences)


if __name__ == "__main__":
    main()
