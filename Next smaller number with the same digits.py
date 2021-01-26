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


def next_smaller(n):
    reversed_numbers = []
    while n > 0:
        reversed_numbers.append(n % 10)
        n = n // 10
    numbers = reversed_numbers[::-1]
    swaped = False
    first_index = len(numbers) - 1
    second_index = len(numbers) - 2
    for i in range(len(numbers)):
        if numbers[second_index] > numbers[first_index]:
            numbers[first_index], numbers[second_index] = numbers[second_index], numbers[first_index]
            first_index -= 1
            second_index -= 1
            return numbers
    return -1



next_smaller(153)
