# Common Search Algorithms

## 1. Linear Search

### Time Complexity: ```O(n)```

### Code

```python3
def linearSearch(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return None
```

<br/><br/>


## 2. Binary Search

### Time Complexity: ```O(logn)```

### Code

```python3
def binarySearch(arr,target):
    left = 0
    right = len(arr)-1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            right = mid - 1
        else:
            left = mid+1
    return None
```

<br/><br/>


## 3. Interpolation Search

### Time Complexity: ```O(loglogn)```

### Code

```python3
def interpolationSearch(arr,target):
    left = 0
    right = len(arr)-1
    while left <= right:
        mid = left + ((target - arr[left]) // (arr[right] - arr[left])) * (right - left)
        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            right = mid - 1
        else:
            left = mid+1
    return None
```

<br/><br/>


## 4. Jump Search

### Time Complexity: ```O(n ^ 0.5)```

### Code

```python3
def jumpSearch(arr, target):
    n = len(arr)
    step = int(n ** 0.5)
    prev = 0
    while arr[min(step, n) - 1] < target:
        prev = step
        step = step + int(n ** 0.5)
        if prev >= n:
            return None
    while arr[prev] < target:
        prev = prev+1
        if prev == min(step, n):
            return None
    if arr[prev] == target:
        return prev
    else:
        return None
```

<br/><br/>

## 5. Quick Search

### Time Comlexity: ```O(n)```

### Code

```python3
def partition(sequence,left,right,pivot_index):
    pivot_value=sequence[pivot_index]
    sequence[pivot_index],sequence[right]=sequence[right],sequence[pivot_index] #交换两个元素，使pivot_index与最右边元素置换位置，即先将pivot移动到最右边
    store_index=left
    for i in range(left,right):
        if sequence[i]<pivot_value:
            sequence[store_index],sequence[i]=sequence[i],sequence[store_index] #交换两个元素，使当前遍历元素(小于pivot_value的元素)与store_index元素置换位置
            store_index=store_index+1 #store_index索引增加1
    sequence[store_index],sequence[right]=sequence[right],sequence[store_index] #交换两个元素，使store_index与最右边元素置换位置，即交换回来pivot最终应该在的位置
    return store_index
def quick_search(sequence,left,right,k):
    if left==right: #如果只有一个元素
        return sequence[left] #返回该元素
    pivot_index=left+random.randint(0,right-left+1) #初始pivot_index，使pivot_index在无序表随机
    pivot_index=partition(sequence,left,right,pivot_index) #pivot在已经排好序的位置
    if k==pivot_index:
        return sequence[k] #返回该位置元素
    elif k<pivot_index:
        return quick_search(sequence,left,pivot_index-1,k) #需要在[left,pivot_index-1]里面继续快速检索
    else:
        return quick_search(sequence,pivot_index+1,right,k) #需要在[pivot_index+1,right]里面继续快速检索
```
<br/><br/>


## 6. Hash Search

### Time Complexity:```O(1)```

### Code

```python3
class HashTable:
    def __init__(self, size):
        self.elem = [None for i in range(size)] # 使用list数据结构作为哈希表元素保存方法
        self.count = size # 最大表长
    def hash(self, key):
        return key % self.count # 散列函数采用除留余数法
    def insert_hash(self, key):
    #插入关键字到哈希表内
        address = self.hash(key) # 求散列地址
        while self.elem[address]: # 当前位置已经有数据了，发生冲突。
            address = (address+1) % self.count # 线性探测下一地址是否可用
        self.elem[address] = key # 没有冲突则直接保存。
    def search_hash(self, key):
    #查找关键字，返回布尔值
        star = address = self.hash(key)
        while self.elem[address] != key:
            address = (address + 1) % self.count
            if not self.elem[address] or address == star: # 说明没找到或者循环到了开始的位置
                return False
        return True,address #返回索引值
```
