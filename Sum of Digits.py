# Given a positive integer, find the sum of its constituent digits.
# Author: ArronS
# Date: 31.8.15

import sys

opened = open(sys.argv[1], "r")
file = opened.read().splitlines()   # gives a list of values (strings) from the file, with newlines stripped

for line in file:
    total = 0                       # resets running total counter to 0
    for value in line:              # for each value within number,
        total += int(value)         # add value to running total
    print(total)                    # print running total

opened.close()
