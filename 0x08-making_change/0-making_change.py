#!/usr/bin/python3
'''We implement a dynamic programming approach
dp[i] represents fewest coins needed to make i
dp[i-c]+1 represents the number of coins needed to make up the
remaining amount plus the current coin'''


def makeChange(coins, total):
    # base case
    if total <= 0:
        return 0
    dp = [float('inf')] * (total + 1)  # convert infinity to floating number
    dp[0] = 0
    for c in coins:
        for i in range(c, total + 1):
            dp[i] = min(dp[i], dp[i-c]+1)
    return dp[total] if dp[total] < float('inf') else -1
