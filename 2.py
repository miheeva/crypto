alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
alphabet_upper = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
digits = '0123456789'
word = input()

def crypt(word):
    for i in word:
        if i in alphabet:
            print(alphabet[(alphabet.index(i) + 3) % 33], end='')
        elif i in alphabet_upper:
            print(alphabet_upper[(alphabet_upper.index(i) + 3) % 33], end='')
        elif i in digits:
            print(digits[(digits.index(i) + 3) % 10], end='')

def decrypt(word):
    for i in word:
        if i in alphabet:
            print(alphabet[(alphabet.index(i) + 3) % 33], end='')
        elif i in alphabet_upper:
            print(alphabet_upper[(alphabet_upper.index(i) + 3) % 33], end='')
        elif i in digits:
            print(digits[(digits.index(i) + 3) % 10], end='')

crypt(word)