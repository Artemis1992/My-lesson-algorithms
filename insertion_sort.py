# 8. Напишите функцию, которая сортирует список чисел по возрастанию (сортировка вставками).\
ppp = "\n---------------------------------------------------"
print(ppp)

def insertion_sort(arr):
    # Проходим по каждому элементу списка, начиная со второго
    for i in range(1, len(arr)):
        key = arr[i] # Сохраняем текущий элемент для сровнения
        j = i - 1 # начинаем проверку с элемента перед текущим
        
        # Сдвигаем элементы arr[0..i-1], которые больше key, на одну позицию вправо
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j] # Перемещаем элемент на одну позицию вправо
            j -= 1  # Переходим к следующему элементу влево
            
         # Вставляем текущий элемент в правильную позицию    
        arr[j + 1] = key

numbers = [12, 11, 13, 9, 8]
func_insert = insertion_sort(numbers)
print(f"Отсортированный список {numbers}")
# Отсортированный список [8, 9, 11, 12, 13]


ppp = "\n---------------------------------------------------"
print(ppp)
# Перебор элементов списка с пропуском первого элемента:

arr1 = [10, 20, 30, 40, 50]
for i in range(1, len(arr1)):
    print(arr1[i])


ppp = "\n---------------------------------------------------"
print(ppp)
# Подсчет суммы всех элементов списка, кроме первого:

arr2 = [10, 20, 30, 40, 50]
total = 0
for i in range(1, len(arr2)):\
    total += arr2[i]
print(total)
    

ppp = "\n---------------------------------------------------"
print(ppp)















