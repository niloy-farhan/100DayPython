alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(start_text, shift_amount, cipher_direction):
    encrypted = ""
    decrypted = ""

    if cipher_direction == "encode":
        for letter in start_text:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            new_letter = alphabet[new_position]
            encrypted += new_letter
        print(f"The encoded text is {encrypted}")

    elif cipher_direction == "decode":
        for letter in text:
            position = alphabet.index(letter)
            new_position = position - shift
            new_letter = alphabet[new_position]
            decrypted += new_letter
        print(f"The encoded text is {decrypted}")
    else:
        print("Invalid Entry!")


caesar(text, shift, direction)