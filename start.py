#!/usr/bin/python3
import os
import sys
import ast
from collections import OrderedDict
import check_checkedCorpera
import tagandroll
import biggercorpora

def main(userInput):



    result1 = check_checkedCorpera.main(userInput)

    if result1 == 1:
        listofsentences = tagandroll.main(userInput)
        # start group 3
        # remove duplicates but keep order
        # source https://stackoverflow.com/questions/7961363/removing-duplicates-in-lists
        listwithoutduplicates = OrderedDict((x, True) for x in listofsentences).keys()
        # call group3 python program
        ranking = biggercorpora.main(listwithoutduplicates)
        print(ranking)
        return ranking



if __name__ == "__main__":
    main()
