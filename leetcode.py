# binary search
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        
        while high >= low:
            mid = low + (high - low)//2
            if nums[mid] == target:
                return mid
            if target > nums[mid]:
                low = mid + 1
            if target < nums[mid]:
                high = mid - 1
        return -1

# search insert
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while high >= low:
            mid = low + (high - low)//2
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return low

# Search in Rotated Sorted Array
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if target == nums[mid]:
                return mid
            if nums[low] <= nums[mid]:
                if target < nums[low] or target > nums[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                if target > nums[high] or target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1

        return -1

# bubble sort
def bubbleSort(arr):
    size = len(arr)
    
    for i in range(size - 1):
        for j in range(size - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# insert sort
def insertSort(arr):
    for i in range(len(arr)):
        j = i
        while arr[j - 1] > arr[j] and j > 0:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j = j - 1

# recursive insert sort
def insertSortRec(arr, n=None):
    if n is None:
        n = len(arr)
    if n <= 1:
        return arr
    insertSortRec(arr, n - 1)
    
    last = arr[n-1]
    j = n-2
    
    while arr[j] > last and j >= 0:
        arr[j+1] = arr[j]
        j = j - 1
    
    arr[j+1] = last

# merge_sort
def merge_sort(arr):
    middle = len(arr)// 2
    arr1 = arr[:middle]
    arr2 = arr[middle:]
    
    def merge_inner(arr1, arr2):
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
def swap(i,j,arr):
    arr[i],arr[j] = arr[j],arr[i]

def buildHeap(arr, n, i):
    parent = i
    left = 2*i + 1
    right = 2*i + 2
    
    if left < n and arr[parent] < arr[left]:
        parent = left
    if right < n and arr[parent] < arr[right]:
        parent = right
    if parent != i:
        swap(i, parent, arr)
        buildHeap(arr, n, parent)

def heapify(arr,n):
    i = n//2 - 1   
    for k in range(i,-1,-1):
        buildHeap(arr, n, k)

def heapsort(arr):
    n = len(arr)
    heapify(arr, n)
    for i in range(n - 1, 0, -1):
        swap(0, i, arr)
        buildHeap(arr, i, 0)
"""        
def heapsort(arr):
    for n in range(len(arr), 0, -1):
        heapify(arr, n)
        swap(0, n - 1, arr)
"""
# quicksort
def partition(arr, current_index, pivot):
    swap_marker = current_index - 1
    while current_index <= pivot:
        if arr[current_index] > arr[pivot]:
            current_index +=1
            continue
        if arr[current_index] <= arr[pivot]:
            swap_marker+=1
            if current_index > swap_marker:
                arr[current_index], arr[swap_marker] = arr[swap_marker], arr[current_index]
            current_index +=1
    return swap_marker

def quicksort(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    if left < right:
        pivot = partition(arr, left, right)
        quicksort(arr, left, pivot - 1)
        quicksort(arr, pivot + 1, right)
        
# strassens matrix miltiplication
def brute_force(A,B):
    C = np.zeros_like(A)
    for i in range(A.shape[0]):
        for j in range(B.shape[1]):
            for k in range(A.shape[1]):
                C[i][j] += A[i][k]*B[k][j]
    return C


def split_matrix(matrix):
    n = len(matrix)
    return matrix[:n//2, :n//2], matrix[:n//2,n//2:], matrix[n//2:,:n//2], matrix[n//2:,n//2:]

def strassens(A,B):
    if len(A) <= 2:
        return brute_force(A,B)
    a,b,c,d = split_matrix(A)
    e,f,g,h = split_matrix(B)
    M1 = strassens(a + d, e + h)
    M2 = strassens(c + d, e)
    M3 = strassens(a, f - h)
    M4 = strassens(d, g - e)
    M5 = strassens(a + b, h)
    M6 = strassens(c - a, e + f)
    M7 = strassens(b - d, g + h)
    
    C11 = M1 + M4 - M5 + M7
    C12 = M3 + M5
    C21 = M2 + M4
    C22 = M1 - M2 + M3 + M6
    
    return np.vstack((np.hstack((C11,C12)), np.hstack((C21,C22))))
