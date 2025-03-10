"""
RSA Key Generation
This program generates a pair of RSA keys using precomputed prime numbers.
The primes are chosen to be large enough to handle our maximum message size.
"""

# Larger prime numbers for better block handling
PRIME_NUMBERS = [
    32749,
    32771,
    32783,
    32789,
    32797,
    32801,
    32803,
    32831,
    32833,
    32839,
    32843,
    32869,
    32887,
    32909,
    32911,
    32917,
    32933,
    32939,
    32941,
    32957,
    32969,
    32971,
    32983,
    32987,
    32993,
    32999,
    33013,
    33023,
    33029,
    33037,
]


def gcd(a: int, b: int) -> int:
    """
    Calculate the Greatest Common Divisor using Euclidean algorithm.

    Args:
        a (int): First number
        b (int): Second number

    Returns:
        int: Greatest Common Divisor of a and b
    """
    while b:
        a, b = b, a % b
    return a


def generate_keys() -> tuple:
    """
    Generate RSA key pair using the largest available prime numbers.
    This ensures consistent key sizes large enough for our messages.

    Returns:
        tuple: ((n, e), (n, d)) - public and private key pairs
    """
    # Always use the two largest primes
    prime_one = PRIME_NUMBERS[-1]  # 33037
    prime_two = PRIME_NUMBERS[-2]  # 33029

    # Calculate modulus n (approximately 1.09 billion)
    modulus = prime_one * prime_two

    # Calculate Euler's totient
    totient = (prime_one - 1) * (prime_two - 1)

    # Use standard RSA public exponent
    public_exp = 65537

    # Calculate private exponent
    private_exp = pow(public_exp, -1, totient)

    return (modulus, public_exp), (modulus, private_exp)


if __name__ == "__main__":
    public_key, private_key = generate_keys()
    print(f"Public Key (n,e): {public_key}")
    print(f"Private Key (n,d): {private_key}")
