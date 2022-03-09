
from random import randrange
from time import time


# унивесральная функция счётчика времени выполнения функции сортировки плоских массивов целых чисел
def get_runtime(sort_function, iterations=1, array_length=1000, _min=0, _max=100):
    # инициализируем пустой массив времени
    time_array = []

    # итерируем переданную функцию сортировки
    for i in range(iterations):
        # генерация массива случайных чисел
        arr = [randrange(_min, _max) for i in range(array_length)]

        # время начала сортировки
        start = time();

        # сортировка
        sort_function(arr)

        # добавление времени выполнения в массив времени
        time_array.append(time() - start)

    # возвращаем среднее время одной итерации
    return sum(time_array) / iterations;

# сортировка выбором
def sort_by_choice(array):
    length = len(array);

    # проходимся по всему массиву
    for i in range(length):

        # поиск минимального значения
        minimum_value = max(array)
        minimum_value_index = length - 1

        # прохождение от последнего минимального индекса наименьшего значения до конца массива
        for k in range(i, length):

            if array[k] < minimum_value:

                minimum_value = array[k]
                minimum_value_index = k

        # сваппинг переменных
        array[i], array[minimum_value_index] = array[minimum_value_index], array[i]

    # возврат отсортированного массива
    return array


# Сортировка вставкой
def sort_by_insertion(array):

    # проход по всему массиву
    for i in range(1, len(array)):

        # прохождение по отсортированной части массива
        for k in range(0, i):

            # сравнение следующего элемента массива с каждым из отсортированного участка
            if array[i] < array[k]:

                # удаление следущего значения
                pop = array.pop(i)

                # вставка
                array.insert(k, pop)

    # возврат отсортированного массива
    return array


# сортировка обменом
def bubble_sort(array):

    # проход по всему массиву
    for i in range(len(array) - 1):

        for j in range(len(array) - i - 1):

            if array[j] > array[j + 1]:

                array[j], array[j + 1] = array[j + 1], array[j]

    # возврат отсортированного массива
    return array


# сортировка Шелла
def shell_sort(array):
    # начальный радиус сортировки
    gap = len(array) // 2

    while gap > 0:

        for i in range(gap, len(array)):
            current_value = array[i]
            position = i

            while position >= gap and array[position - gap] > current_value:
                array[position] = array[position - gap]
                position -= gap
                array[position] = current_value

        # уменьшение радиуса с каждым проходом
        gap //= 2

    # возврат отсортированного массива
    return array

#
# # Турнирная сортировка (обычная)
# def turnir_sort(array):
#
#
# # Турнирная сортировка со слиянием
# def turnir_sort_on_join:
#


# Пирамидальная сортировка (AKA сортировка кучей, АКА турнирная ?? )
def heap_sort(data):
    # Формируем первоначальное сортирующее дерево
    # Для этого справа-налево перебираем элементы массива
    # (у которых есть потомки) и делаем для каждого из них просейку
    for start in range(int((len(data) - 2) / 2), -1, -1):
        HeapSift(data, start, len(data) - 1)

        # Первый элемент массива всегда соответствует корню сортирующего дерева
    # и поэтому является максимумом для неотсортированной части массива.
    for end in range(len(data) - 1, 0, -1):
        # Меняем этот максимум местами с последним
        # элементом неотсортированной части массива
        data[end], data[0] = data[0], data[end]
        # После обмена в корне сортирующего дерева немаксимальный элемент
        # Восстанавливаем сортирующее дерево
        # Просейка для неотсортированной части массива
        HeapSift(data, 0, end - 1)
    return data


# Просейка свеху вниз, в результате которой восстанавливается сортирующее дерево
def HeapSift(data, start, end):
    # Начало подмассива - узел, с которого начинаем просейку вниз
    root = start

    # Цикл просейки продолжается до тех пор,
    # Пока встречаются потомки, большие чем их родитель
    while True:

        child = root * 2 + 1  # Левый потомок
        # Левый потомок за пределами подмассива - завершаем просейку
        if child > end: break

        # Если правый потомок тоже в пределах подмассива,
        # то среди обоих потомков выбираем наибольший
        if child + 1 <= end and data[child] < data[child + 1]:
            child += 1

        # Если больший потомок больше корня, то меняем местами
        # при этом больший потомок сам становится корнем,
        # от которого дальше опускаемся вниз по дереву
        if data[root] < data[child]:
            data[root], data[child] = data[child], data[root]
            root = child
        else:
            break


def quick_sort(lst):
    quick_sort_helper(lst, 0, len(lst) - 1)
    return lst


def quick_sort_helper(lst, low, high):
    if low < high:
        split_point = partition(lst, low, high)
        quick_sort_helper(lst, low, split_point - 1)
        quick_sort_helper(lst, split_point + 1, high)


def partition(lst, low, high):
    pivot_value = lst[low]
    left_mark = low + 1
    right_mark = high
    done = False

    while not done:
        while left_mark <= right_mark and lst[left_mark] <= pivot_value:
            left_mark += 1
        while right_mark >= left_mark and lst[right_mark] >= pivot_value:
            right_mark -= 1

        if right_mark < left_mark:
            done = True
        else:
            lst[left_mark], lst[right_mark] = lst[right_mark], lst[left_mark]

    lst[low], lst[right_mark] = lst[right_mark], lst[low]
    return right_mark


### Тест времени для каждого алгоритма

# Сортировка выбором
print("Cортировка выбором:", get_runtime(sort_by_choice, 10, 5000), "секунд")

# Сортировка вставкой
print("Cортировка вставкой:", get_runtime(sort_by_insertion, 10, 5000), "секунд")

# Сортировка обменном
print("Cортировка обменом:", get_runtime(bubble_sort, 10, 5000), "секунд")

# Сортировка Шелла
print("Cортировка Шелла:", get_runtime(shell_sort, 10, 5000), "секунд")

# Сортировка быстрая
print("Cортировка быстрая:", get_runtime(quick_sort, 10, 5000), "секунд")

# Сортировка Пирамидальная
print("Cортировка Шелла:", get_runtime(heap_sort, 10, 5000), "секунд")
