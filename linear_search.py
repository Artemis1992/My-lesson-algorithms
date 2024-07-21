# Линейный поиск — это простой алгоритм поиска, 
# который последовательно проверяет каждый элемент в списке до 
# тех пор, пока не найдет заданный элемент или не пройдет через 
# все элементы списка. Этот метод полезен для небольших или 
# неупорядоченных списков, где другие, более сложные алгоритмы, 
# могут быть избыточными O(n).

# Пример функции линейного поиска на Python:
def linear_search(lst, target):
    """
    Функция для поиска индекса заданного элемента в списке.

    :param lst: Список, в котором производится поиск.
    :param target: Элемент, который нужно найти.
    :return: Индекс элемента, если он найден, иначе -1.
    """

    for index in range(len(lst)):
        if lst[index] == target:
            return index
    return -1

numbers = [10, 23, 45, 70, 11, 15]
target_number = 70
index = linear_search(numbers, target_number)

if index != -1:
    print(f'Элемент найден на индексе {index}')
else:
    print('Элемент не найден')

# Разбираем этот код по элементно с примероми 

ppp = "\n---------------------------------------------------"
print(ppp)
# разбираем стрку for index in range(len(lst)):
# Пример 1: Удвоение каждого элемента списка

lst1 = [1, 2, 3, 4, 5]

for index in range(len(lst1)):
    lst1[index] *= 2
print(lst1) # [2, 4, 6, 8, 10]


ppp = "\n---------------------------------------------------"
print(ppp)
# Пример 2: Замена отрицательных чисел на их абсолютные значения

lst2 = [-1, -2, -3, -4, -5]

for index in range(len(lst2)):
    if lst2[index] < 0:
        lst2[index] = abs(lst2[index])
print(lst2) # [1, 2, 3, 4, 5]


ppp = "\n---------------------------------------------------"
print(ppp)
# Пример 3: Печать элементов списка в обратном порядке

lst3 = [10, 20, 30, 40, 50]

for index in range(len(lst3)):
    print(lst3[len(lst3) - 1 - index])
    # index = 0 -> len(lst) - 1 - 0 = 4 -> lst[4] = 50
    # index = 1 -> len(lst) - 1 - 1 = 3 -> lst[3] = 40
    # index = 2 -> len(lst) - 1 - 2 = 2 -> lst[2] = 30
    # index = 3 -> len(lst) - 1 - 3 = 1 -> lst[1] = 20
    # index = 4 -> len(lst) - 1 - 4 = 0 -> lst[0] = 10


ppp = "\n---------------------------------------------------"
print(ppp)
# Пример 4: Подсчет количества четных и нечетных чисел в списке

lst4 = list(range(30)) # Список от 0 до 29
even_count = 0
odd_count = 0

for index in range(len(lst4)):
    if index % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print(f"Количество четных {even_count}\nКоличество не четных {odd_count}")
# Количество четных 15
# Количество не четных 15


ppp = "\n---------------------------------------------------"
print(ppp)
# Пример 5: Создание нового списка с элементами, увеличенными на их индекс

lst5 = [61, 561, 123, 732, 281]

for index in range(len(lst5)):
    insert_update = lst5[index] + index
    print(f"Индекс {index} мы прибавили к числу {lst5[index]} результат {insert_update}")


ppp = "\n---------------------------------------------------"
print(ppp)
# Следующий пример строки кода - Поиск элемента в массиве. if lst6[index] == target1:
# Пример 1: Поиск элемента и вывод индекса 
lst6 = [41, 23, 83, 15]
target1 = 23

for index in range(len(lst6)):
    if lst6[index] == target1:
        print(f"Элемент найден на индексе {index}")
        # Вывод: Элемент найден на индексе 2
        
        
ppp = "\n---------------------------------------------------"
print(ppp)
# Пример 2: Поиск элемента и вывод значения

lst7 = [41, 23, 83, 15]
target2 = 15

for index in range(len(lst7)):
    
    if lst7[index] == target2:
        print(f"Значение найдено {target2}")
        break
else:
    print("Ничего не найдено")
        

ppp = "\n---------------------------------------------------"
print(ppp)
# Пример 3: Поиск элемента и изменение его значения

lst8 = [41, 23, 83, 15]
target3 = 83

for index in range(len(lst8)):
    if lst8[index] == target3:
        lst8[index] = 0 # Замена найденного элемента на 0
print(lst8)
# Вывод: [0, 74, 23, 94]


ppp = "\n---------------------------------------------------"
print(ppp)
# Пример 4: Поиск элемента и завершение цикла

lst9 = [41, 23, 83, 15]
target4 = 41

for index in range(len(lst9)):
    if lst9[index] == target4:
        print(f"Объект найден на индексе {index}")
        break # Завершение цикла после нахождения элемента
# Вывод: Элемент найден на индексе 1


ppp = "\n---------------------------------------------------"
print(ppp)
# Пример 5: Поиск элемента и удаление его из списка

lst10 = [41, 23, 83, 15]
target5 = 41

for index in range(len(lst10)):
    if lst10[index] == target5:
        del lst10[index] # Удаление найденного элемента из списка
        break # Завершение цикла после удаления элемента
print(f"Объект {target5} был успешно удален из списка {lst10}")


ppp = "\n---------------------------------------------------"
print(ppp)
# Рассмотрим тело нашей функции и приведем несколько примеров 
# чтобы лучше понять что у нас туту происходит с использованием 
# -1 и None. Проверяем найден ли элемент на индексе.

# С использованием проверки -1
def find_target_index(lst, target):
    for index in range(len(lst)):
        if lst[index] == target:
            return index
    return -1

lst = [41, 23, 83, 15]
target = 41
index = find_target_index(lst, target)

if index != -1:
    print(f"Элемент найден на индексе {index}")
else:
    print("Элементы не найдены")
    
    
# С использованием None
def find_target_index_or_none(lst, target):
    for index in range(len(lst)):
        if lst[index] == target:
            return index
    return None
lst = [51, 12, 64, 24]
target_number = 12
indexes = find_target_index_or_none(lst, target_number)

if indexes is not None:
    print(f"Элемент найден на индексе {indexes}")
else:
    print("Элемент не найден")
    
    