# 643. Maximum Average Subarray I
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur_sum = sum(nums[0:k])
        cur_max = cur_sum / k

        for i in range(k, len(nums)):
            cur_sum += nums[i]
            cur_sum -= nums[i - k]
            cur_average = cur_sum / k
            cur_max = max(cur_average, cur_max)
        
        return cur_max
        
# 219. Contains Duplicate II
# Time Complexity: O(n)
# Space Complexity: O(k)
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        j = 0
        i = 0
        while j < len(nums):
            if abs(i - j) <= k:
                if not nums[j] in window:
                    window.add(nums[j])
                    j += 1
                else:
                    return True
            else:
                window.remove(nums[i])
                i += 1
        return False

# Last Stone Weight
# Time Complexity: O(nlogn)
# Space Complexity: O(n)
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            if x != y:
                heapq.heappush(stones, x - y)
        return abs(stones[0]) if stones else 0

# Reverse String
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        p1 = 0

        p2 = len(s) - 1

        while p1 < p2:
            s[p1], s[p2] = s[p2], s[p1]
            p1 += 1
            p2 -= 1
            
# Kth Largest Element in a Stream
# Time Complexity: O(logk) because we dont store all elements in the array, we store only k amount
# Space Complexity: O(k)
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k: int = k
        self.minHeap: List[int] = nums
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
        
# Invert Binary Tree
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.left, root.right = root.right, root.left
            self.invertTree(root.right)
            self.invertTree(root.left)
        return root
# Has Cycle
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

# Best Time to Buy and Sell Stock
# Time Complexity: O(n)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)
        return max_profit
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

# Is subsequence
# Time Complexity: O(n), Space Complexity: O(1)
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p1 = 0
        p2 = 0
        while p1 != len(s):
            if p2 == len(t):
                return False
            if s[p1] != t[p2]:
                p2 += 1
            else:
                p1 += 1
                p2 += 1
        return True
    return dfs(some_node)[0]

# Optimized
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p1 = 0
        p2 = 0
        while p1 < len(s) and p2 < len(t):
            if s[p1] == t[p2]:
                p1 += 1
            p2 += 1
        return p1 == len(s)

# Unique Number of Occurrences
# Time Complexity:  O(n + m²)
# Space Complexity: O(m)
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurrences = dict().fromkeys(arr, 0)
        for value in arr:
            if value in occurrences:
                occurrences[value] += 1
        values = list(occurrences.values())
        value_to_compare = values[0]
        for i in range(1, len(values)):
            if value_to_compare in values[i:]:
                return False
            value_to_compare = values[i]
        return True
        
# Time Complexity:  O(n)
# Space Complexity: O(m)
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        set_of_values = set()
        occurrences = dict().fromkeys(arr, 0)
        for value in arr:
            if value in occurrences:
                occurrences[value] += 1
        
        for value in occurrences.values():
            set_of_values.add(value)
        
        return len(occurrences) == len(set_of_values)

# Find difference
# Time Complexity:  O(n + m)
# Space Complexity: O(n + m)
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        result = []
        dict1 = dict().fromkeys(nums1, 0)
        dict2 = dict().fromkeys(nums2, 0)
        first_list = [key for key in dict1 if key not in dict2]
        second_list = [key for key in dict2 if key not in dict1]
        result.append(first_list)
        result.append(second_list)
        return result

# Time Complexity:  O(n + m)
# Space Complexity: O(m + m)
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]
        set1 = set(nums1)
        set2 = set(nums2)
        return [list(set1 - set2), list(set2 - set1)]

# Is Anagram
# Time Complexity:  O(n)
# Space Complexity: O(m + n)
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        s_dict = dict.fromkeys(list(s), 0)
        for char in s:
            if char in s_dict:
                s_dict[char] += 1
        for char in t:
            if char in s_dict:
                s_dict[char] -= 1
        for value in s_dict.values():
            if value != 0:
                return False
        return True
        
# Time Complexity:  O(n)
# Space Complexity: O(m + n)
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        s_dict, t_dict = {}, {}
        
        for i in range(len(s)):
            s_dict[s[i]] = 1 + s_dict.get(s[i], 0)
            t_dict[t[i]] = 1 + t_dict.get(t[i], 0)
        for key in s_dict:
            if s_dict[key] != t_dict.get(key, 0):
                return False
        return True
        
# Valid parenthesis         
# Time Complexity:  O(n)
# Space Complexity: O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        ...
        parenthesis = {
           '(':')', '{':'}', '[':']'
        }
        stack = []
        for char in s:
            if stack:
                previous = parenthesis.get(stack[-1])
                if not previous:
                    return False
                elif char == previous:
                    stack.pop()
                else:
                    stack.append(char)
            else:
                stack.append(char)

        return False if stack else True

# Container With Most Water
# Time Complexity:  O(n)
# Space Complexity: O(1)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        def waterAmount(index1: int, index2: int):
            min_height = (
                height[index1] if height[index1] < height[index2] else height[index2]
            )
            return min_height * (index2 - index1)

        max_water = 0
        left = 0
        right = len(height) - 1

        while left < right:
            current_amount = waterAmount(
                index1=left,
                index2=right,
            )
            max_water = current_amount if current_amount > max_water else max_water
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_water

# Reverse Linked list
# Time Complexity:  O(n)
# Space Complexity: O(1)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        current = head
        previous = None
        while current:
            temp_node = current.next
            current.next = previous
            previous = current
            current = temp_node
        return previous

# Merge two sorted Linked Lists
# Time Complexity: O(n + m)
# Space Complexity: O(1)
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode],
                      list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        last_node = list1 if list1 else list2
        if last_node:
            tail.next = last_node
        return dummy.next

