# Sorting Algorithms

## 10 Sorting Algorithms with examples

### 1. Bubble Sort

Compare every two elements in the given array.

Repeat until all elements are sorted.

Suitable for small data set.

#### GIF Explanation

![bubble sort](https://github.com/xxicypatxx/Leetcode---Medium/blob/main/Algorithms/imgaes/bubble_sort.gif)

#### Properties

- Space Complexity: ```O(1)```

- Average Time Complexity : ```O(n**2)```

- Best Case Performance: ```O(n)```

- Worst Case Performance: ```O(n**2)```

- Stable: Yes

#### Code

```python3
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
```
<br/><br/>


### 2. Selection Sort

Keep searching for the smallest (or biggest) element and swapping it into place.

#### GIF Explanation

![selection sort](https://github.com/xxicypatxx/Leetcode---Medium/blob/main/Algorithms/imgaes/selection_sort.gif)

#### Properties

- Space Complexity: ```O(1)```

- Average Time Complexity : ```O(n**2)```

- Best Case Performance: ```O(n**2)```

- Worst Case Performance: ```O(n**2)```

- Stable: No

#### Code

```python3
def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        min_i = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_i]:
                min_i = j
        arr[i], arr[min_i] = arr[min_i], arr[i]
    return arr
```
<br/><br/>


### 3. Insertion Sort

Suitable for a small number of elements.

#### GIF Explanation

![insertion sort](https://github.com/xxicypatxx/Leetcode---Medium/blob/main/Algorithms/imgaes/insertion_sort.gif)

#### Properties

- Space Complexity: ```O(1)```

- Average Time Complexity : ```O(n**2)```

- Best Case Performance: ```O(n)```

- Worst Case Performance: ```O(n**2)```

- Stable: Yes

#### Code

```python3
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
```


