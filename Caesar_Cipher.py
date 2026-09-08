def encrypt(text, key):
    result = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - ord('A') + key) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') + key) % 26 + ord('a'))
        else:
            result += char

    return result


def decrypt(text, key):
    return encrypt(text, -key)


text = input("Enter message: ")
key = int(input("Enter key: "))

encrypted = encrypt(text, key)
print("Encrypted message:", encrypted)

decrypted = decrypt(encrypted, key)
print("Decrypted message:", decrypted)
#input
Enter message: GITAM UNIVERSITY
Enter key: 6
#output
Enter message: GITAM UNIVERSITY
Enter key: 6
Encrypted message: MOZGS ATOBKXYOZE
Decrypted message: GITAM UNIVERSITY
