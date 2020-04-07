'''This version of the prime_factors program follows the factorization
procedure described in the directions of the Prime Factors exercise on exercism.io'''

def factors(value):
    primes = []
    while value > 1:
        for num in range(2, value+ 1):
            if value % num == 0:
                primes.append(num)
                value //= num
                break
    return sorted(primes)

