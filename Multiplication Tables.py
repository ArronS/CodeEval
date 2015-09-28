# PrintS out the grade school multiplication table up to 12*12 in a matrix (4x4) fashion
# Author: ArronS
# Date: 1.9.15


for y in range(1, 13):              # sets y axis position

    for x in range(1, 13):          # sets x axis position

        z = x * y                   # calculates table value

        if z < 10:                  # determines indent spacing
            print("   ", end="")

        elif z < 100:
            print("  ", end="")

        elif z < 1000:
            print(" ", end="")

        print(z, end="")            # prints table value

    print("")                       # prints new line
