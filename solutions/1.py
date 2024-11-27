# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

integer = range(1000)
num_sum = 0

for x in integer:
    if x % 3 == 0 or x % 5 == 0:
        num_sum += x

print(num_sum)

# Solution: 233168
