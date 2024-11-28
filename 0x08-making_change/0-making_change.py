#!/usr/bin/python3
""" Module that contains the function for interview question
make change.
"""


def makeChange(coins, total):
    """ Determines the fewest number of coins needed to meet a
    given amount total.
    """
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        if total <= 0:
            break
        count += total // coin
        total %= coin

    return count if total == 0 else -1
