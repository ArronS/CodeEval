# Converts line to lower case and prints
# Author: ArronS
# Date: 26.8.15

import sys

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    result = test.lower()   # converts all line text to lower case with function
    print(result, end="")   # prints result

test_cases.close()
