import os
import sys
import ast

import check_checkedCorpera
import tagandroll

def main():

    if len(sys.argv) > 1:
        userInput = sys.argv[1]
    else:
        print("Please give me the sentence you want to get checked:")
        userInput = input()
    
    result1 = check_checkedCorpera.main(userInput)

    if result1 == 1:
        listofsentences = tagandroll.main(userInput)
        
        # THIS IS WHAT NEXT GROUP USES
        print(listofsentences)

        
if __name__ == "__main__":
        main()