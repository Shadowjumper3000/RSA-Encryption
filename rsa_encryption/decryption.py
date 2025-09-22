"""
RSA Decryption
This module decrypts a message using RSA decryption with improved padding removal.
"""

from .utils import calculate_block_size, create_char_mappings, split_into_chunks


def rsa_decrypt(
    alphabet: str, modulus: int, private_exponent: int, encrypted_message: str
) -> str:
    """
    Decrypt an RSA encrypted message with improved padding handling.

    Args:
        alphabet (str): The alphabet used for encoding
        modulus (int): The RSA modulus (n)
        private_exponent (int): The RSA private exponent (d)
        encrypted_message (str): The encrypted message to decrypt

    Returns:
        str: The decrypted message

    Raises:
        ValueError: If decryption fails or input is invalid
    """
    # Create character mappings
    _, num_to_char_map = create_char_mappings(alphabet)

    # Calculate block size
    block_size = calculate_block_size(modulus, len(alphabet))

    # Calculate encrypted block size
    encrypted_block_size = len(str(modulus))

    try:
        # Split encrypted message into blocks
        encrypted_blocks = split_into_chunks(encrypted_message, encrypted_block_size)

        # Decrypt blocks
        decrypted_message = ""
        for block in encrypted_blocks:
            if not block:
                continue

            block_value = int(block)
            decrypted_block = str(pow(block_value, private_exponent, modulus))
            decrypted_block = decrypted_block.zfill(block_size)

            # Convert pairs of digits back to characters
            for i in range(0, len(decrypted_block), 2):
                pair = decrypted_block[i : i + 2]
                if pair in num_to_char_map:
                    char = num_to_char_map[pair]
                    # Only add non-padding characters or preserve intentional nulls
                    if char != alphabet[0] or i < len(decrypted_block) - 2:
                        decrypted_message += char

        # Remove trailing padding characters (first character of alphabet)
        decrypted_message = decrypted_message.rstrip(alphabet[0])
        return decrypted_message

    except (ValueError, KeyError) as e:
        raise ValueError(f"Decryption failed: {str(e)}")
