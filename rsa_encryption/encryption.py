"""
RSA Encryption
This module encrypts a message using RSA encryption with improved block handling.
"""

from .utils import calculate_block_size, create_char_mappings, split_into_chunks


def rsa_encrypt(alphabet: str, modulus: int, public_exponent: int, message: str) -> str:
    """
    Encrypt a message using RSA with improved padding and block handling.

    Args:
        alphabet (str): The alphabet to use for encoding
        modulus (int): The RSA modulus (n)
        public_exponent (int): The RSA public exponent (e)
        message (str): The message to encrypt

    Returns:
        str: The encrypted message as a string of digits

    Raises:
        ValueError: If message is empty or contains invalid characters
    """
    if len(message) == 0:
        raise ValueError("Error: Empty message!")

    # Create character mappings
    char_to_num_map, _ = create_char_mappings(alphabet)

    # Convert message to numeric form
    numeric_message = ""
    for char in message:
        if char not in char_to_num_map:
            raise ValueError(f"Error: Character '{char}' not in the alphabet!")
        numeric_message += char_to_num_map[char]

    # Calculate safe block size
    block_size = calculate_block_size(modulus, len(alphabet))

    # Split message into blocks
    blocks = split_into_chunks(numeric_message, block_size)

    # Encrypt each block
    encrypted_blocks = []
    for block in blocks:
        # Pad with first alphabet character (index 00) instead of zeros
        if len(block) < block_size:
            padding_char = "00"  # Use alphabet[0] index
            block = block.ljust(block_size, padding_char[-1])

        block_value = int(block)
        if block_value >= modulus:
            raise ValueError("Error: Block value exceeds modulus!")

        encrypted_block = pow(block_value, public_exponent, modulus)
        # Use consistent block size for encrypted output
        encrypted_blocks.append(str(encrypted_block).zfill(len(str(modulus))))

    return "".join(encrypted_blocks)
