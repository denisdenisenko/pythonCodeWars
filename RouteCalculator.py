import re

"""This calculator takes values that could be written in a browsers route path as a single string. It then returns the result as a number (or an error message).

Route paths use the '/' symbol so this can't be in our calculator. Instead we are using the '$' symbol as our divide operator.

You will be passed a string of any length containing numbers and operators:

'+' = add
'-' = subtract
'*' = multiply
'$' = divide
Your task is to break the string down and calculate the expression using this order of operations. (division => multiplication => subtraction => addition)

If you are given an invalid input (i.e. any character except .0123456789+-*$) you should return the error message:'400: Bad request'

Remember:
Operations are infinite
Order of operations is imperitive
No eval or equivalent functions

"""

"""

tests = [
    ["1.1", 1.1],                   # returns the number if no commands given
    ["10+5", 15],                   # addition
    ["8-2", 6],                     # subtraction
    ["4*3", 12],                    # muliplication
    ["18$2", 9],                    # division
    ["5+8-8*2$4", 9],               # multiple commands
    ["3x+1", "400: Bad request"]    # handles incorrect input
]

for test in tests:
    Test.assert_equals(calculate(test[0]), test[1])
    
"""

"""
calculate('1+1')     => '2'
calculate('10$2')    => '5'
calculate('1.5*3')   => '4.5'

calculate('5+5+5+5') => '20'

calculate('1000$2.5$5+5-5+6$6') =>'81'

calculate('10-9p')   =>  '400: Bad request'
"""

"""

Further Notes - Parameters outside of this challenge:
Brackets e.g. 10*(1+2)
Square root, log, % or any other operators
Unary minus (10*-1)
Bad mathematical input (10**$10 or 5+5$)
You may have to deal with floats
If enjoy this and want something harder please see http://www.codewars.com/kata/evaluate-mathematical-expression/ for making a much more complicated calculator. This is a good kata leading up to that.

"""


def calculate(expression):

    ops = {"+": (lambda x, y: x + y), "-": (lambda x, y: x - y),"/": (lambda x, y: x / y),"*": (lambda x, y: x * y)}

    digitPointer = 0
    expPoiner = 0

    x = re.split("\d", expression)
    y = re.split("\D", expression)

    startWithSymbolArray = []
    startWithdigitArray = []
    if x[0] == '':
        for i in x:
            if i != '':
                startWithdigitArray.append(i)
            else:
                startWithSymbolArray.append(i)


    # this is an array with replaced symbols
    new_array = replaceSymbols(startWithdigitArray)

    print(new_array)
    print(y)

    sum = 0

    longest_array = longestArray(x, y)




    print (ops[new_array[1]](int(y[0]),int(y[1]))) # prints 2



# combineTwoArrays



# return   # evaluated expression


def longestArray(arr1, arr2):
    x = arr1.__len__()
    y = arr2.__len__()
    if x > y:
        return x
    elif y > x:
        return y


def replaceSymbols(arr):
    newArray = []
    for i in arr:
        if i == "$":
            newArray.append("/")
        else:
            newArray.append(i)

    return newArray


calculate("45*6$456+3")
