def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def main():
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

main()
