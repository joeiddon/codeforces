'''
sol: number of combinations (ways of choosing) unique prime factors
because over the different values for `a`, lcm will either
cancel them all out (resulting in `1`), or cancel none out

assuming that every combination is possible, the different results
are the unique combinations of prime factors
'''
import math, itertools

def p_fact(n):
    factors = []
    dividor = 2
    lim = int(n ** 0.5) + 1
    while n > 1 and dividor < lim:
        while n % dividor == 0:
            factors.append(dividor)
            n //= dividor
        dividor += 1
    if n != 1:
        factors.append(n)
    return factors

prime_factors = p_fact(int(input()))

ways = 1
#end stop for the for-loop
prime_factors.append(-1)
this_factor_count = 0
for i, f in enumerate(prime_factors[:-1]):
    this_factor_count += 1
    if f != prime_factors[i+1]:
        #we can pick factors as many times as there
        #are factors + 1 since we can pick no factors
        ways *= this_factor_count + 1
        this_factor_count = 0

print(ways)
