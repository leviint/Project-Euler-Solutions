# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is
# 9009 = 91 x 99

# Find the largest palindrome made from the product of two 3-digit numbers.

# -- Notes -- #
# 3-digit Palindromes can be either xxxxxx, xyyyyx, xyzzyx
# Lychrel numbers may help?

palindrome_list = []

biggest_palindrome = 0

for i in range(999, 99, -1):
    for j in range(i, 99, -1):
        product = i * j
        str_product = str(product)
        if len(str_product) == 6:
            is_palindrome = (str_product[0] == str_product[5]) and (str_product[1] == str_product[4]) and (str_product[2] == str_product[3])
            if is_palindrome and product > biggest_palindrome:
                biggest_palindrome = product

print(biggest_palindrome)
