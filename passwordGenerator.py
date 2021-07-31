from random import randint

def passwordGenerator(passLen, passQ, filepath):
    symbols: str = '1234567890QWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()_+=/?' + 'QWERTYUIOPASDFGHJKLZXCVBNM'.lower()
    file = open(filepath, 'w', encoding='utf-8')
    for i in range(passQ):
        password: str = ''
        for i in range(passLen):
            password += symbols[randint(0, len(symbols) - 1)]
        file.write(password + '\n')
    
    file.close()