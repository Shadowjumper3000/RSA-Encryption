from RSAKeyGeneration import generate_keys
from RSAEncryption import rsa_encrypt
from RSADecryption import rsa_decrypt


def get_alphabet():
    use_capitals = input("Include capital letters? (y/n): ").lower() == "y"
    use_numbers = input("Include numbers? (y/n): ").lower() == "y"

    alphabet = "abcdefghijklmnopqrstuvwxyz "
    if use_capitals:
        alphabet += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if use_numbers:
        alphabet += "0123456789"
    return alphabet


def main():
    while True:
        print("\nRSA Encryption System")
        print("1. Generate Key Pair")
        print("2. Encrypt Message")
        print("3. Decrypt Message")
        print("4. Exit")

        choice = input("\nEnter your choice (1-4): ")

        if choice == "1":
            public_key, private_key = generate_keys()
            print("\nStore these keys safely!")
            print(f"Public Key (n,e): {public_key}")
            print(f"Private Key (n,d): {private_key}")

        elif choice == "2":
            alphabet = get_alphabet()
            rsa_encrypt(alphabet)

        elif choice == "3":
            rsa_decrypt()

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
