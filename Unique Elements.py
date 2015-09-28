# Removes repeated values and prints refined list with duplicates removed
# Author: ArronS
# Date: 6.9.15

import sys

inputFile = open(sys.argv[1], "r")
inputs = inputFile.read().splitlines()  # opens file and strips \n from inputs

for line in inputs:

    line = line.split(",")
    prev = 0                    # defines previous as integer
    total = []                  # defines total as string

    for value in line:          # loop to determine duplicates and add to string if not

        if value == prev:       # if previous value = current value, iterate to next value
            continue
        else:
            total.append(value)     # append, extend creates iterable single value string

        prev = value            # assigns current value to previous value for next loop

    print(",".join(total))      # joins total list into comma delimited string and prints

inputFile.close()
