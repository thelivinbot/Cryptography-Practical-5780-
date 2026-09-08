def encrypt(text, key):
    text = text.upper().replace(" ", "")

    if len(text) % 2 != 0:
        text += "X"

    result = ""

    for i in range(0, len(text), 2):
        x1 = ord(text[i]) - ord('A')
        x2 = ord(text[i + 1]) - ord('A')

        y1 = (key[0][0] * x1 + key[0][1] * x2) % 26
        y2 = (key[1][0] * x1 + key[1][1] * x2) % 26

        result += chr(y1 + ord('A'))
        result += chr(y2 + ord('A'))

    return result


def decrypt(text, key):
    determinant = (
        key[0][0] * key[1][1]
        - key[0][1] * key[1][0]
    ) % 26

    determinant_inverse = pow(determinant, -1, 26)

    inverse_key = [
        [
            (key[1][1] * determinant_inverse) % 26,
            (-key[0][1] * determinant_inverse) % 26
        ],
        [
            (-key[1][0] * determinant_inverse) % 26,
            (key[0][0] * determinant_inverse) % 26
        ]
    ]

    return encrypt(text, inverse_key)


text = input("Enter message: ")

key = [
    [3, 3],
    [2, 5]
]

encrypted = encrypt(text, key)
print("Encrypted message:", encrypted)

decrypted = decrypt(encrypted, key)
print("Decrypted message:", decrypted)

#INPUT
Enter message: GITAM UNIVERSITY

#OUTPUT
Encrypted message: QAFMSULOXKBUDHLH
Decrypted message: GITAMUNIVERSITYX
