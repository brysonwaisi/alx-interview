# Prime Game

#### We use the Sieve of Eratosthenes to solve this problem optimally.

 The function generates all primes up to the maximum number in nums using the Sieve of Eratosthenes algorithm, and then counts the number of primes in each round to determine the winner.

To determine the winner of the game, we use the Sieve of Eratosthenes to generate a list of prime numbers up to `n`. Then, we can simulate the game by keeping track of the remaining numbers in the set and the player whose turn it is. On each turn, the player chooses the smallest remaining prime number and removes it and its multiples from the set. If there are no more prime numbers in the set, the other player wins.