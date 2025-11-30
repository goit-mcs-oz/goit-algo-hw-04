
import random
import timeit

# Сортування злиттям


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Спочатку об'єднайте менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Якщо в лівій або правій половині залишилися елементи,
            # додайте їх до результату
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


# Сортування вставками

def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >= 0 and key < lst[j]:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = key
    return lst


n = 1000  # Number of random numbers
test_list = random.sample(range(1, int(n * 1.5)), n)


def merge_sort_test():
    sorted_list = merge_sort(test_list)


def insertion_sort_test():
    sorted_list = insertion_sort(test_list)


def sorted_test():
    sorted_list = sorted(test_list)


time = timeit.timeit(merge_sort_test, number=1000)
print(f'Сортування злиттям time = {time} ')
time = timeit.timeit(merge_sort_test, number=1000)
print(f'Сортування вставками time = {time} ')
time = timeit.timeit(sorted_test, number=1000)
print(f'Сортування sorted time = {time} ')

'''
Отримано наступні результати:
Сортування злиттям time = 1.9296018939930946 
Сортування вставками time = 1.9003892810433172 
Сортування sorted time = 0.09342711203498766 

Швидкість сортування злиттям та вставками приблизно однакова, але швидкість сортуваня вставками на сотні долі секунди швидше

Швидкість сортування вбудованою функцією sorted швидше приблизно в 20 раз

Одже поєднання сортування злиттям і сортування вставками робить алгоритм Timsort набагато ефективнішим, і саме з цієї причини програмісти, в більшості випадків, використовують вбудовані в Python алгоритми, а не кодують самі.

'''
