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
  
# O(n), O(n)    
def fibMemo(num: int, memo: dict = dict()):
    if num == 0:
        return 0
    if num in (1, 2):
        return 1
    if num not in memo:
        memo[num] = fibMemo(num - 2, memo) + fibMemo(num - 1, memo)
    return memo[num]
  
# O(n), O(n)
def fibTab(num):
    if num == 0:
        return num  
    tb = [0, 1]
    for i in range(2, num + 1):
        tb.append(tb[i - 1] + tb[i - 2])
    return tb[num]
