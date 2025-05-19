print("Андреев В.К. группа 1408-05\n")

name = input("Введите ваше Имя: ")
surname = input("Введите вашу Фамилию: ")
age = input("Введите ваш возраст: ")
  # с использованием метода format
  output_format = " Ваше имя: {}, Фамилия: {}, Возраст: {} лет.".format(name, surname, age)
 print(output_format)
  # с использованием f-string
  output_f_string = f" Ваше имя: {name}, Фамилия: {surname}, Возраст: {age} лет."
 print(output_f_string)
