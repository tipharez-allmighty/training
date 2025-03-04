# Greatest Common Divisor of Strings
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str: 
        for i in range(min(len(str1), len(str2)), 0, -1):        
            if (len(str2) % i) == 0 and (len(str1) % i) == 0:
                n1, n2 = len(str1) // i, len(str2) // i
                if str1 == n1*str1[:i] and str2 == n2*str1[:i]:
                    return str1[:i]
        return ''

# binary search
class Solution:
    # Time Complexity: O(log n) because we split the search space in half each iteration.
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while high >= low:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return mid
            if target > nums[mid]:
                low = mid + 1
            if target < nums[mid]:
                high = mid - 1
        return -1

# Valid Palindrome
class Solution:
    # Time Complexity: O(n), where n is the length of the string. We scan each character once from both ends.
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            elif s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False
        return True

# search insert
class Solution:
    # Time Complexity: O(log n) due to binary search approach.
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while high >= low:
            mid = low + (high - low) // 2
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return low

# Search in Rotated Sorted Array
class Solution:
    # Time Complexity: O(log n) because we use a modified binary search to handle rotation.
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
# Time Complexity: O(n^2) due to nested loops.
def bubbleSort(arr):
    size = len(arr)

    for i in range(size - 1):
        for j in range(size - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

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
    
# maximum Depth of Binary Tree
class Solution(object):
    # Time Complexity: O(n), where n is the number of nodes, as we visit each node once.
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        stack = [[root, 1]]
        res = 0

        while stack:
            node, depth = stack.pop()
            if node:
                if res < depth:
                    res = depth
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return res

# recursive maximum Depth of Binary Tree
class Solution(object):
    # Time Complexity: O(n) for each recursive call on each node.
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# strassens matrix multiplication
def brute_force(A, B):
    # Time Complexity: O(n^3), where n is the matrix dimension.
    C = np.zeros_like(A)
    for i in range(A.shape[0]):
        for j in range(B.shape[1]):
            for k in range(A.shape[1]):
                C[i][j] += A[i][k] * B[k][j]
    return C

def split_matrix(matrix):
    # Time Complexity: O(1), as it simply slices the matrix.
    n = len(matrix)
    return matrix[:n // 2, :n // 2], matrix[:n // 2, n // 2:], matrix[n // 2:, :n // 2], matrix[n // 2:, n // 2:]

def strassens(A, B):
    # Time Complexity: O(n^log7) ≈ O(n^2.81) due to recursive multiplications and additions.
    if len(A) <= 2:
        return brute_force(A, B)
    a, b, c, d = split_matrix(A)
    e, f, g, h = split_matrix(B)

    p1 = strassens(a, f - h)
    p2 = strassens(a + b, h)
    p3 = strassens(c + d, e)
    p4 = strassens(d, g - e)
    p5 = strassens(a + d, e + h)
    p6 = strassens(b - d, g + h)
    p7 = strassens(a - c, e + f)

    top = np.hstack((p5 + p4 - p2 + p6, p1 + p2))
    bottom = np.hstack((p3 + p4, p1 + p5 - p3 - p7))

    return np.vstack((top, bottom))
    
# merge alternatively
class Solution(object):
    def mergeAlternately(self, word1, word2):
        result = ''
        count = 0

        while count < len(word1) or count < len(word2):
            if count < len(word1):
                result += word1[count]
            if count < len(word2):
                result += word2[count]
            count +=1
        
        return result
# Balanced Binary Tree
# Naive Approach
# Time Complexity: O(n^2), Space Complexity: O(n)
def getdepth(some_node):
    if some_node is None:
        return 0
    return 1 + max(
        getdepth(some_node.left),
        getdepth(some_node.right)
    )
    
def balanced(some_node):
    if some_node is None:
        return True
    left = getdepth(some_node.left)
    right = getdepth(some_node.right)
    
    result = abs(left - right) <= 1
    if result is False:
        return False
    return balanced(some_node.left) and balanced(some_node.right)

# Optimized
# Time Complexity: O(n^2), Space Complexity: O(H), where H is the height of the tree (in the worst case, this can be O(n)).
def isBalanced(some_node):
    def dfs(some_node):
        if not some_node:
            return [True, 0]
        left, right = dfs(some_node.left), dfs(some_node.right)
        balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
        height = 1 + max(left[1], right[1])
        return [balanced, height]
    
    return dfs(some_node)[0]
