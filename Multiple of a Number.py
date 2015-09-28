# Prints out smallest multiple of x[1] that is larger than x[0]
# Author: ArronS
# Date: 26.8.15

import sys

test_cases = open(sys.argv[1], 'r')

for test in test_cases:

    v = test.split(",")     # converts line values into list

    x = int(v[0])           # changes list values into int variables
    y = int(v[1])
    z = 0                   # set as 0 online. can be set as y to save 1 iteration of the while loop

    while x > z:            # iterates multiples until minimum point reached
        z += y              # z required for multiple iterations (with y, value doubles)

    print(z)                # prints smallest multiple

test_cases.close()
