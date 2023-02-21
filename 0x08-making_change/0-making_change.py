#!/usr/bin/python3
'''We implement a dynamic programming approach
dp[i] represents fewest coins needed to make i
dp[i-c]+1 represents the number of coins needed to make up the
remaining amount plus the current coin'''

# def makeChange(coins, total):
#     # base case
#     if total <= 0:
#         return 0
#     dp = [float('inf')] * (total + 1)  # convert infinity to floating number
#     dp[0] = 0
#     for c in coins:
#         for i in range(c, total + 1):
#             dp[i] = min(dp[i], dp[i-c]+1)
#     return dp[total] if dp[total] < float('inf') else -1

'''To make the solution even more efficient,
we can optimize the space complexity by using a one-dimensional array
dp instead of a two-dimensional one.
Instead of storing the fewest number of coins needed for each amount `i`
up to total for each coin, we can store the fewest number of coins
needed for each amount i upto total considering all the coins
we have processed so far.'''


def makeChange(coins, total):
    if total <= 0:
        return 0
    dp = [float('inf')] * (total+1)
    dp[0] = 0
    for c in coins:
        for i in range(c, total+1):
            dp[i] = min(dp[i], dp[i-c]+1)
    return dp[total] if dp[total] < float('inf') else -1
