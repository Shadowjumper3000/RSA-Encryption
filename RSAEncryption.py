"""
RSA Encryption
This program encrypts a message using RSA encryption. The user is prompted to enter
the public key (n, e) and the raw message. The program then encrypts the message
and outputs the encoded message.
"""


def calculate_block_size(modulus: int, alphabet_length: int) -> int:
    """
    Calculate the maximum safe block size for the given modulus.

    Args:
        modulus (int): The RSA modulus (n)
        alphabet_length (int): Length of the alphabet being used

    Returns:
        int: Maximum safe block size in digits
    """
    block_size = 2
    while True:
        test_value = int("9" * block_size)
        if test_value >= modulus:
            return block_size - 2
        block_size += 2


def rsa_encrypt(alphabet: str, modulus: int, public_exponent: int, message: str) -> str:
    """Encrypt a message using RSA."""
    # Create character-to-number mapping
    char_to_num_map = {char: str(i).zfill(2) for i, char in enumerate(alphabet)}

    if len(message) == 0:
        raise ValueError("Error: Empty message!")

    # Convert message to numeric form
    numeric_message = ""
    for char in message:
        if char not in char_to_num_map:
            raise ValueError(f"Error: Character '{char}' not in the alphabet!")
        numeric_message += char_to_num_map[char]

    # Calculate safe block size
    block_size = calculate_block_size(modulus, len(alphabet))

    # Split message into blocks
    blocks = [
        numeric_message[i : i + block_size]
        for i in range(0, len(numeric_message), block_size)
    ]

    # Encrypt each block
    encrypted_blocks = []
    for block in blocks:
        if len(block) < block_size:
            block = block.ljust(block_size, "0")  # Pad with zeros
        block_value = int(block)
        if block_value >= modulus:
            raise ValueError("Error: Block value exceeds modulus!")
        encrypted_block = pow(block_value, public_exponent, modulus)
        encrypted_blocks.append(str(encrypted_block).zfill(block_size))

    return "".join(encrypted_blocks)
