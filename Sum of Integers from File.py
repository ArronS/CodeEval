# Print out sum of integers read from file
# Author: ArronS
# Date: 1.9.15

import sys

test_cases = open(sys.argv[1], 'r')

total = 0                   # sets the initial value of total, and defines type (int)

for test in test_cases:

    test = int(test)        # converts line in file to int

    total += test           # creates running total of lines

print(total)                # once file is finished, prints total

test_cases.close()
