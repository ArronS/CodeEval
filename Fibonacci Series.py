# Finds the nth number in a fibonacci sequence
# Author: ArronS
# Date: 1.9.15

import sys

test_cases = open(sys.argv[1], 'r')

for test in test_cases:

    a = 1               # sets initial conditions
    b = 1
    c = 0

    test = int(test)    # converts test (str) to an integer for iteration

    while test > 0:     # iterates until the nth number is reached
        a = b           # moves values back one place (post calculation)
        b = c
        c = a + b
        test -= 1

    print(c)            # prints nth number in fibonacci sequence

test_cases.close()