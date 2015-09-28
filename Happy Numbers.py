# Calculates if a number is happy or not (the values digits square roots tend to 0)
# https://www.codeeval.com/open_challenges/39/
# Author: ArronS
# Date: 6.9.15

import sys

inputFile = open(sys.argv[1], "r")

for file in inputFile:

    file = file.strip()         # strips new lines

    for x in range(0, 100):     # tries to calculate required output for 100 iterations

        total = 0               # resets total (required value) for each iteration

        for i in file:              # for each int within line
            total += (int(i)**2)    # square int and add to running total

        if total == 1:      # exit loop if target output (total == 1) is met
            print("1")
            break

        if x == 99:         # exit loop if target output (total == 1) is not met after 99 iterations
            print("0")
            break

        file = str(total)   # converts total int into iterable string

inputFile.close()
