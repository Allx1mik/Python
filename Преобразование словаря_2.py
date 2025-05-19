print("Андреев В.К. группа 1482-05\n")

dct = {1: 11, 2: 22, 3: 33, 4: 4, 5: 33, 6: 1}

# Создаем множества
keys_set = set(dct.keys())
values_set = set(dct.values())
# Объединяем множества
union_set = keys_set.union(values_set)
# Выводим результаты
print("Множество ключей:", keys_set)
print("Множество значений:", values_set)
print("Объединение множеств:", union_set)
