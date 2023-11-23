def main():
    alphabet = 'abcdefghijklmnopqrstuvwxyz '
    library = {}
    for i, letter in enumerate(alphabet):
        library[letter] = str(i).zfill(2)

    # Take input for public key values
    PublicKeyN = int(input("Enter n: "))
    PublicKeyE = int(input("Enter e: "))

    # Take input for the raw message
    rawMessage = input("Input your message here: ")

    # Check if the message is empty
    if len(rawMessage) == 0:
        print("Error: Empty message!")
        exit()

    # Convert the message to a string of numbers
    numericMessage = ""
    for char in rawMessage:
        if char in library:
            numericMessage += library[char]
        else:
            print(f"Error: Character '{char}' not in the alphabet!")
            exit()

    # Calculate the block size
    k = 0
    l = str(len(library))
    while int(l) <= PublicKeyN:
        l += str(len(library))
        k += 2
        if int(l) > PublicKeyN:
            break

    # Split the message into blocks
    blocks = [numericMessage[i:i + k] for i in range(0, len(numericMessage), k)]
    print(blocks)
    # Encode the message
    encodedMessage = ""
    for b in blocks:

        # Convert the block to an integer
        if len(b) < 3:
            b += str(len(alphabet)+1)
        blockInt = int(b)

        # Check if the block value exceeds the public key modulus
        if blockInt >= PublicKeyN:
            print("Error: Block value exceeds the public key modulus!")
            exit()

        # Perform RSA encryption
        encodedBlock = str(pow(blockInt, PublicKeyE, PublicKeyN))

        # Append the encoded block to the encoded message
        encodedMessage += encodedBlock.zfill(k)

    print(encodedMessage)

main()
