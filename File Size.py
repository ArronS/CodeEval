# Calculates the size in bytes of an input file (whole file, multiple lines)
# Author: ArronS
# Date: 5.9.15

import sys
inputFile = open(sys.argv[1], 'r')   # opens file

total = 0

for line in inputFile:              # gets size of file for each char line (expected file)

    line.encode('utf8')             # encodes line to unicode
    total += len(line)              # calculates length of unicode string

print(total)

inputFile.close()                   # closes file
