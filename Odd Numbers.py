# Prints the odd numbers from 1 to 99
# Author: ArronS
# Date: 31.8.15

for x in range(1, 100):
    if x % 2 == 1:
        print(x)
    elif x % 2 == 0:
        continue
    else:
        print("Value is neither Odd nor Even")
