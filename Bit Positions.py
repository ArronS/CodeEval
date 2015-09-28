# Calculates if x[1] is equal to x[2] and prints output accordingly
# Author: ArronS
# Date: 27.8.15

import sys

test_cases = open(sys.argv[1], 'r').read().splitlines()  # opens file and strips \n from inputs

for test in test_cases:     # repeats cycle for each input

    v = test.split(",")     # converts line values into list

    if v[1] == v[2]:        # calculates if match
        print("true")
    else:
        print("false")
