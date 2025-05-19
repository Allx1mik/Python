print("Андреев В.К. группа 1482-05\n")

def get_common_elements():
    try:
        # Ввод первого списка
        first_list_input = input("Введите первый список (числа через пробел): ")
        first_list = list(map(int, first_list_input.split()))
        # Ввод второго списка
        second_list_input = input("Введите второй список (числа через пробел): ")
        second_list = list(map(int, second_list_input.split()))
        # Находим общие элементы
        common_elements = set(first_list) & set(second_list)
        # Вывод результата
        if common_elements:
            print("Общие элементы:", ' '.join(map(str, common_elements)))
        else:
            print("Нет общих элементов.")
    except ValueError:
        print("Ошибка: Пожалуйста, убедитесь, что вы вводите только числа, разделенные пробелами.")
if __name__ == "__main__":
    get_common_elements()


