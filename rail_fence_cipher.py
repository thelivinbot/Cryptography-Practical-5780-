def encrypt(text, key):
    rail = ['' for _ in range(key)]
    row = 0
    direction = 1

    for char in text:
        rail[row] += char

        if row == 0:
            direction = 1
        elif row == key - 1:
            direction = -1

        row += direction

    return ''.join(rail)


def decrypt(cipher, key):
    pattern = []
    row = 0
    direction = 1

    for _ in cipher:
        pattern.append(row)

        if row == 0:
            direction = 1
        elif row == key - 1:
            direction = -1

        row += direction

    rail = [''] * key
    index = 0

    for r in range(key):
        count = pattern.count(r)
        rail[r] = list(cipher[index:index + count])
        index += count

    result = ""

    for r in pattern:
        result += rail[r].pop(0)

    return result


text = input("Enter message: ")
key = int(input("Enter number of rails: "))

encrypted = encrypt(text, key)
print("Encrypted message:", encrypted)

decrypted = decrypt(encrypted, key)
print("Decrypted message:", decrypted)

#INPUT
Enter message: GITAM UNIVERSITY
Enter number of rails: 3

#OUTPUT
Encrypted message: GMISIA NVRIYTUET
Decrypted message: GITAM UNIVERSITY

