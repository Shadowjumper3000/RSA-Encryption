# RSA Encryption System

A Python implementation of RSA encryption that demonstrates public-key cryptography concepts.

## Features

- Generate RSA key pairs
- Encrypt messages using public keys
- Decrypt messages using private keys
- Support for:
  - Lowercase letters
  - Capital letters (optional)
  - Numbers (optional)
  - Spaces

## Usage

Run the main program:
```bash
python main.py
```

The program provides an interactive menu with these options:
1. Generate Key Pair - Creates new public/private key pair
2. Encrypt Message - Encrypts text using a public key
3. Decrypt Message - Decrypts text using a private key
4. Exit

## Project Structure

- [`main.py`](main.py) - Main interface and menu system
- [`RSAKeyGeneration.py`](RSAKeyGeneration.py) - Handles key pair generation
- [`RSAEncryption.py`](RSAEncryption.py) - Implements message encryption
- [`RSADecryption.py`](RSADecryption.py) - Implements message decryption

## Running Tests

```bash
python -m unittest test_rsa.py -v
```

## Technical Details

The implementation includes:
- Prime number validation
- GCD calculation for key generation
- Modular exponentiation for encryption/decryption
- Block-based message processing

## Requirements

- Python 3.6+

## License

Free use - do whatever you want with it.

## Notes

This is an educational project demonstrating RSA concepts. Not recommended for production use.
