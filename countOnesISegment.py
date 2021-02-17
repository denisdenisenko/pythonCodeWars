import re
from functools import lru_cache
import itertools

"""
Given two numbers: 'left' and 'right' (1 <= 'left' <= 'right' <= 200000000000000) return sum of all '1' occurencies in binary representations of numbers between 'left' and 'right' (including both)

Example:
countOnes 4 7 should return 8, because:
4(dec) = 100(bin), which adds 1 to the result.
5(dec) = 101(bin), which adds 2 to the result.
6(dec) = 110(bin), which adds 2 to the result.
7(dec) = 111(bin), which adds 3 to the result.
So finally result equals 8.
WARNING: Segment may contain billion elements, to pass this kata, your solution cannot iterate through all numbers in the segment!


test.describe("Sample Tests")
test.it('Easy') 
test.assert_equals(countOnes(5,7), 7)
test.assert_equals(countOnes(12,29), 51)


"""

@lru_cache(maxsize=None)
def countOnes(left, right):
    number_of_ones = 0
    for i in range(left, right+1):
        x = bin(i)
        b = re.findall(r"1", x)
        number_of_ones+=len(b)
    return number_of_ones


def countOnes2(left, right):
    number_of_ones = 0
    for i in range(left, right+1):
        x = bin(i)
        b = re.findall(r"1", x)
        number_of_ones+=len(b)
    return number_of_ones

countOnes(12,29)