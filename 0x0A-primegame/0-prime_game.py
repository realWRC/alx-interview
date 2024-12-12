#!/usr/bin/python3
def isWinner(x, nums):
    """ Evaluates the winner of the prime game over multiple rounds.
    """
    if not nums or x < 1:
        return None

    max_n = max(nums)
    if max_n < 1:
        ben_wins = x
        maria_wins = 0
        if ben_wins > maria_wins:
            return 'Ben'
        elif maria_wins > ben_wins:
            return 'Maria'
        else:
            return None

    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False

    for p in range(2, int(max_n ** 0.5) + 1):
        if is_prime[p]:
            for multiple in range(p * p, max_n + 1, p):
                is_prime[multiple] = False

    count_primes = [0] * (max_n + 1)
    for i in range(2, max_n + 1):
        count_primes[i] = count_primes[i - 1] + (1 if is_prime[i] else 0)

    maria_wins = 0
    ben_wins = 0

    for i in range(x):
        if i >= len(nums):
            break
        n = nums[i]
        if n < 1:
            primes = 0
        elif n > max_n:
            primes = count_primes[max_n]
        else:
            primes = count_primes[n]

        if primes % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
