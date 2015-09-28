# Find the right-most occurrence of the second character in the first string
# https://www.codeeval.com/open_challenges/31/
# Author: ArronS
# Date: 7.9.15

import sys

inputFile = open(sys.argv[1], "r")

for line in inputFile:

    if line == "\n":                        # if line is empty, skip line
        continue

    newLine = line.split(",")               # separates input into string and character

    string = newLine[0]                     # moves each variable piece into unique variable
    character = newLine[1]
    newCharacter = character[0]                # strips newline bug from character value
    length = len(string)                    # determines length of string to minus x from

    newString = string[::-1]                # reverses string to count from opposite direction

    x = 0                                   # initialises counter

    for value in newString:                 # iterates through string values
        x += 1

        if value == newCharacter:              # tests if solution (character in string) is found
            countFromLeft = length - x      # calculates places from left
            print(countFromLeft)
            break                           # breaks when solution found

        if x == length:
            print("-1")                     # if no solution is found, print -1

inputFile.close()
