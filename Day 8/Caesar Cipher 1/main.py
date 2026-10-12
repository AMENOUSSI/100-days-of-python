
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
    'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
    's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

def encrypt(original_text, shift_amount):
    encrypted_text = ""

    # Handle shifts larger than the alphabet
    shift_amount = shift_amount % 26

    for char in original_text:
        if char in alphabet:
            current_position = alphabet.index(char)
            new_position = (current_position + shift_amount) % 26
            encrypted_text += alphabet[new_position]
        else:
            # Keep spaces, numbers and punctuation unchanged
            encrypted_text += char

    print(f"Encrypted message: {encrypted_text}")


direction = input(
    "Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

print(f"Original text: {text}")

if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    encrypt(text, -shift)
else:
    print("Invalid choice! Type 'encode' or 'decode'.")
