def create_alphabet_library():
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 '
    library = {}
    for i, letter in enumerate(alphabet):
        library[letter] = str(i + 1).zfill(2)
    return library

def main():
    # Create Alphabet Library
    alphabet_library = create_alphabet_library()

    # Take input for public key values
    publicKeyN = int(input("Enter n: "))
    publicKeyE = int(input("Enter e: "))

    # Take input for the raw message
    rawMessage = input("Input your message here: ")

    # Check if the message is empty
    if len(rawMessage) == 0:
        print("Error: Empty message!")
        exit()

    # Convert the message to a string of numbers
    numericMessage = ""
    for char in rawMessage:
        if char in alphabet_library:
            numericMessage += alphabet_library[char]
        else:
            print(f"Error: Character '{char}' not in the alphabet!")
            exit()

    # Calculate the block size
    k = 0
    l = "25"
    while int(l) <= publicKeyN:
        l += "25"
        k += 2
        if int(l) > publicKeyN:
            break

    # Split the message into blocks
    blocks = [numericMessage[i:i + k] for i in range(0, len(numericMessage), k)]

    # Encode the message
    encodedMessage = ""
    for b in blocks:
        
        # Convert the block to an integer
        blockInt = int(b)

        # Check if the block value exceeds the public key modulus
        if blockInt >= publicKeyN:
            print("Error: Block value exceeds the public key modulus!")
            exit()

        # Perform RSA encryption
        encodedBlock = pow(blockInt, publicKeyE, publicKeyN)

        # Append the encoded block to the encoded message
        encodedMessage += str(encodedBlock).zfill(k)

    print(encodedMessage)

main()
