alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
digits = '0123456789'

def crypt(text, key):
    text = ''.join(l for l in text if l.isalpha())                      # чистим строку всех символов
    shift = key[0:2]                                                    # смещение
    scale_of_notation = int(key[2:4])                                        # система счисления
    text_key = key[4:]                                                  # текстовый ключ

    # шифр Виженера
    key_length = len(text_key)
    key_as_int = [alphabet.index(i) for i in text_key]
    plaintext_int = [alphabet.index(i) for i in text]
    ciphertext = ''
    for i in range(len(plaintext_int)):
        value = (plaintext_int[i] + key_as_int[i % key_length]) % 33
        ciphertext += alphabet[value]

    # переводим в цифры
    digittext = ''
    for letter in ciphertext:
        if len(str(alphabet.index(letter))) == 1:
            a = '0' + str(alphabet.index(letter))
        else:
            a = f'{alphabet.index(letter)}'
        digittext += a

    # сдвигаем на число
    shift_digittext = ''
    for digit in digittext:
        shift_digittext += digits[(int(digit) + int(shift)) % 10]



    # переводим в СС
    shift_digittext = int(shift_digittext, 10) if isinstance(shift_digittext, str) else shift_digittext
    alphabet_to_convert = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    convert_digittext = ''
    while shift_digittext > 0:
        shift_digittext, m = divmod(shift_digittext, scale_of_notation)
        convert_digittext += alphabet_to_convert[m]



    # переводим в буквы
    return_to_letters = []
    letters = {
        'A': '10',
        'B': '11',
        'C': '12',
        'D': '13',
        'E': '14',
        'F': '15',
        'G': '16',
        'H': '17',
        'I': '18',
        'J': '19',
        'K': '20',
        'L': '21',
        'M': '22',
        'N': '23',
        'O': '24',
        'P': '25',
        'Q': '26',
        'R': '27',
        'S': '28',
        'T': '29',
        'U': '30',
        'V': '31',
        'W': '32',
        'X': '33',
        'Y': '34',
        'Z': '35'
    }
    reverse_letters = {
        v: k for k, v in letters.items()
    }
    for i in convert_digittext[::-1]:

        if i in letters:
            return_to_letters.append(letters.get(i))
        else:
            return_to_letters.append(alphabet[int(i)])

    change_letters = []
    for i, j in enumerate(return_to_letters):
        l = reverse_letters.get(j)
        if l:
            change_letters.append(l)
        else:
            change_letters.append(j)
        # for k, v in reverse_letters.items():
        #
        #     if j in k:
        #         j = reverse_letters[k]
    return change_letters


def decrypt(text, key):
    text = ''.join(l for l in text if l.isalpha())  # чистим строку всех символов
    shift = key[0:2]  # смещение
    scale_of_notation = int(key[2:4])  # система счисления
    text_key = key[4:]

    # возвращаем в цифры
    return_to_digits = ''
    for i in text:
        return_to_digits += str(alphabet.index(i))


    # переводим в обратную СС
    number = int(return_to_digits, int(scale_of_notation)) if isinstance(return_to_digits, str) else return_to_digits

    alphabet_to_convert = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    convert_digittext = ''
    while number > 0:
        number, m = divmod(number, 10)
        convert_digittext += alphabet_to_convert[m]
    convert_digittext = int(convert_digittext[::-1])




    # сдвигаем на число обратно
    shift_digittext = ''
    for digit in str(convert_digittext):
        shift_digittext += digits[(int(digit) - int(shift)) % 10]


    # переводим в текст
    return_to_text = []
    for i in range(0, len(shift_digittext), 2):
        return_to_text.append(shift_digittext[i:i + 2])

    create_string = ''
    for i in return_to_text:
        create_string += alphabet[int(i) % 33]


    # виженер
    key_length = len(text_key)
    key_as_int = [alphabet.index(i) for i in text_key]
    ciphertext_int = [alphabet.index(i) for i in create_string]
    plaintext = ''
    for i in range(len(ciphertext_int)):
        value = (ciphertext_int[i] - key_as_int[i % key_length]) % 33
        plaintext += alphabet[value]
    return plaintext

print(*crypt('тестируем', '0716сейчас'), sep='')
print(decrypt('иFиADаADBбDззиё', '0716сейчас'))