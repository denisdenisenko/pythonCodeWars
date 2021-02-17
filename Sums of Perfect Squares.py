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
    new_n = 0
    sqrt_num = n
    counter = 0
    while True:
        sqrt_num = math.sqrt(n)
        if sqrt_num.is_integer() and counter == 0:
            number+=1
            return number
        elif sqrt_num.is_integer() and counter != 0:
            number+=1
            sqrt_num = n - sqrt_num
            sum_of_squares_recurs(sqrt_num,number,counter)


        sqrt_num = ((n) - counter)
        counter += 1


def sum_of_squares_recurs(n,number,counter):


