#!/usr/bin/python3
'''The minimum operations coding challenge.
'''


def minOperations(n):
    '''Computes the fewest number of operations needed to result
    in exactly n H characters.
    '''
    if n <= 1:
        return 0
    dp = [float('inf')] * (n + 1)
    dp[1] = 0
    for i in range(2, n+1):
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + (i // j))
                break
        if dp[i] == float('inf'):
            dp[i] = i
    return dp[n]
