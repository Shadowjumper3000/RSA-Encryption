"""
RSA Decryption
This program decrypts a message using RSA decryption.
The user provides:
1. Private key components (n, d)
2. Encrypted message
The program outputs the original decrypted message.
"""


def split_into_chunks(text: str, chunk_size: int) -> list:
    """
    Split a string into chunks of specified size.

    Args:
        text (str): String to split
        chunk_size (int): Size of each chunk

    Returns:
        list: List of string chunks
    """
    return [text[i : i + chunk_size] for i in range(0, len(text), chunk_size)]


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


def rsa_decrypt(
    alphabet: str, modulus: int, private_exponent: int, encrypted_message: str
) -> str:
    """Decrypt an RSA encrypted message."""
    # Create number-to-character mapping
    num_to_char_map = {str(i).zfill(2): char for i, char in enumerate(alphabet)}

    # Calculate block size
    block_size = calculate_block_size(modulus, len(alphabet))

    try:
        # Split encrypted message into blocks
        encrypted_blocks = [
            encrypted_message[i : i + block_size]
            for i in range(0, len(encrypted_message), block_size)
        ]

        # Decrypt blocks
        decrypted_message = ""
        for block in encrypted_blocks:
            block_value = int(block)
            decrypted_block = str(pow(block_value, private_exponent, modulus))
            decrypted_block = decrypted_block.zfill(block_size)

            # Convert pairs of digits back to characters
            for i in range(0, len(decrypted_block), 2):
                pair = decrypted_block[i : i + 2]
                if pair in num_to_char_map:
                    decrypted_message += num_to_char_map[pair]

        # Remove padding added during encryption
        decrypted_message = decrypted_message.rstrip("0")
        return decrypted_message

    except (ValueError, KeyError) as e:
        raise ValueError(f"Decryption failed: {str(e)}")
