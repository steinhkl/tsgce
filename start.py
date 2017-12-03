import os
import sys
import ast

python2 = "/usr/lib/python2.7"
if os.name == 'nt':
    python2 = "C:/python27/python.exe"

python3 = "/usr/bin/python3"
if os.name == 'nt':
    python3 = "python.exe"

def main():

    if sys.argv[1]:
        userInput = sys.argv[1]
    else:
        print("Please give me the sentence you want to get checked:")
        userInput = input()
    
    import subprocess

    python3_command = python3 + " check_checkedCorpera.py "+userInput  # launch your python2 script using bash
    process = subprocess.Popen(python3_command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    
    if process.returncode ==1:
        python2_command = python2 + " tagandroll.py "+userInput  # launch your python2 script using bash
        process2 = subprocess.Popen(python2_command.split(), stdout=subprocess.PIPE)
        output, error = process2.communicate()
        for line in output.splitlines():
            pass
        last = line
        listofsentences = ast.literal_eval(last.decode('utf-8'))
        
        # THIS IS WHAT NEXT GROUP USES
        print(listofsentences)

        
if __name__ == "__main__":
        main()