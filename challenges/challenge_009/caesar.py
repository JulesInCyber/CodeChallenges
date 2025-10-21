def caesar_eccryption(message, shift):
    enc_message = ''

    for letter in message:
        if letter.isalpha():
            if letter.isupper():
                start = ord("A")
            else:
                start = ord("a")
            enc_letter = chr((ord(letter) - start + shift) % 26 + start)
            enc_message += enc_letter
        else:
            enc_message += letter
    return enc_message

print(caesar_eccryption("Hello World!", 13))