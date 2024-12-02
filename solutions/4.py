# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is
# 9009 = 91 x 99

# Find the largest palindrome made from the product of two 3-digit numbers.

# -- Notes -- #
# 3-digit Palindromes can be either xxxxxx, xyyyyx, xyzzyx

digit_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

first_digit = digit_list[1:] # cannot be 0
second_digit = digit_list
third_digit = digit_list
fourth_digit = third_digit
fifth_digit = second_digit
last_digit = first_digit

