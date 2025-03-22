# Dictionaries

# Count Word Frequency
def count_word_frequency(words):
    result = {}.fromkeys(words, 0)
    for word in words:
        if word in result.keys():
            result[word] +=1
    return result    

def count_word_frequency(words):
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

# Common Keys
def merge_dicts(dict1, dict2):
    result = {}
    for key in dict1:
        if key in dict2:
            result[key] = dict1[key] + dict2.pop(key)
        else:
            result[key] = dict1[key]
    result.update(dict2)
    return result

def merge_dicts(dict1, dict2):
    result = dict1.copy()
    for key, value in dict2.items():
        result[key] = result.get(key, 0) + value
    return result
    
# Key with the highest value
def max_value_key(my_dict):
    max_key, max_value = None, float('-inf')
    for key, value in my_dict.items():
        if value > max_value:
            max_key = key
            max_value = value
    return max_key

def max_value_key(my_dict):
    return max(my_dict, key=my_dict.get)

# Reverse Key-Value Pairs
def reverse_dict(my_dict):
    result = {value:key for key, value in my_dict.items()}
    return result

# Conditional Filter
def filter_dict(my_dict, condition):
    result = {k:v for k, v in my_dict.items() if condition(k,v)}
    return result

# Same Frequency
def check_same_frequency(list1, list2):
    list1_dict = {}
    list2_dict = {}
    for value in list1:
        list1_dict[value] = list1_dict.get(value, 0) + 1
    for value in list2:
        list2_dict[value] = list2_dict.get(value, 0) + 1
        
    return list1_dict==list2_dict

def check_same_frequency(list1, list2):
    def count_elements(lst):
        counter = {}
        for element in lst:
            counter[element] = counter.get(element, 0) + 1
        return counter
    
    return count_elements(list1) == count_elements(list2)

# Tuples

# Sum and Product
def sum_product(input_tuple):
    sum_result = 0
    product_result = 1
    for number in input_tuple:
        sum_result +=number
        product_result *=number
    return sum_result, product_result

# Elementwise Sum
def tuple_elementwise_sum(tuple1, tuple2):
    return tuple(map(sum, zip(tuple1, tuple2)))

def tuple_elementwise_sum(t1, t2):
    if len(t1) != len(t2):
        raise ValueError("Input tuples must have the same length.")
 
    result = tuple(a + b for a, b in zip(t1, t2))
    return result

# Insert at the Beginning
def insert_value_front(input_tuple, value_to_insert):
    new_tuple = value_to_insert,
    return new_tuple + input_tuple

# Diagonal
def get_diagonal(tup):
    output_tuple = []
    j = 0
    for inner_tuple in tup:
        output_tuple.append(inner_tuple[j])
        j+=1
    
    return tuple(output_tuple)

def get_diagonal(input_tuple):
    return tuple(input_tuple[i][i] for i in range(len(input_tuple)))

# Common Elements
def common_elements(tuple1, tuple2):
    result = []
    for element in tuple1:
        if element in tuple2:
            result.append(element)
            
    return tuple(set(result))

def common_elements(tuple1, tuple2):
    return tuple(set(tuple1) & set(tuple2))

# Singly Linked lists

# Merge Two Sorted Linked List 
# Time Complexity: O(n + m), Space Complexity: O(1)
def mergeTwoLists(self, l1, l2):
    dummy = ListNode()
    tail = dummy
    
    while l1 is not None or l2 is not None:
        if l1 is None:
            tail.next = l2
            l2 = l2.next
        elif l2 is None:
            tail.next = l1
            l1 = l1.next
        elif l1.val <= l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    
    return dummy.next

def mergeTwoLists(self, l1, l2):
    """
    :type list1: Optional[ListNode]
    :type list2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    prehead = ListNode(-1)

    prev = prehead
    while l1 and l2:
        if l1.val <= l2.val:
            prev.next = l1
            l1 = l1.next
        else:
            prev.next = l2
            l2 = l2.next            
        prev = prev.next

    # At least one of l1 and l2 can still have nodes at this point, so connect
    # the non-null list to the end of the merged list.
    prev.next = l1 if l1 is not None else l2

    return prehead.next

# Remove Duplicates (sorted)
# Time Complexity: O(n), Space Complexity: O(1)
def deleteDuplicates(self, head):
    current = head
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    return head

# Remove Duplicates
# Time Complexity: O(n^2), Space Complexity: O(1)
def remove_duplicates(ll):
    current = ll.head
    prev_node = None
    while current:
        runner = current
        while runner.next:
            if runner.next.value == current.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        prev_node = current
        current = current.next
    
    ll.tail = prev_node
    
# Remove Linked List Elements
def removeElements(self, head, val):
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    current = head

    while current:
        if current.val == val:
            prev.next = current.next
        else:
            prev = current
        current = current.next
        
    return dummy.next

# Reverse Linked List
def reverseList(self, head):
    prev = None
    curr = head
    while curr:
        temp_node = curr.next
        curr.next = prev
        prev = curr
        curr = temp_node
    return prev

# Palindrome Linked List
def isPalindrome(self, head):
    fast = head
    slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    
    prev = None
    
    while slow:
        temp_node = slow.next
        slow.next = prev
        prev = slow
        slow = temp_node
    
    left, right = head, prev
    
    while right:
        if left.val != right.val:
            return False
        
        left = left.next
        right = right.next
    
    return True

# Middle of the Linked List
def middleNode(self, head):
    fast = head
    slow = head
    
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    
    return slow
    
#Insert into a Sorted Circular Linked List
def insert_into_sorted(self, data):
    new_node = Node(data)

    if not self.head:
        new_node.next = new_node
        self.head = new_node
        return
    
    if data < self.head.data:
        tail_node = self.head
        while tail_node.next != self.head:
            tail_node = tail_node.next
        new_node.next = self.head
        tail_node.next = new_node
        self.head = new_node
        return
    
    current = self.head
    while current.next != self.head:
        if current.data <= data < current.next.data:
            new_node.next = current.next
            current.next = new_node
            return
        current = current.next

    current.next = new_node
    new_node.next = self.head
            
# Josephus Circle using Circular Linked List
def josephus_circle(self, step):
    if self.head == self.head.next:
        return self.head
    temp = self.head
    count = 0
    while self.head != self.head.next:
        count += 1
        if count == step:
            self.delete_node(temp.data)
            print('Removed', str(temp))
            temp = temp.next
            count = 0
        else:
            temp = temp.next
            
def josephus_circle(self, step):
    temp = self.head

    while self.count_nodes() > 1:
        count = 1
        while count != step:
            temp = temp.next
            count += 1
        self.delete_node(temp.data)
        temp = temp.next

    return f"Last person left standing: {temp.data}"

# nth element to last
def nth_to_last(ll, n):
    p1 = ll.head
    p2 = ll.head
    
    for i in range(n):
        if not p2:
            return None
        p2 = p2.next
    while p2:
        p1 = p1.next
        p2 = p2.next
    
    return p1.value

# Partition around value
# Time Complexity: O(n), Space Complexity: O(1)
def partition(self, head, x):
    left, right = list_node(), list_node()
    lt, rt = left, right

    while head:
        if head.value < x:
            lt.next = head
            lt = lt.next
        else:
            rt.next = head
            rt = rt.next
        head = head.next

    lt.next = right
    rt.next = None
    return left.next
    
# Add two numbers
def addTwoNumbers(self, l1, l2):
    dummy = ListNode()
    curr = dummy
    carry = 0
    while l1 or l2 or carry:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0
        result = v1 + v2 + carry
        carry = result // 10
        result = result % 10
        curr.next = ListNode(result)
        curr = curr.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    
    return dummy.next

# Intersection of Two Linked Lists
# Time Complexity: O(m + n), Space Complexity: O(1)
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        countA = 0
        countB = 0
        current1 = headA
        current2 = headB

        while current1:
            countA += 1
            current1 = current1.next

        while current2:
            countB += 1
            current2 = current2.next

        while countA > countB:
            headA = headA.next
            countA -= 1
        while countB > countA:
            headB = headB.next
            countB -= 1


        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next

        return None
        
# Intersection of Two Linked Lists
# Time Complexity: O(m + n), Space Complexity: O(1)       
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode):
        countA = 0
        countB = 0
        currentA = headA
        currentB = headB

        while currentA:
            countA+=1
            currentA = currentA.next

        while currentB:
            countB+=1
            currentB = currentB.next
        
        step = 0
        if countA > countB:
            step = countA - countB
            while step !=0:
                headA = headA.next
                step -=1
        elif countB > countA:
            step = countB - countA
            while step !=0:
                headB = headB.next
                step -=1
        else:
            pass
        while headA or headB:
            if headA == headB:
                return headA
            if headA:
                headA = headA.next
            if headB:
                headB = headB.next
        
        return None
        
# Intersection of Two Linked Lists
# Time Complexity: O(m + n), Space Complexity: O(1)
def getIntersectionNode(self, headA, headB):
    l1, l2 = headA, headB
    while l1 != l2:
        l1 = l1.next if l1 else headB
        l2 = l2.next if l2 else headA
    return l1

# Depth-first search
visited = []
def dfs(node):
    if node not in visited:
        visited.append(node)
        for edge in some_graph.adj_list[node]:
            dfs(edge)

# Route Between Nodes 
# Time Complexity: O(V + E)
# Space Complexity: O(V + E)
def checkRoute(self, startNode, endNode):
    visited = set()
    queue = deque()
    queue.append(startNode)
    while queue:
        current_vertex = queue.popleft()
        if current_vertex not in visited:
            visited.add(current_vertex)
        if current_vertex == endNode:
            return True
        for edge in self.gdict.get(current_vertex, []):
            if edge not in visited:
                queue.append(edge)
    return False

# Minimal tree
# Time Complexity: O(n log n)
# Space Complexity: O(n)
def minimalTree(sortedArray):
    middle = len(sortedArray) // 2
    node = BSTNode(data=sortedArray[middle])
    left_array = sortedArray[:middle]    
    right_array = sortedArray[middle + 1:]
    stack = [(node, left_array, right_array)]
    
    while stack:
        current_node, left_array, right_array = stack.pop()
        
        if left_array:
            left_middle = len(left_array) // 2
            current_node.left = BSTNode(data=left_array[left_middle])
            stack.append(
                (current_node.left, left_array[:left_middle], 
                 left_array[middle + 1:])
                )
        if right_array:
            right_middle = len(right_array) // 2
            current_node.right = BSTNode(data=right_array[right_middle])
            stack.append(
                (current_node.right, right_array[:right_middle], 
                 right_array[right_middle + 1:])
                ) 
        
    return node

def minimalTree_rec(sortedArray):
    if len(sortedArray) == 0:
        return None
    if len(sortedArray) == 1:
        return sortedArray[0]
    middle = len(sortedArray) // 2
    left = minimalTree_rec(sortedArray[:middle])
    right =  minimalTree_rec(sortedArray[middle + 1:])
    node = BSTNode(
        data=sortedArray[middle],
        left=left, right=right
    )
    return node

# List of Depths
# Time Complexity: O(n)
# Space Complexity: O(n)
def depth(tree):
    queue = deque()
    queue.append(tree)
    d = 1
    result = {}
    while queue:
        level_size = len(queue)
        for _ in range(level_size):
            current_node = queue.popleft()
            if d not in result:
                result[d] = LinkedList(current_node.val)
            else:
                result[d].add(current_node.val)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        d += 1
    print({k: result[k] for k in sorted(result.keys(), reverse=True)})
    return result
    
# Valid BST
# Time Complexity: O(n)
# Space Complexity: O(n)
def isValidBST(root):
    if not root:
        return True
    queue = deque()
    queue.append((root, float('-inf'), float('inf')))
    while queue:
        current_node, low, high = queue.popleft()
        if not (low < current_node.val < high):
            return False
        if current_node.left:
            queue.append((current_node.left, low, current_node.val))
        if current_node.right:
            queue.append((current_node.right, current_node.val, high))
    return True
 
def isValidBST_rec(root):
    def dfs(node, low=float('-inf'), high=float('inf')):
        if not node:
            return True
        if not (low < node.val < high):
            return False
        return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)
    return dfs(root)

# In order successor
# Time Complexity: O(n)
# Space Complexity: O(n)
def inOrderSuccessor(root, n):
    stack = []
    current = root
    succesor = False
    while stack or current:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        if succesor:
            return current.data
        if current.data == n:
            succesor = True
        current = current.right

# In order successor
# Time Complexity: O(n)
# Space Complexity: O(n)
def inOrderSuccessor_rec(root, n):
    ordered = []
    def inOrderTraversal(root):
        if root is None:
            return
        inOrderTraversal(root.left)
        ordered.append(root)
        inOrderTraversal(root.right)
    inOrderTraversal(root)
    
    ordered = [item.data for item in ordered]
    if n in ordered:
        if ordered.index(n) == len(ordered) - 1:
            return None
        return ordered[ordered.index(n)+1]

# In order successor
# Time Complexity: O(n) if tree is completely skewed, O(logn) on average
# Space Complexity: O(1)
def inOrderSuccesorOptimal(root, n):
    succesor = None
    current = root
    while current:
        if n >= current.data:
            current = current.right
        else:
            succesor = current.data
            current = current.left
    return succesor

# Lowest Common Ancestor of a Binary Tree
# Time Complexity: O(n)
# Space Complexity: O(h)
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if left and right:
            return root        
        return left or right   

# Fractional Knapsack
# Time Complexity: O(nlogn)
# Space Complexity: O(h)
class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.ratio = value / weight
    
    def __repr__(self):
        return f'weight={self.weight}, value={self.value}, ratio={self.ratio}'

def fractKnap(items: list[Item], max_weight: int) -> int:
    sorted_items = sorted(items, key=lambda x: x.ratio, reverse=True)
    total_value = 0
    space_left = max_weight
    for item in sorted_items:
        reminder = space_left - item.weight
        if reminder < 0:
            total_value += space_left * item.ratio
            space_left = 0
            break
        total_value += item.weight * item.ratio
        space_left = reminder
    return total_value
