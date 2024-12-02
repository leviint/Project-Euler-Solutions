# The prime factors of 13195 are 5, 7, 13 and 29
# What is the largest prime factor of the number 600851475143?

def factor(n):
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
        if divisor * divisor > n and n > 1:
            factors.append(n)
            break
    return factors

number = 600851475143
print(f"Prime factors: {factor(number)}")

# Solution: 6857