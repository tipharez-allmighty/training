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

#Search in Rotated Sorted Array
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
