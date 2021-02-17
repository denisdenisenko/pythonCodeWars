import math

"""
The task is simply stated. Given an integer n (3 < n < 109), find the length of the smallest list of perfect squares which add up to n. Come up with the best algorithm you can; you'll need it!

Examples:

sum_of_squares(17) = 2
17 = 16 + 1 (4 and 1 are perfect squares).
sum_of_squares(15) = 4
15 = 9 + 4 + 1 + 1. There is no way to represent 15 as the sum of three perfect squares.
sum_of_squares(16) = 1
16 itself is a perfect square.
Time constraints:

5 easy (sample) test cases: n < 20

5 harder test cases: 1000 < n < 15000

5 maximally hard test cases: 5 * 1e8 < n < 1e9

15 random maximally hard test cases: 1e8 < n < 1e9

"""

"""

test.describe("Testing sum_of_squares: easy test cases")
test.assert_equals(sum_of_squares(15), 4)
test.assert_equals(sum_of_squares(16), 1)
test.assert_equals(sum_of_squares(17), 2)
test.assert_equals(sum_of_squares(18), 2)
test.assert_equals(sum_of_squares(19), 3)
"""


def sum_of_squares(n):
    number = 0
    counter = 0
    if math.sqrt(n).is_integer():
        number += 1
        return number
    else:
        return sum_of_squares_recurs(n, number, counter)


def sum_of_squares_recurs(n, number, counter):
    if math.sqrt(n).is_integer() and counter == 0:
        number += 1
        return number
    elif math.sqrt(n).is_integer() and counter != 0:
        return sum_of_squares_recurs(int(math.sqrt(n)), number, 0)


x = sum_of_squares(15)
print(x)
