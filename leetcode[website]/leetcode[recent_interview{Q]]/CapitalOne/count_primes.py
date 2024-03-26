import math

def count_primes(n:int) -> list[int]:
    """
        2 rules
        divisble by 1 and divisable by itself
        anything else pop() like it drop throw it away
        the algorithm we going to use is Sieve of Eratosthenes 
        n loglog n
    """
    primes = [True] * (n+1)
    primes[0] = primes[1] = False

    p = 2
    count_log_iterations_took = 0
    while p*p <= n:
        count_log_iterations_took += 1
        if primes[p]:
            for i in range(p*p, n+1, p):
                primes[i] = False
        p += 1
    return [n for n in range(2, n+1) if primes[n]], count_log_iterations_took

limit = 100
primes, count = count_primes(limit, limit * math.log(math.log(limit, 10), 10))


def is_prime(n:int) -> boool:
    """
        0 1 => False
        2 covered
        3 covered 
        checking for 2 and 3 is for optimal solution by quickly eliminating 
        even numbers except 2 and numbers that are divisble by 3 
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    p = 5
    while p * p <= n:
        if n % p == 0 or n % (p + 1) == 0:
            return False
        p += 6
    return True

def primes(n:int):
    return [n for n in range(n) if is_prime(n)]

print(is_prime(100))
