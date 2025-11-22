
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(original_text, shift_amount, endcode_or_decode):
    output = ""
    shift_amount = shift_amount % 26
    if endcode_or_decode == "decode":
        shift_amount *= -1
    for letter in original_text:

        if letter not in alphabet:
            output += letter
            continue
        current_position = alphabet.index(letter)

        shifted_position  = current_position + shift_amount

        output += alphabet[shifted_position]

    print(f"The {direction} result is: {output}")

caesar(text,shift,direction)