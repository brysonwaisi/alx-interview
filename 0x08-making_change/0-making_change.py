#!/usr/bin/python3
'''We implement a dynamic programming approach'''


def makeChange(coins, total):
    if total <= 0:
        return 0
    coins.sort()
    dp = [float('inf')] * (total+1)
    dp[0] = 0
    for c in coins:
        last_c = -1
        for i in range(c, total+1):
            if dp[i-c] != float('inf') and last_c < dp[i-c]:
                dp[i] = min(dp[i], dp[i-c]+1)
                last_c = dp[i-c]
    return dp[total] if dp[total] < float('inf') else -1
