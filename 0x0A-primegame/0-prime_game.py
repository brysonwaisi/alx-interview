#!/usr/bin/python3
'''Prime game - This question
is a custom coding problem'''


def isWinner(x, nums):
    """Determines the winner of a prime game session with `x` rounds.
    """
    if x < 1 or not nums:
        return None

    marias_wins, bens_wins = 0, 0

    # Generate primes up to the maximum number in `nums`
    n = max(nums)
    primes = [True for _ in range(1, n + 1)]
    primes[0] = False

    # Use the Sieve of Eratosthenes algorithm to mark all non-prime numbers
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i - 1]:
            for j in range(i * i, n + 1, i):
                primes[j - 1] = False

    # Count the number of primes less than `n` in each round
    for n in nums:
        primes_count = sum(primes[0:n])
        if primes_count % 2 == 0:
            bens_wins += 1
        else:
            marias_wins += 1

    # Determine the winner based on the number of wins for each player
    if marias_wins == bens_wins:
        return None
    elif marias_wins > bens_wins:
        return 'Maria'
    else:
        return 'Ben'
