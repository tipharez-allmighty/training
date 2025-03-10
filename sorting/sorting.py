# bubble sort
# Time Complexity: O(n^2) due to nested loops.
def bubbleSort(arr):
    size = len(arr)

    for i in range(size - 1):
        for j in range(size - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# selection sort
# Time Complexity: O(n^2)
def selectionSort(nums: list[int]) -> None:
    for i in range(len(nums)):
        min_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]

# insert sort
# Time Complexity: O(n^2) for the worst case, where elements are in reverse order.
def insertSort(arr):
    for i in range(len(arr)):
        j = i
        while arr[j - 1] > arr[j] and j > 0:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j = j - 1

# recursive insert sort
# Time Complexity: O(n^2) due to recursive calls and element comparisons/swaps.
def insertSortRec(arr, n=None):
    if n is None:
        n = len(arr)
    if n <= 1:
        return arr
    insertSortRec(arr, n - 1)

    last = arr[n - 1]
    j = n - 2

    while arr[j] > last and j >= 0:
        arr[j + 1] = arr[j]
        j = j - 1

    arr[j + 1] = last

# merge_sort
# Time Complexity: O(n log n), where n is the length of the array.
def merge_sort(arr):
    middle = len(arr) // 2
    arr1 = arr[:middle]
    arr2 = arr[middle:]

    def merge_inner(arr1, arr2):
        # Time Complexity of merge_inner: O(n), where n is len(arr1) + len(arr2).
        temp_arr = []
        while len(arr1) != 0 and len(arr2) != 0:
            if arr1[0] > arr2[0]:
                temp_arr.append(arr2[0])
                arr2.remove(arr2[0])
            else:
                temp_arr.append(arr1[0])
                arr1.remove(arr1[0])

        while len(arr1) != 0:
            temp_arr.append(arr1[0])
            arr1.remove(arr1[0])

        while len(arr2) != 0:
            temp_arr.append(arr2[0])
            arr2.remove(arr2[0])

        return temp_arr

    if len(arr) == 1:
        return arr

    arr1 = merge_sort(arr1)
    arr2 = merge_sort(arr2)

    return merge_inner(arr1, arr2)

# heap sort
# Time Complexity: O(n log n), where n is the number of elements.
def swap(i, j, arr):
    arr[i], arr[j] = arr[j], arr[i]

def buildHeap(arr, n, i):
    # Time Complexity of buildHeap: O(log n) due to recursive calls.
    parent = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[parent] < arr[left]:
        parent = left
    if right < n and arr[parent] < arr[right]:
        parent = right
    if parent != i:
        swap(i, parent, arr)
        buildHeap(arr, n, parent)

def heapify(arr, n):
    # Time Complexity of heapify: O(n) for building a max heap.
    i = n // 2 - 1
    for k in range(i, -1, -1):
        buildHeap(arr, n, k)

def heapsort(arr):
    # Time Complexity of heapsort: O(n log n)
    n = len(arr)
    heapify(arr, n)
    for i in range(n - 1, 0, -1):
        swap(0, i, arr)
        buildHeap(arr, i, 0)

# quicksort
# Time Complexity: O(n log n) on average, but O(n^2) in the worst case.
def partition(arr, current_index, pivot):
    swap_marker = current_index - 1
    while current_index <= pivot:
        if arr[current_index] > arr[pivot]:
            current_index += 1
            continue
        if arr[current_index] <= arr[pivot]:
            swap_marker += 1
            if current_index > swap_marker:
                arr[current_index], arr[swap_marker] = arr[swap_marker], arr[current_index]
            current_index += 1
    return swap_marker

def quicksort(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    if left < right:
        pivot = partition(arr, left, right)
        quicksort(arr, left, pivot - 1)
        quicksort(arr, pivot + 1, right)

# countsort
# Time Complexity: O(n + k), where n is the number of elements in the array, and k is the range of the input values.
# Space Complexity: O(n + k), as additional space is required for the count array and output array.
# Note: Counting Sort is not a comparison-based algorithm and is efficient for small ranges of integers, 
# but it is not suitable for sorting data with large ranges or floating-point numbers.
def count_sort(nums, k):
    counts = [0]*k
    result = [0]*len(nums)
    
    for num in nums:
        counts[num] +=1
    for i in range(1, len(counts)):
        counts[i] = counts[i-1] + counts[i]

    for i in range(len(nums) -1,-1,-1):
        value = nums[i]
        result_position = counts[value] - 1
        result[result_position] = value
        counts[value] -=1
    return result
