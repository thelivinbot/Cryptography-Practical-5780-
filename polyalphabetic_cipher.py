def encrypt(text, key):
    result = ""
    key = key.upper()
    key_index = 0

    for char in text.upper():
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')

            encrypted = chr(
                (ord(char) - ord('A') + shift) % 26 + ord('A')
            )

            result += encrypted
            key_index += 1
        else:
            result += char

    return result


def decrypt(text, key):
    result = ""
    key = key.upper()
    key_index = 0

    for char in text.upper():
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')

            decrypted = chr(
                (ord(char) - ord('A') - shift) % 26 + ord('A')
            )

            result += decrypted
            key_index += 1
        else:
            result += char

    return result


text = input("Enter message: ")
key = input("Enter key: ")

encrypted = encrypt(text, key)
print("Encrypted message:", encrypted)

decrypted = decrypt(encrypted, key)
print("Decrypted message:", decrypted)

#input
Message: GITAM UNIVERSITY
Key: KEY

#output
Encrypted message: QMRKQ SXMTOVQSXW
Decrypted message: GITAM UNIVERSITY
