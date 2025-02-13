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
