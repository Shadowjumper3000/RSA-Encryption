def create_alphabet_library():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    library = {}
    for i, letter in enumerate(alphabet):
        library[str(i).zfill(2)] = letter
    return library

def split_string(string, n):
    return [string[i:i+n] for i in range(0, len(string), n)]

def main():
    # Create Alphabet Library
    alphabet_library = create_alphabet_library()

    # Get Private Key
    PrivateKeyN = int(input("Enter n: "))
    PrivateKeyD = int(input("Enter d: "))

    # Get encoded message as list of ints
    encodedMessage = [str(i).zfill(4) for i in input("Enter encoded message: ").split()]
    if len(encodedMessage[0]) > 4:
        encodedMessage = [int(encodedMessage[0][i:i+4]) for i in range(0, len(encodedMessage[0]), 4)]

    decodedMessage = ""
    for i in encodedMessage:
        # Decrypt the block and convert it to a string
        decryptedBlock = str(pow(int(i), PrivateKeyD, PrivateKeyN))

        # Split the decrypted block into pairs of two characters
        pairs = split_string(str(decryptedBlock).zfill(4), 2)
        # Convert each pair to its corresponding letter using the alphabet library
        for pair in pairs:
            decodedMessage += alphabet_library[pair]
            
    print(decodedMessage)

main()
