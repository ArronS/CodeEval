# Converts hexadecimal input into decimal
# Author: ArronS
# Date: 6.9.15

import sys

inputFile = open(sys.argv[1], "r")

for file in inputFile:

    print(int(file, 16))

inputFile.close()
