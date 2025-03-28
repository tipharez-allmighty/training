def fibMemo(num: int, memo: dict = dict()):
    if num == 0:
        return 0
    if num in (1, 2):
        return 1
    if num not in memo:
        memo[num] = fibMemo(num - 2, memo) + fibMemo(num - 1, memo)
    return memo[num]

def fibTab(num):
    if num == 0:
        return num  
    tb = [0, 1]
    for i in range(2, num + 1):
        tb.append(tb[i - 1] + tb[i - 2])
    return tb[num]

def numFactorMemo(num, memo: dict | None = None):
    if memo is None:
        memo = dict()
    if num in (0, 1, 2):
        return 1
    if num == 3:
        return 2
    if num not in memo:
        memo[num] = numFactorMemo(num - 1, memo) + numFactorMemo(num - 3, memo) + numFactorMemo(num - 4, memo)
    return memo[num]

def numFactorTab(num):
    tab = [1, 1, 1, 2]
    for i in range(4, num + 1):
        result = tab[i - 4] + tab[i - 3] + tab[i - 1]
        tab.append(result)
    return tab[num]

def houseRobberMemo(houses: list[int], current_house: int = 0, memo: dict | None = None):
    if memo is None:
        memo = dict()
    if current_house > len(houses) - 1:
        return 0
    else:
        memo[current_house] = max(
            houses[current_house] + houseRobberMemo(houses, current_house + 2, memo),
            houseRobberMemo(houses, current_house + 1, memo)
        )
    return memo[current_house]

def houseRobberTab(houses: list[int]):
    tab = [0] * (len(houses) + 2)
    for i in range(len(houses) - 1, -1, -1):
        tab[i] = max(
            houses[i] + tab[i + 2], tab[i + 1]
        )
    return tab[0]
