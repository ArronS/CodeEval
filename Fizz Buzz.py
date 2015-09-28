import sys

content = open(sys.argv[1], 'r')

for line in content:

    values = line.split(" ")

    X = int(values[0])
    Y = int(values[1])
    N = int(values[2])

    for x in range(1, N+1):

        if x % X == 0:
            print("F", end="")
            if x % Y == 0:
                print("B", end=" ")
                continue
            print("", end=" ")

        elif x % Y == 0:
            print("B", end=" ")

        else:
            print(x, end=" ")

    print("")

content.close()