print("Андреев В.К. группа 1408-05\n")

while True:
    user_input = input("Введите число (или 'exit' для выхода): ")
    if user_input.lower() == 'exit':
        print("Выход из программы...")
        break
    # Проверка, является ли введенное значение числом
    if user_input.lstrip('-').isdigit():
        # Определяем количество цифр
        num_digits = len(user_input.lstrip('-'))  # Убираем знак минус для подсчета цифр
        print(f"В этом числе {num_digits} цифры.")
    else:
        print("Ошибка: данные не являются числом.")
