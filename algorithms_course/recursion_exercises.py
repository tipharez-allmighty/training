# Sum of digits
def sum_of_digits_rec(num: int):
    if num == 0:
        return num
    else: return(int(num % 10) + sum_of_digits_rec(num // 10))

def sum_of_digits_iter(num: int):
    result = 0
    while num > 0:
        result += int(num % 10)
        num = num // 10
    return result

# Power of the number
def power_of_num_rec(num: int, power: int):
    if power == 0:
        return 1
    return num * power_of_num_rec(num, power - 1)

def power_of_num_iter(num: int, power: int):
    result = 1
    if num == 0:
        return result
    for _ in range(abs(power)):
        result *= num
    
    if power < 0:
        result = 1 / result
    return result

# Greatest Common Divisor
def gcd_rec(num1, num2):
    if num2 == 0:
        return num1
    return gcd_rec(num2, num1 % num2)

def gcd_iter(num1, num2):
    greater_num = num1 if num1 < num2 else num2
    for i in range(greater_num, 0, -1):
        if num1 % i == 0 and num2 % i == 0:
            return i

# Decimal to binary
def decimal_to_binary_iter(decimal: int):
    binary = []
    while decimal != 0:
        remainder = decimal % 2
        decimal = decimal // 2
        binary.insert(0, remainder)
    return binary

def decimal_to_binary_rec(decimal: int):
    if decimal == 0:
        return 0
    return decimal % 2 + 10 * decimal_to_binary_rec(decimal // 2)


# Factorial
def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num - 1)

# Fibonacci
# O(2^n), O(n)
def fib(num):
    if num <= 1:
        return num
    return fib(num - 1) + fib(num - 2)

# O(n), O(1)
def fib(num):
    if num <= 1:
        return num
    
    prev1 = 1
    prev2 = 0
    
    for _ in range(2, num + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
    
    return current
        
# Product of the array
def productOfArray(arr):
    if not arr:
        return 1
    return arr[0] * productOfArray(arr[1:])

# Recursive range
def recursiveRange(num):
    if num == 0:
        return 0
    return num + recursiveRange(num - 1)

# Reverse string
def reverse_string_iter(string: str):
    string_list = list(string)
    left, right = 0, len(string) - 1
    while left < right:
        string_list[left], string_list[right] = string_list[right], string_list[left]
        left += 1
        right -= 1
    
    return ''.join(string_list)

def reverse_string_rec(string: str):
    if len(string) <=1:
        return string
    
    return string[-1] + reverse_string_rec(string[:-1])

# Is palidrome
def isPalidrome(string: str):
    left = 0
    right = len(string) - 1
    
    while left < right:
        if not string[left].isalnum():
            left += 1
        elif not string[right].isalnum():
            right -= 1
        elif string[left] == string[right]:
            left += 1
            right -= 1
        else: return False    
    return True

def isPalidrome_rec(string: str):
    if len(string) == 1:
        return True
    if string[0] != string[-1]:
        return False
    return isPalidrome_rec(string[1:-1])

# Some recursive
def isOdd(num):
    if num%2==0:
        return False
    else:
        return True
        
def someRecursive(arr, cb):
    if len(arr) == 0:
        return False
    if cb(arr[-1]):
        return True
    return someRecursive(arr[:-1], cb)

# Flatten
def flatten_iter(arr):
    stack = arr[::-1]
    flatten_list = []
    while stack:
        item = stack.pop()
        if isinstance(item, list):
            stack.extend(item[::-1])
        else:
            flatten_list.append(item)
    return flatten_list

def flatten_rec(arr):
    flatten_list = []
    for item in arr:
        if isinstance(item, list):
            flatten_list.extend(flatten_rec(item))
        else:
            flatten_list.append(item)
    return flatten_list

# Capitalize first
def capitalizeFirst_iter(arr):
    for i in range(len(arr)):
        if arr[i].isalnum():
            arr[i] = arr[i].capitalize()
    return arr

def capitalizeFirst_rec(arr):
    result = []
    if len(arr) == 0:
        return result
    result.append(arr[0].capitalize())
    return result + capitalizeFirst_rec(arr[1:])

# Nested numbers sum
def nestedEvenSum_iter(obj):
    even_num_sum = 0
    stack = [[key, value] for key, value in obj.items()]
    while stack:
        temp = stack.pop()
        temp_value = temp[1]
        if isinstance(temp_value, int):
            if temp_value % 2 == 0:
                even_num_sum += temp_value
        elif isinstance(temp_value, dict):
            stack.extend([[key, value] for key, value in temp_value.items()])
            
    return even_num_sum

def nestedEvenSum_rec(obj):
    even_num_sum = 0
    
    for key, value in obj.items():
        if isinstance(value, int):
            if value % 2 == 0:
                even_num_sum += value
        elif isinstance(value, dict):
            even_num_sum += nestedEvenSum_rec(value)
        
    return even_num_sum

# Capitalize words
def capitalizeWords(arr):
    result = []
    if len(arr) == 0:
        return result
    result.append(arr[0].upper())
    return result + capitalizeWords(arr[1:])

# Stringify numbers
def stringifyNumbers_iter(obj):
    stack = [obj]
    
    while stack:
        current = stack.pop()
        for key, value in current.items():   
            if type(value) is int:
                current[key] = str(value)
            if type(value) is dict:
                stack.append(value)
    return obj
                
def stringifyNumbers_rec(obj):
    for key, value in obj.items():
        if type(value) is int:
            obj[key] = str(value)
        if type(value) is dict:
            obj[key] = stringifyNumbers_rec(value)
    return obj

# Collect strings
def collectStrings_iter(obj):
    collected_strings = []
    stack = [obj]
    
    while stack:
        current = stack.pop()
        for key, value in current.items():
            if type(value) is str:
                collected_strings.append(value)
            if type(value) is dict:
                stack.append(value)
                
    return collected_strings

def collectStrings_rec(obj):
    collected_strings = []
    
    for key, value in obj.items():
        if type(value) is str:
            collected_strings.append(value)
        if type(value) is dict:
            collected_strings += collectStrings_rec(value)
                
    return collected_strings 
