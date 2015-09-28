# Finds the modulus of N / M without using the modulus operator
# Author: ArronS
# Date: 6.9.15

import sys

inputFile = open(sys.argv[1], "r")

for line in inputFile:          # reads input file, input by input

    line = line.split(",")      # splits comma delimited input into a list

    N = int(line[0])            # assigns each list value to each input value
    M = int(line[1])            # and converts to int

    while N >= M:               # removed total, using N. while value is greater than divider, iterate
        N -= M                  # > -> >= to allow for zero modulus returns

    print(N)                    # print return value after iterations are complete

inputFile.close()
