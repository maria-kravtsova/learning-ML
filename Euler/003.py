def largestPrime(number):
    """Find the largest prime factor"""
    primes = []
    i = 2
    while i * i < number:
        while number % i == 0:
            number = number / i
            primes.append(number)
        i = i + 1
    print(number)
    print(primes)

largestPrime(600851475143)
