import random

symbols = [r"qazwsxedcrfvtgbyhnujmik,ol.;p['/]\\1234567890-=!@#$%^&*()_+{}|:?><"]

word = ""

while len(word) < 5:
    word += random.choice(symbols)

print(word)
