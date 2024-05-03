import random
import timeit

def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key 
    return lst

numbers = [5, 3, 8, 4, 2]
insertion_sort(numbers)


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

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1


    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

test_arr = [random.randint(1,1000)for i in range(1000)]

merge_sort_time = timeit.timeit("merge_sort(test_arr.copy())", globals=globals(), number=1)
insertion_sort_time = timeit.timeit("insertion_sort(test_arr.copy())", globals=globals(), number=1)
tim_sort_time = timeit.timeit("sorted(test_arr.copy())", globals=globals(), number=1)

print(f"Час сортування злиттям: {merge_sort_time} секунд")
print(f"Час сортування вставками: {insertion_sort_time} секунд")
print(f"Час Timsort: {tim_sort_time} секунд")