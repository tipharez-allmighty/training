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
