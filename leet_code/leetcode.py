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
