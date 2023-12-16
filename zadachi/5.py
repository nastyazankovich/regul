# Задача №5
# Разработай скрипт на Python, использующий
# регулярные выражения для обработки текстовых данных.
# 1.	Реализуй поиск и извлечение информации
# из текстовых данных (например, адресов
# электронной почты, номеров телефонов,
# ссылок на сайты и т.д.).
# 2.	Реализуй фильтрацию текстовых данных по
# заданным критериям (например, поиск и удаление
# лишних символов, замена определенных слов или
# фраз на другие и т.д.).
# 3.	Реализуй разбиение текстовых данных на
# отдельные слова или фразы для последующей обработки
# (например, подсчет количества повторяющихся слов или фраз в тексте).
# 4.	Реализуй проверку соответствия текстовых данных
# заданному шаблону (например, проверка корректности
# ввода пароля или логина на сайте).
import re

text = "sdfgh123@gmail.com,+375251234567,https://sdfgsdfg"

email = r'\w+@\w+\.\w+'
phone = r'\+\d{1,12}'
site = r'https?://[^\s]+'

emails = re.findall(email, text)
phones = re.findall(phone, text)
sites = re.findall(site, text)

print("Emails:", emails)
print("Phones:", phones)
print("Sites:", sites)

text = "Hello! What is your name?"

changed_text = re.sub('Hello','Hi', text)

print(changed_text)

text = "Hello! What is your name? Hello, hello"

words = re.findall(r'\w+', text.lower())
symbols = re.findall(r'[^\w\s]', text)

word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

symbol_counts = {}
for symbol in symbols:
    if symbol in symbol_counts:
        symbol_counts[symbol] += 1
    else:
        symbol_counts[symbol] = 1

print("Symbol counts:", symbol_counts)
print("Word counts:", word_counts)

password = 'Password_123'
pattern = r"[A-Z].{8,}"
if re.match(pattern, password):
    print("Пароль надежный")
else:
    print("Измените пароль")