def columnar_transposition(text, key):
    columns = len(key)
    rows = (len(text) + columns - 1) // columns

    text += 'X' * (rows * columns - len(text))

    matrix = []

    for i in range(0, len(text), columns):
        matrix.append(list(text[i:i + columns]))

    order = sorted(range(columns), key=lambda x: key[x])

    result = ""

    for col in order:
        for row in range(rows):
            result += matrix[row][col]

    return result


def inverse_columnar_transposition(text, key):
    columns = len(key)
    rows = len(text) // columns

    order = sorted(range(columns), key=lambda x: key[x])

    matrix = [[''] * columns for _ in range(rows)]

    index = 0

    for col in order:
        for row in range(rows):
            matrix[row][col] = text[index]
            index += 1

    result = ""

    for row in range(rows):
        for col in range(columns):
            result += matrix[row][col]

    return result


def encrypt(text, key1, key2):
    first = columnar_transposition(text, key1)
    second = columnar_transposition(first, key2)

    return second


def decrypt(text, key1, key2):
    first = inverse_columnar_transposition(text, key2)
    second = inverse_columnar_transposition(first, key1)

    return second


text = input("Enter message: ")
key1 = input("Enter first key: ")
key2 = input("Enter second key: ")

encrypted = encrypt(text, key1, key2)
print("Encrypted message:", encrypted)

decrypted = decrypt(encrypted, key1, key2)
print("Decrypted message:", decrypted)

#INPUT
Enter message: GITAMUNIVERSITY
Enter first key: ZEBRA
Enter second key: TIGER

#OUTPUT
Encrypted message: TSUYNGEITIARMIV
Decrypted message: GITAMUNIVERSITY
