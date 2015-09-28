# Converts from zero-based numbers into integers
# Flag "0" means that the following sequence of zeroes should be appended to a binary string.
# Flag "00" means that the following sequence of zeroes should be transformed into a
# sequence of ones and be appended to a binary string.
# Author: ArronS
# Date: 6.9.15

import sys

inputFile = open(sys.argv[1], "r")
file = inputFile.read().splitlines()

for line in file:

    line = line.split(" ")
    x = 0
    total = ""

    for value in line:          # determines place within sequence

        ''' Calculates first (check bit) position and value '''

        if x % 2 == 0:          # even, checkBit
            checkBit = 1

            if value == "00":   # determines subsequent string should be converted into ones
                multiplier = 1
            elif value == "0":  # or zeros
                multiplier = 0
            else:
                print("Value Error")
            x += 1              # increase x by 1 (will not hit with continue used)
            continue            # continue loop to next iteration for sequence values

        else:                   # odd, checkBit reset
            checkBit = 0        # complete loop, finding length and updating binary value

        ''' Adds appropriate number of zeros or ones to total '''

        length = len(line[x])   # finds length of sequence

        if multiplier == 1:     # append ones

            for value2 in range(0, length):     # for each value (len) within sequence, add a 1 to string
                total += "1"

        elif multiplier == 0:   # append zeros

            for value2 in range(0, length):     # for each value (len) within sequence, add a 0 to a string
                total += "0"

        x += 1                  # iterates to next line input value

    print(int(total, 2))        # covert sting binary value string to integer and print

inputFile.close()
