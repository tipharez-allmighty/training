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
