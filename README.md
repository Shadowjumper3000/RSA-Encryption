# RSA Encryption Tool

A Python implementation of RSA encryption for educational purposes with both CLI and library interfaces, demonstrating public-key cryptography concepts.
## ToDo
- [] Fix padding being stripped on decryption for single block messages
- [] Add more prime numbers to the prime list for key generation
## Features

- **Command Line Interface**: Easy-to-use CLI for all RSA operations
- **RSA Key Generation**: Generate secure RSA key pairs using randomly selected prime numbers
- **Message Encryption**: Encrypt text messages using RSA public keys
- **Message Decryption**: Decrypt encrypted messages using RSA private keys
- **Flexible Alphabets**: Support for various character sets:
  - `basic`: Lowercase letters and space (27 chars)
  - `extended`: Lowercase, uppercase letters and space (53 chars)
  - `full`: Letters, numbers, and space (63 chars)
  - `numeric`: Numbers and space (11 chars)
  - Custom: Any custom alphabet string
- **File I/O**: Save/load keys and messages to/from files
- **Block Processing**: Intelligent block-based message handling for longer texts
- **Comprehensive Testing**: Full test suite with unit and integration tests

## Installation

```bash
git clone https://github.com/Shadowjumper3000/RSA-Encryption.git
cd RSA-Encryption
```

## CLI Usage

The main interface is through the command line using `main.py`:

### Generate Keys

```bash
# Generate keys and display them
python main.py generate-keys

# Save keys to a JSON file
python main.py generate-keys --output keys.json
```

### Encrypt Messages

```bash
# Encrypt with saved keys (interactive message input)
python main.py encrypt --key-file keys.json --alphabet basic

# Encrypt with explicit message and keys
python main.py encrypt --key-file keys.json --message "hello world" --alphabet basic

# Encrypt with explicit key values
python main.py encrypt --n 1091218173 --e 65537 --message "hello" --alphabet basic

# Save encrypted message to file
python main.py encrypt --key-file keys.json --message "secret" --alphabet basic --output encrypted.txt
```

### Decrypt Messages

```bash
# Decrypt with saved keys (interactive input)
python main.py decrypt --key-file keys.json --alphabet basic

# Decrypt explicit message
python main.py decrypt --key-file keys.json --message "123456789" --alphabet basic

# Decrypt from file
python main.py decrypt --key-file keys.json --input encrypted.txt --alphabet basic

# Decrypt with explicit key values
python main.py decrypt --n 1091218173 --d 987654321 --message "123456789" --alphabet basic
```

### Alphabet Information

```bash
# Show available alphabet types
python main.py alphabet-info
```

## Library Usage

You can also use the package as a Python library:

```python
from rsa_encryption import generate_keys, rsa_encrypt, rsa_decrypt

# Generate RSA key pair
public_key, private_key = generate_keys()
modulus, public_exp = public_key
_, private_exp = private_key

# Define alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz "

# Encrypt a message
message = "hello world"
encrypted = rsa_encrypt(alphabet, modulus, public_exp, message)
print(f"Encrypted: {encrypted}")

# Decrypt the message
decrypted = rsa_decrypt(alphabet, modulus, private_exp, encrypted)
print(f"Decrypted: {decrypted}")
```
### Extended Alphabet Example

```python
from rsa_encryption import generate_keys, rsa_encrypt, rsa_decrypt

# Extended alphabet with uppercase, lowercase, numbers, and space
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "

public_key, private_key = generate_keys()
modulus, public_exp = public_key
_, private_exp = private_key

message = "Hello World 123"
encrypted = rsa_encrypt(alphabet, modulus, public_exp, message)
decrypted = rsa_decrypt(alphabet, modulus, private_exp, encrypted)

assert decrypted == message  # Perfect round-trip
```

## Project Structure

```
RSA-Encryption/
├── main.py                  # CLI interface
├── rsa_encryption/          # Main package
│   ├── __init__.py         # Package interface
│   ├── key_generation.py   # RSA key generation
│   ├── encryption.py       # Message encryption
│   ├── decryption.py       # Message decryption
│   └── utils.py            # Utility functions
├── tests/                  # Comprehensive test suite
│   ├── test_key_generation.py
│   ├── test_encryption.py
│   ├── test_decryption.py
│   └── test_integration.py
├── requirements.txt        # Dependencies
└── README.md              # This file
```

## Running Tests

Run the complete test suite:
```bash
python -m unittest discover tests -v
```

Run specific test modules:
```bash
python -m unittest tests.test_encryption -v
python -m unittest tests.test_decryption -v
python -m unittest tests.test_integration -v
```

## Technical Details

### Key Generation
- Uses randomly selected prime numbers from a curated list
- Implements the Extended Euclidean Algorithm for modular inverse calculation
- Generates keys with standard RSA public exponent (65537)

### Encryption/Decryption
- Character-to-number mapping using zero-padded indices
- Intelligent block size calculation based on modulus size
- Proper padding handling for block boundaries
- Error handling for invalid characters and malformed input

### Security Considerations
- **Educational Purpose**: This implementation is designed for learning RSA concepts
- **Not Production Ready**: Uses smaller prime numbers and lacks padding schemes like OAEP
- **No Side-Channel Protection**: Implementation doesn't protect against timing attacks

## Development

### Setting up Development Environment

```bash
# Clone the repository
git clone https://github.com/Shadowjumper3000/RSA-Encryption.git
cd RSA-Encryption

# Create virtual environment (optional)
python -m venv .venv
source .venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies (optional)
pip install -r requirements.txt
```

## Requirements

- Python 3.8 or higher
- No external runtime dependencies (pure Python implementation)

## License

This project is provided for educational purposes. Feel free to use, modify, and distribute as needed.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## Educational Note

This RSA implementation is designed specifically for educational purposes to demonstrate:
- Public-key cryptography concepts
- RSA algorithm mechanics
- Python package development best practices

For production applications, use established cryptographic libraries like `cryptography` or `PyCryptodome`.
