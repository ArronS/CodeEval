# Print out the distance from the starting point to the nearest city,
# and the distances between two nearest cities separated by comma,
# in the order they appear on the route. (straight line route, sorted by range from start)
# Author: ArronS
# Date: 1.9.15

import sys

test_cases = open(sys.argv[1], 'r')
lines = test_cases.read().splitlines()  # gives a list of values (strings) from the file, with newlines stripped

for routes in lines:              # repeats cycle for each line of inputs

    values = routes.split(";")    # converts input string to list, determining separation as the semi-colon

    distances = []              # declares list for storage of town positions relative to start

    for x in values:

        y = x.split(",")        # splits list into two strings, inside a list (town name and town location)
        z = y[1::]              # splits list values from names
        distances.extend(z)     # extends list, creating "xxxx", instead of ["xxxx"]. Also removes empty list value [WTF]

    distances.sort()            # sorts distances in terms of range from start points (nearest to furthest)

    startPoint = 0              # sets value of start point
    totalDistance = []          # declares running distance total list

    for town in distances:                      # iterates through each value in sorted list
        point = int(town)                       # converts list value into usable int (next location)
        diff = point - startPoint               # calculates difference between values (locations)
        startPoint = point                      # defines new start point
        totalDistance.append(diff)              # appends difference between two nearest points into list
    print(','.join(map(str, totalDistance)))    # joins list of ints into comma delimited string and prints

test_cases.close()
