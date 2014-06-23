# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

def relativelyPrimeToList(q, prime_list):
    """returns whether q is divisible by anything in the prime list"""
    for p in prime_list:
        if q % p == 0 : return False
        if p**2 > q : return True
    return True

# <codecell>

def nthPrime(n):
    """returns the nth prime number"""
    prime_list = [2]
    i = 2
    while len(prime_list) < n:
        i += 1
        if relativelyPrime(i, prime_list): prime_list.append(i)
    return prime_list[-1]

# <codecell>

def primeList( n ):
    """returns all the primes less than n"""
    prime_list = [2]
    i = 2
    while i < n:
        i += 1
        if relativelyPrime(i, prime_list): prime_list.append(i)
    return prime_list

# <codecell>

nthPrime(4)

# <codecell>

primeList(100)

# <codecell>

#problem 7 - find the 10,001st prime number

# <codecell>

nthPrime(10001)

# <codecell>

relativelyPrimeToList(107, [2,3,5,7,11,13])

# <codecell>


