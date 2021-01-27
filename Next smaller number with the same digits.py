import random
import itertools

"""

Write a function that takes a positive integer and returns the next smaller positive integer containing the same digits.

For example:

next_smaller(21) == 12
next_smaller(531) == 513
next_smaller(2071) == 2017
Return -1 (for Haskell: return Nothing, for Rust: return None), when there is no smaller number that contains the same digits. Also return -1 when the next smaller number with the same digits would require the leading digit to be zero.

next_smaller(9) == -1
next_smaller(135) == -1
next_smaller(1027) == -1  # 0721 is out since we don't write numbers with leading zeros
some tests will include very large numbers.
test data only employs positive integers.
The function you write for this challenge is the inverse of this kata: "Next bigger number with the same digits."
"""

"""
Test.it("Smaller numbers")
Test.assert_equals(next_smaller(907), 790)
Test.assert_equals(next_smaller(531), 513)
Test.assert_equals(next_smaller(135), -1)
Test.assert_equals(next_smaller(2071), 2017)
Test.assert_equals(next_smaller(414), 144)
Test.assert_equals(next_smaller(123456798), 123456789)
Test.assert_equals(next_smaller(123456789), -1)
Test.assert_equals(next_smaller(1234567908), 1234567890)
"""

"""def next_smaller(n):
    reversed_numbers = []
    while n > 0:
        reversed_numbers.append(n % 10)
        n = n // 10
    numbers = reversed_numbers[::-1]
    combinations = set(itertools.permutations(numbers, len(numbers)))
    new_numbers = sorted(combinations)
    print(new_numbers)
    if len(numbers) == len(new_numbers):
        return -1
    print()
    return"""


def next_smaller(n):
    s = list(str(n))
    i = j = len(s) - 1
    while i > 0 and s[i - 1] <= s[i]: i -= 1
    if i <= 0: return -1
    while s[j] >= s[i - 1]: j -= 1
    s[i - 1], s[j] = s[j], s[i - 1]
    s[i:] = reversed(s[i:])
    if s[0] == '0': return -1
    print(int(''.join(s)))
    return int(''.join(s))


def convertig_list_to_int(some_list):
    new_integer = 0
    list_length = len(some_list) - 1
    for i in range(list_length + 1):
        new_integer += some_list[i] * (10 ** list_length)
        list_length -= 1
    return new_integer


next_smaller(2071)
