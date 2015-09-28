# to calculate sum of first 1000 primes (answer = 3682913) [24.8.15]

y = 0
t = 0

for x in range(2, 1000000):     # 1 is not a prime number and is therefore skipped

    for a in range(2, x):   # divides x ny all numbers excluding 1
        if x % a == 0:      # if x % a = 0 (x divided ny all numbers leaves no remainder)
            break           # x is not prime, therefore break
    else:           # if for loop exits organically, a modulus of 0 has not been found
        y += x      # therefore the prime is added to the running total (y)
        t += 1      # prime found so add to running break total

    if t == 1000:   # once 1000 primes have been found, break
        break

print(y)    # print running total
