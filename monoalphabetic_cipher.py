def encrypt(text, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for char in text.upper():
        if char.isalpha():
            index = alphabet.index(char)
            result += key[index]
        else:
            result += char

    return result


def decrypt(text, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for char in text.upper():
        if char.isalpha():
            index = key.index(char)
            result += alphabet[index]
        else:
            result += char

    return result


text = input("Enter message: ")
key = input("Enter 26-letter key: ").upper()

encrypted = encrypt(text, key)
print("Encrypted message:", encrypted)

decrypted = decrypt(encrypted, key)
print("Decrypted message:", decrypted)


#input
Enter message: GITAM UNIVERSITY
Enter 26-letter key: QWERTYUIOPASDFGHJKLZXCVBNM

#output
Encrypted message: UOZQD XFOCTKLOZN
Decrypted message: GITAM UNIVERSITY
