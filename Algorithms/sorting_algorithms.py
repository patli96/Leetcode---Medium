import random

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        min_i = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_i]:
                min_i = j
        arr[i], arr[min_i] = arr[min_i], arr[i]
    return arr


def insertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def mergeSort(arr):
    n = len(arr)
    if n < 2:
        return arr
    ret = []
    mid = int(n/2)
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            ret.append(left[0])
            left.pop(0)
        else:
            ret.append(right[0])
            right.pop(0)
    ret += left
    ret += right
    return ret


def quickSort(arr):
    n = len(arr)
    if n < 2:
        return arr
    pivot = arr[0]
    left = [item for item in arr if item < pivot]
    mid = [item for item in arr if item == pivot]
    right = [item for item in arr if item > pivot]
    ret = quickSort(left) + mid + quickSort(right)
    return ret


a = [random.randint(0, 100) for i in range(20)]
print(a)
print(quickSort(a))