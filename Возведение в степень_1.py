print("Андреев В.К. группа 1408-05\n")

def process_list(numbers, power):
    result = []
    for element in numbers:
        try:
            # Пробуем преобразовать
            num = float(element)
            # Проверяем, является ли число целым
            if num.is_integer():
                num = int(num)
            # Возводим в степень
            processed = num ** power
            result.append(processed)
        except ValueError:
            # Если не число - умножаем строку на степень
            processed = element * power
            result.append(processed)
    return result
# Получаем ввод
input_numbers = input("Введите числа через пробел: ").split()
power_input = input("Введите степень: ")
try:
    power = int(power_input)
except ValueError:
    try:
        power = float(power_input)
    except ValueError:
        print("Степень должна быть числом!")
        exit()
# Обрабатываем список
output = process_list(input_numbers, power)
# Выводим результат
print("Вывод:", " ".join(map(str, output)))