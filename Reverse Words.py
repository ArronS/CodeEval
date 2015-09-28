# Reverses the order of whole words
# Author: ArronS
# Date: 25.8.15

import sys

test_cases = open(sys.argv[1], 'r')
lines = test_cases.read().splitlines()  # gives a list of values (strings) from the file, with newlines stripped

for test in lines:         # repeats cycle for each input

    values = test.split(" ")    # converts input string to list, determining separation as the space
    l = values[::-1]            # reverses the order of the list using split notation
    str1 = ' '.join(l)          # joins spilt list values together into string with space separation

    print(str1)                 # prints joined string

test_cases.close()
