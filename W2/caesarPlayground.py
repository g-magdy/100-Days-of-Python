alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encrypt(message, shift):
    encoded_message = ""
    for letter in message:
        current_alphabetical_index = alphabet.index(letter) # new idea - get the index of an element : listName.index(elementValue)
        new_alphabetical_index = (current_alphabetical_index + shift) % len(alphabet)
        encoded_message += alphabet[new_alphabetical_index]
    print(encoded_message)

def decrypt(text, shift):
    decrypted_message = ""
    for letter in text:
        current_index = alphabet.index(letter)
        new_index = (current_index - shift) % len(alphabet)
        decrypted_message += alphabet[new_index]
    print(decrypted_message)
