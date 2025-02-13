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
