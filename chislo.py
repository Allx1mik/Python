print("Андреев В.К. группа 1408-05\n")

while True:
    user_input = input("Введите число: ")
    # Проверяем, состоит ли ввод только из цифр
    if user_input.isdigit():
        number = int(user_input)
        # Проверяем чётность
        if number % 2 == 0:
            print(f"Число {number} является четным")
        else:
            print(f"Число {number} не является четным")
        break
    else:
        print("Ошибка: введено не число")