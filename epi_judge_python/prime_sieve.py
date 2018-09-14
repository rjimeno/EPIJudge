from test_framework import generic_test


# Given n, return all primes up to and including n.
def generate_primes(n):
    primes = []
    # is_prime[p] represents if p is prime or not. Initially, set each to
    # true, except 0 and 1. Then use sieving to eliminate non primes.
    is_prime = [False, False] + [True] * (n - 1)
    for p in range(2, n + 1):
        if is_prime[p]:
            primes.append(p)
            for i in range(p, n + 1, p):
                is_prime[i] = False
    return primes


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("prime_sieve.py", "prime_sieve.tsv",
                                       generate_primes))
