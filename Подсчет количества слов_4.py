print("Андреев В.К. группа 1482-05\n")

# Ввод строки
text = input("Введите строку: ")
# Приводим к нижнему регистру
words = text.lower().split()
# Создаем словарь
word_count = {}
# Подсчитываем количество
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
# Результат
for word, count in word_count.items():
    print(f"{word}: {count}")


