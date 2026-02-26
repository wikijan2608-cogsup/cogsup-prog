"""
Write a script that lists all the prime numbers between 1 and 10000.
(A prime number is an integer greater or equal to 2 which has no divisors except 1 and itself). 
Hint: Write an is_factor helper function.
"""

def is_factor(d, n):
    """True if (if and only if) d is a divisor of n."""
    return n % d == 0

def is_prime(n):
    if n < 2:
        return False
    else:
        for d in range(2,n):
            if is_factor(d, n):
                return False
        return True


list_of_primes = []               

for n in range(2, 1001):          
    if is_prime(n):               
        list_of_primes.append(n)  

print(list_of_primes)
