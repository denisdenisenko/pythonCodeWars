import functools

"""
A Hamming number is a positive integer of the form 2i3j5k, for some non-negative integers i, j, and k.

Write a function that computes the nth smallest Hamming number.

Specifically:

The first smallest Hamming number is 1 = 203050
The second smallest Hamming number is 2 = 213050
The third smallest Hamming number is 3 = 203150
The fourth smallest Hamming number is 4 = 223050
The fifth smallest Hamming number is 5 = 203051
The 20 smallest Hamming numbers are given in example test fixture.

Your code should be able to compute all of the smallest 5,000 (Clojure: 2000, NASM: 13282) Hamming numbers without timing out.
"""


def same_structure_as(original, other):
    x = str(original)
    y = str(other)

    str1 = ""
    str2 = ""

    str_str1 = ""
    str_str2 = ""
    opened = '['
    closed = ']'
    coma = ','

    print(x)
    x.split("'")
    print(x)
    for i in x:
        if i == opened or i == closed or i == coma:
            str1 += str(i)
            print(str1)
        elif i == "'":
            continue

    for j in y:
        if j == opened or j == closed or j == coma:
            str2 += str(j)
        elif j == "'":
            continue

    print(str1)
    print(str2)


@functools.lru_cache(maxsize=None)
def hamming(element):
    elements = []
    counter = 1
    if element == 1:
        return 1
    sequence = 1
    # for i in range(element):
    while element != 0:
        x = hamming_numbers_sequence(sequence)
        if x == True:
            elements.append(sequence)
            counter += 1
            sequence += 1
            element -= 1
        else:
            counter += 1
            sequence += 1
    print(elements)
    return (elements[-1])


@functools.lru_cache(maxsize=None)
def hamming_numbers_sequence(x):
    if x == 1:
        return True
    if x % 2 == 0:
        return hamming_numbers_sequence(x / 2)
    if x % 3 == 0:
        return hamming_numbers_sequence(x / 3)
    if x % 5 == 0:
        return hamming_numbers_sequence(x / 5)
    else:
        return False


@functools.lru_cache(maxsize=None)
def memoize(f):
    memo = {}

    def helper(x):
        if x not in memo:
            memo[x] = f(x)
            print(memo[x])
        return memo[x]

    return helper


hamming(300)
