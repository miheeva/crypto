import random
cipher = {
    'а': ['21', '40', '10'],
    'б': ['37', '26', '03'],
    'в': ['14', '63', '71'],
    'г': ['22', '47', '82'],
    'д': ['01', '31', '15'],
    'е': ['24', '83', '70'],
    'ё': ['94', '98', '96'],
    'ж': ['62', '88', '11'],
    'з': ['73', '30', '55'],
    'и': ['46', '02', '90'],
    'й': ['97', '99', '95'],
    'к': ['23', '91', '69'],
    'л': ['12', '72', '38'],
    'м': ['08', '32', '61'],
    'н': ['27', '77', '54'],
    'о': ['53', '68', '09'],
    'п': ['35', '60', '84'],
    'р': ['04', '44', '45'],
    'с': ['20', '52', '89'],
    'т': ['13', '39', '67'],
    'у': ['59', '07', '93'],
    'ф': ['25', '49', '76'],
    'х': ['75', '33', '18'],
    'ц': ['43', '85', '51'],
    'ч': ['19', '58', '87'],
    'ш': ['29', '80', '66'],
    'щ': ['06', '50', '81'],
    'ъ': ['65', '34', '92'],
    'ы': ['74', '17', '42'],
    'ь': ['48', '56', '79'],
    'э': ['36', '78', '86'],
    'ю': ['28', '64', '05'],
    'я': ['16', '41', '57']
}

word = input().replace(' ', '').lower()


def crypt(word):
    for letter in word:
        if letter in cipher:
            value_key = cipher.get(letter)
            return random.choice(list(value_key))


def decrypt(word):
    words = []
    for i in range(0, len(word), 2):
        words.append(word[i:i+2])
    for elem in words:
        for k, v in cipher.items():
            if elem in v:
                return k