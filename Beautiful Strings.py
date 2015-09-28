# Finds the maximum numerical value of a string (Beautiful Strings)
# Author: ArronS
# Date: 27.8.15

# Split string into each singular character, removing any special characters and spaces
# Sort characters and count occurrences
# Multiply character occurrence values by values from 26 to 1 (highest to most occurring character)
# Calculate running total of outputs and print total of all values

import sys
import re
from collections import Counter

test_cases = open("data.txt", 'r')

for test in test_cases:                         # repeats cycle for each input

    i = 0                                       # initialises start value
    t = 26                                      # defines highest multiplication value to jog back from

    test = test.lower()                         # sets all characters to lower case
    test = re.sub("[\W\d]+", "", test.strip())  # strips special characters, replaces with ""

    count = Counter(test)                       # converts string to value defined dict
    count = count.most_common()                 # removes "counter"(x) and places values into list

    for x in count:                             # for each value in counted list
        i += (x[1] * t)                         # creates running total, multiplying biggest value by 26 down
        t -= 1                                  # reduces 26 down, so that no two chars are * the same value
    print(i)                                    # prints total

test_cases.close()
