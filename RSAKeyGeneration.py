"""
RSA Key Generation
This program generates a pair of RSA keys.
The user is prompted to enter two prime numbers,
and the program generates the public and private keys based on these numbers.
"""

def is_prime(n):
    """
    Check if a number is prime.

    Args:
        n (int): Number to check for primality

    Returns:
        bool: True if the number is prime, False otherwise
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def gcd(a, b):
    """
    Calculate the Greatest Common Divisor of two numbers using
    the Euclidean algorithm.

    Args:
        a (int): First number
        b (int): Second number

    Returns:
        int: Greatest Common Divisor of a and b
    """
    while b:
        a, b = b, a % b
    return a

def generate_keys():
    # Get Prime Values
    PrimeOne = int(input("Enter first Prime number: "))
    PrimeTwo = int(input("Enter second Prime number: "))

    # Generate n
    n = PrimeOne * PrimeTwo

    # Generate x and e
    x = (PrimeOne - 1) * (PrimeTwo - 1)

    # Find a suitable e that is coprime with x
    e = 2
    while gcd(e, x) != 1:
        e += 1

    publicKey = (n, e)
    print("Public Key: ")
    print(publicKey)

    # Calculate private key d such that (d * e) % x == 1
    d = 1
    while (d * e) % x != 1:
        d += 1

    privateKey = (n, d)
    print("Private Key: ")
    print(privateKey)

    return publicKey, privateKey
