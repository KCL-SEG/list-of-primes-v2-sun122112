"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def isPrime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 ==0:
        return False
    for i in range(3, int(num/2)+1):
        if (num % i) == 0:
            return False
    return True


def primes(number_of_primes):
    if number_of_primes <=0:
        raise ValueError
    list = []
    num = 2
    while len(list) < number_of_primes:
        if isPrime(num):
            list.append(num)
        num += 1

    return list
