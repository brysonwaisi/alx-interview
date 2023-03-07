#!/usr/bin/python3
'''Prime game - This question
is a custom coding problem'''


def isWinner(x, nums):
    # Initialize a variable to keep track of the winner
    winner = None
    # Loop through each round
    for i in range(x):
        # Generate a list of prime numbers up to n
        n = nums[i]
        primes = []
        is_prime = [True] * (n+1)
        for j in range(2, n+1):
            if is_prime[j]:
                primes.append(j)
                for k in range(2*j, n+1, j):
                    is_prime[k] = False

        # Initialize a set of remaining numbers
        remaining = set(range(1, n+1))
        # Initialize a variable to keep track of the current player
        player = "Maria"

        # Simulate the game
        while primes:
            # Determine the smallest remaining prime number
            p = primes[0]
            # Remove p and its multiples from the set
            for i in range(p, n+1, p):
                if i in remaining:
                    remaining.remove(i)
            # If there are no more prime numbers in the set,
            # the other player wins
            if not remaining.intersection(set(primes)):
                if player == "Maria":
                    winner = "Ben"
                else:
                    winner = "Maria"
                break

            # Switch to the other player's turn
            if player == "Maria":
                player = "Ben"
            else:
                player = "Maria"

            # Remove p from the list of prime numbers
            primes.remove(p)

        # If the winner hasn't been determined yet, the current player wins
        if winner is None:
            winner = player

    return winner
