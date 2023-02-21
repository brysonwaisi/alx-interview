#!/usr/bin/python3
'''We implement a greedy approach'''


def makeChange(coins, total):
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    coin_count = 0
    for coin in coins:
        if total >= coin:
            coin_count += total // coin
            total %= coin
        if total == 0:
            return coin_count
    return -1
