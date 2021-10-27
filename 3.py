alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

def encrypt(plaintext, key):
    plaintext = plaintext.replace(' ', '')
    key_length = len(key)
    key_as_int = [alphabet.index(i) for i in key]
    plaintext_int = [alphabet.index(i) for i in plaintext]
    ciphertext = ''
    for i in range(len(plaintext_int)):
        value = (plaintext_int[i] + key_as_int[i % key_length]) % 33
        ciphertext += alphabet[value]
    return ciphertext


def decrypt(ciphertext, key):
    key_length = len(key)
    key_as_int = [alphabet.index(i) for i in key]
    ciphertext_int = [alphabet.index(i) for i in ciphertext]
    plaintext = ''
    for i in range(len(ciphertext_int)):
        value = (ciphertext_int[i] - key_as_int[i % key_length]) % 33
        plaintext += alphabet[value]
    return plaintext

print(encrypt('прокрастинация', 'сейчас'))
print(decrypt('ъщыюаюлговшз', 'питон'))