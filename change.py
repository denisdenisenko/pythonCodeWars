"""
Write a function that counts how many different ways you can make change for an amount of money, given an array of coin denominations. For example, there are 3 ways to give change for 4 if you have coins with denomination 1 and 2:

1+1+1+1, 1+1+2, 2+2.
The order of coins does not matter:

1+1+2 == 2+1+1
Also, assume that you have an infinite amount of coins.

Your function should take an amount to change and an array of unique denominations for the coins:

  count_change(4, [1,2]) # => 3
  count_change(10, [5,2,3]) # => 4
  count_change(11, [5,7]) # => 0

"""

"""
test.assert_equals(3, count_change(4, [1,2]))
test.assert_equals(4, count_change(10, [5,2,3]))
test.assert_equals(0, count_change(11, [5,7]))
"""


def count_change(money, coins):
    if len(coins)==1 and coins[0]==money:
        return 1
    if len(coins) == 1 and coins[0] != money:
        return 0
    external_counter = 0
    for i in coins:
        for j in coins:
            external_counter += money_equals_number_of_times_with_itself(money, j)
            external_counter += count_change(money, coins[i+1:])
            if i + j < money:
                static_j = j
                while (i + j < money):
                    j += static_j
                    if i + j == money:
                        external_counter += 1
                        break
                    elif i + j > money:
                        j = static_j
                        break
    return external_counter


def money_equals_number_of_times_with_itself(money, coin):
    counter = 0
    if money == coin:
        counter += 1
        return counter
    else:
        coin_static = coin
        while money >= coin:
            coin = coin + coin_static
            if money == coin:
                counter += 1
                return counter
    return 0


print(count_change(10, [5, 2, 3]))

print(money_equals_number_of_times_with_itself(10, 2))

somelist = [1,2,3,4,5,6]
