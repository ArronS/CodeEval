# to calculate the highest prime palindrome that is less than 1000 [24.8.15]

def reverse(x):             # turn x into string, use slice notation to reverse string
  return int(str(x)[::-1])  # turn string back into int "a[start:end:step]"

for x in range(1, 1000):    # check all numbers (assign x) between 1 and 1000

    rev = reverse(x)    # call int reverse function

    if rev == x:   # if the reversed int = the previous int, palindrome

        for a in range(2, x):
            if x % a == 0:      # if x % a = 0 (x divided ny all numbers leaves no remainder)
                break           # x is not prime, therefore break
        else:       # if for loop exits organically, a modulus of 0 has not been found
            y = x   # therefore the prime is passed into y

print(y)    # a higher value for x has not been found, therefore print y
