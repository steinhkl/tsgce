#!/usr/bin/python3
import os
import sys
import ast
from collections import OrderedDict


import check_checkedCorpera
import tagandroll
import biggercorpora

def main():

    if len(sys.argv) > 1:
        userInput = sys.argv[1]
    else:
        print("Please give me the sentence you want to get checked:")
        userInput = input()

    result1 = check_checkedCorpera.main(userInput)

    if result1 == 1:
        listofsentences = tagandroll.main(userInput)

        # start group 3
        # remove duplicates but keep order
        # source https://stackoverflow.com/questions/7961363/removing-duplicates-in-lists
        #listwithoutduplicates = OrderedDict((x, True) for x in listofsentences).keys()
        # call group3 python program
        listofsentences = biggercorpora.main(listofsentences)
        print(listofsentences)



if __name__ == "__main__":
    main()
