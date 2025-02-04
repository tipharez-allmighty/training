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
