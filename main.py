#!/usr/bin/env python3
"""
RSA Encryption CLI Tool

A command-line interface for RSA encryption operations including key generation,
message encryption, and message decryption with configurable alphabet sizes.
"""

import argparse
import sys
import json
from rsa_encryption import generate_keys, rsa_encrypt, rsa_decrypt


def get_alphabet(alphabet_type):
    """
    Get alphabet based on the specified type.

    Args:
        alphabet_type (str): Type of alphabet ('basic', 'extended', 'full', or 'custom')

    Returns:
        str: The alphabet string
    """
    alphabets = {
        "basic": "abcdefghijklmnopqrstuvwxyz ",
        "extended": "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ",
        "full": "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ",
        "numeric": "0123456789 ",
    }

    if alphabet_type in alphabets:
        return alphabets[alphabet_type]
    else:
        # Custom alphabet
        return alphabet_type


def generate_keys_command(args):
    """Generate RSA key pair and optionally save to files."""
    public_key, private_key = generate_keys()

    keys_data = {
        "public_key": {"n": public_key[0], "e": public_key[1]},
        "private_key": {"n": private_key[0], "d": private_key[1]},
    }

    if args.output:
        # Save keys to file
        with open(args.output, "w") as f:
            json.dump(keys_data, f, indent=2)
        print(f"Keys saved to {args.output}")
    else:
        # Print keys to stdout
        print("Generated RSA Key Pair:")
        print(f"Public Key (n, e): ({public_key[0]}, {public_key[1]})")
        print(f"Private Key (n, d): ({private_key[0]}, {private_key[1]})")
        print("\nJSON Format:")
        print(json.dumps(keys_data, indent=2))


def encrypt_command(args):
    """Encrypt a message using RSA encryption."""
    alphabet = get_alphabet(args.alphabet)

    # Load keys
    if args.key_file:
        with open(args.key_file, "r") as f:
            keys_data = json.load(f)
        n = keys_data["public_key"]["n"]
        e = keys_data["public_key"]["e"]
    else:
        n = args.n
        e = args.e

    if not n or not e:
        print(
            "Error: Public key (n, e) must be provided either via --key-file or --n and --e"
        )
        sys.exit(1)

    # Get message
    message = args.message or input("Enter message to encrypt: ")

    try:
        encrypted = rsa_encrypt(alphabet, n, e, message)
        print(f"Encrypted message: {encrypted}")

        if args.output:
            with open(args.output, "w") as f:
                f.write(encrypted)
            print(f"Encrypted message saved to {args.output}")

    except ValueError as error:
        print(f"Encryption error: {error}")
        sys.exit(1)


def decrypt_command(args):
    """Decrypt a message using RSA decryption."""
    alphabet = get_alphabet(args.alphabet)

    # Load keys
    if args.key_file:
        with open(args.key_file, "r") as f:
            keys_data = json.load(f)
        n = keys_data["private_key"]["n"]
        d = keys_data["private_key"]["d"]
    else:
        n = args.n
        d = args.d

    if not n or not d:
        print(
            "Error: Private key (n, d) must be provided either via --key-file or --n and --d"
        )
        sys.exit(1)

    # Get encrypted message
    if args.message:
        encrypted_message = args.message
    elif args.input:
        with open(args.input, "r") as f:
            encrypted_message = f.read().strip()
    else:
        encrypted_message = input("Enter encrypted message: ")

    try:
        decrypted = rsa_decrypt(alphabet, n, d, encrypted_message)
        print(f"Decrypted message: {decrypted}")

        if args.output:
            with open(args.output, "w") as f:
                f.write(decrypted)
            print(f"Decrypted message saved to {args.output}")

    except ValueError as error:
        print(f"Decryption error: {error}")
        sys.exit(1)


def alphabet_info_command(args):
    """Show information about available alphabets."""
    alphabets = {
        "basic": "abcdefghijklmnopqrstuvwxyz ",
        "extended": "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ",
        "full": "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ",
        "numeric": "0123456789 ",
    }

    print("Available alphabet types:")
    for name, alphabet in alphabets.items():
        print(f"  {name:10} ({len(alphabet):2} chars): {alphabet}")

    print("\nYou can also specify a custom alphabet as a string.")


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="RSA Encryption CLI Tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate keys and save to file
  python main.py generate-keys --output keys.json
  
  # Generate keys and print to console
  python main.py generate-keys
  
  # Encrypt with key file
  python main.py encrypt --key-file keys.json --message "hello world" --alphabet basic
  
  # Encrypt with explicit keys
  python main.py encrypt --n 1091218173 --e 65537 --message "hello" --alphabet basic
  
  # Decrypt with key file
  python main.py decrypt --key-file keys.json --message "123456789" --alphabet basic
  
  # Show alphabet information
  python main.py alphabet-info
        """,
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Generate keys command
    gen_parser = subparsers.add_parser("generate-keys", help="Generate RSA key pair")
    gen_parser.add_argument("--output", "-o", help="Output file for keys (JSON format)")

    # Encrypt command
    encrypt_parser = subparsers.add_parser("encrypt", help="Encrypt a message")
    encrypt_parser.add_argument("--message", "-m", help="Message to encrypt")
    encrypt_parser.add_argument(
        "--alphabet",
        "-a",
        default="basic",
        help="Alphabet type: basic, extended, full, numeric, or custom string",
    )
    encrypt_parser.add_argument("--key-file", "-k", help="JSON file containing keys")
    encrypt_parser.add_argument(
        "--n", type=int, help="Public key modulus (if not using key file)"
    )
    encrypt_parser.add_argument(
        "--e", type=int, help="Public key exponent (if not using key file)"
    )
    encrypt_parser.add_argument(
        "--output", "-o", help="Output file for encrypted message"
    )

    # Decrypt command
    decrypt_parser = subparsers.add_parser("decrypt", help="Decrypt a message")
    decrypt_parser.add_argument("--message", "-m", help="Encrypted message to decrypt")
    decrypt_parser.add_argument(
        "--input", "-i", help="Input file containing encrypted message"
    )
    decrypt_parser.add_argument(
        "--alphabet",
        "-a",
        default="basic",
        help="Alphabet type: basic, extended, full, numeric, or custom string",
    )
    decrypt_parser.add_argument("--key-file", "-k", help="JSON file containing keys")
    decrypt_parser.add_argument(
        "--n", type=int, help="Private key modulus (if not using key file)"
    )
    decrypt_parser.add_argument(
        "--d", type=int, help="Private key exponent (if not using key file)"
    )
    decrypt_parser.add_argument(
        "--output", "-o", help="Output file for decrypted message"
    )

    # Alphabet info command
    subparsers.add_parser("alphabet-info", help="Show available alphabet types")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    if args.command == "generate-keys":
        generate_keys_command(args)
    elif args.command == "encrypt":
        encrypt_command(args)
    elif args.command == "decrypt":
        decrypt_command(args)
    elif args.command == "alphabet-info":
        alphabet_info_command(args)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
