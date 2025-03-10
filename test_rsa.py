import unittest
from RSAKeyGeneration import generate_keys, gcd, PRIME_NUMBERS
from RSAEncryption import rsa_encrypt
from RSADecryption import rsa_decrypt


class TestRSASystem(unittest.TestCase):
    def test_gcd(self):
        """Test Greatest Common Divisor function"""
        self.assertEqual(gcd(48, 18), 6)
        self.assertEqual(gcd(54, 24), 6)
        self.assertEqual(gcd(7, 13), 1)
        self.assertEqual(gcd(28, 0), 28)

    def test_key_generation(self):
        """Test RSA key pair generation"""
        public_key, private_key = generate_keys()
        n, e = public_key
        n_priv, d = private_key

        # Test if both keys share the same n
        self.assertEqual(n, n_priv)

        # Test if n is product of two primes from our list
        factors = [p for p in PRIME_NUMBERS if n % p == 0]
        self.assertEqual(len(factors), 2)
        p, q = factors

        # Test if public exponent is valid
        self.assertIn(e, [3, 5, 17, 257, 65537])

        # Test if e and totient are coprime
        totient = (p - 1) * (q - 1)
        self.assertEqual(gcd(e, totient), 1)

        # Test if d is valid private exponent
        self.assertEqual((d * e) % totient, 1)

    def test_encryption_decryption_cycle(self):
        """Test complete encryption-decryption cycle"""
        for _ in range(5):  # Test multiple times with different keys
            # Test data
            alphabet = "abcdefghijklmnopqrstuvwxyz "
            test_message = "hello world"  # More realistic test message

            # Get keys from the key generation function - this is how it would be used in practice
            public_key, private_key = generate_keys()
            modulus, pub_exp = public_key
            _, priv_exp = private_key

            try:
                # Encrypt message
                encrypted = rsa_encrypt(alphabet, modulus, pub_exp, test_message)
                self.assertIsNotNone(encrypted)
                self.assertTrue(len(encrypted) > 0)
                self.assertNotEqual(
                    encrypted, test_message
                )  # Ensure encryption happened

                # Decrypt message
                decrypted = rsa_decrypt(alphabet, modulus, priv_exp, encrypted)
                self.assertEqual(decrypted, test_message)  # Compare exact strings

            except ValueError as e:
                self.fail(
                    f"Encryption/Decryption failed with keys (n={modulus}, e={pub_exp}): {str(e)}"
                )

    def test_encryption_invalid_input(self):
        """Test encryption with invalid input"""
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        with self.assertRaises(ValueError):
            rsa_encrypt(alphabet, 391, 7, "")  # Empty message
        with self.assertRaises(ValueError):
            rsa_encrypt(alphabet, 391, 7, "Hello!")  # Invalid character

    def test_long_message_encryption_decryption(self):
        """Test encryption and decryption of a longer message"""
        # Test data with full alphabet
        alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "
        test_message = "The Quick Brown Fox Jumps Over The Lazy Dog 123"

        # Get keys from the key generation function - this is how it would be used in practice
        public_key, private_key = generate_keys()
        modulus, pub_exp = public_key
        _, priv_exp = private_key

        try:
            # Encrypt long message
            encrypted = rsa_encrypt(alphabet, modulus, pub_exp, test_message)
            self.assertIsNotNone(encrypted)
            self.assertTrue(len(encrypted) > 0)
            self.assertNotEqual(encrypted, test_message)

            # Decrypt long message
            decrypted = rsa_decrypt(alphabet, modulus, priv_exp, encrypted)
            self.assertEqual(decrypted, test_message)
            self.assertEqual(len(decrypted), len(test_message))

        except ValueError as e:
            self.fail(
                f"Encryption/Decryption failed with keys (n={modulus}, e={pub_exp}): {str(e)}"
            )

    def test_encryption_specific(self):
        """Test encryption functionality specifically"""
        # Test data
        alphabet = "abcdefghijklmnopqrstuvwxyz "
        test_cases = [
            "hello",  # Basic test
            "hello world",  # With space
            "zzz",  # Edge case - highest values
            "aaa",  # Edge case - lowest values
            "a b c",  # Multiple spaces
        ]

        # Get keys from generation
        public_key, _ = generate_keys()
        modulus, pub_exp = public_key

        for test_message in test_cases:
            try:
                # Encrypt message
                encrypted = rsa_encrypt(alphabet, modulus, pub_exp, test_message)

                # Verify encryption
                self.assertIsNotNone(encrypted)
                self.assertTrue(len(encrypted) > 0)
                self.assertNotEqual(encrypted, test_message)
                self.assertTrue(
                    all(c.isdigit() for c in encrypted)
                )  # Should be numeric

            except ValueError as e:
                self.fail(f"Encryption failed for '{test_message}': {str(e)}")

    def test_decryption_specific(self):
        """Test decryption functionality specifically"""
        alphabet = "abcdefghijklmnopqrstuvwxyz "
        test_message = "test message"

        # Generate keys
        public_key, private_key = generate_keys()
        modulus, pub_exp = public_key
        _, priv_exp = private_key

        # Create known encrypted values
        encrypted = rsa_encrypt(alphabet, modulus, pub_exp, test_message)

        try:
            # Test normal decryption
            decrypted = rsa_decrypt(alphabet, modulus, priv_exp, encrypted)
            self.assertEqual(decrypted, test_message)

            # Test decryption with padded input
            padded_encrypted = "0" + encrypted
            with self.assertRaises(ValueError):
                rsa_decrypt(alphabet, modulus, priv_exp, padded_encrypted)

            # Test decryption with modified input
            if len(encrypted) > 0:
                modified = str(int(encrypted[0]) + 1) + encrypted[1:]
                with self.assertRaises(ValueError):
                    rsa_decrypt(alphabet, modulus, priv_exp, modified)

        except ValueError as e:
            self.fail(f"Decryption test failed: {str(e)}")


if __name__ == "__main__":
    unittest.main()
