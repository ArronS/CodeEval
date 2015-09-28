# Calculates and prints the prime numbers up to the value given
# Author: ArronS
# Date: 25.8.15

import sys
import math

test_cases = open(sys.argv[1], 'r')

for test in test_cases:

    x = int(test)   # assigns line value to a variable
    total = "2"    # (re)starts calculations, first value will always be 2 (1st prime)

    for a in range(3, x, 2):   # goes through values 3 to line value, skips even numbers

        r = int(math.sqrt(a)) + 1
        '''assign the value of r to the square root of a. Brute forces only to sqrt(a).
        +1 to avoid override integer division.'''

        for b in range(2, r):   # calculates if prime
            if a % b == 0:
                break           # if x is not prime, continue
        else:
            total += str(",")   # adds required separation between string values
            total += str(a)     # if prime, adds value (as string) to total string

    print(total)    # prints string

test_cases.close()