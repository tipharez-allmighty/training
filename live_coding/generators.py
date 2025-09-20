# Implement a generator that yields Fibonacci numbers up to n.
def fib(n: int) -> Generator:  
    prev1 = 1
    prev2 = 0
    for i in range(n + 1):
        if i <= 1:
            yield i
        else:
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current
            yield prev1

# for n in iter(fib(10)):
#     print(n)

# Write a generator that reads a large text file line by line and yields only lines containing a certain keyword.
def open_file(path: str):
    with open(path, 'r') as file:
        for line in file:
            if "Python" in line:
                yield line

for line in iter(open_file('some_text.txt')):
    print(line)

# Create a custom iterator class for iterating over the squares of numbers from 1 to 10.
class SquareIter:
    def __init__(self, num: int):
        self.num: int = num
    
    def __iter__(self):
        for number in range(self.num + 1):
            yield number ** 2

    def __getitem__(self, index):
        return [value ** 2 for value in range(self.num + 1)][index]
        
for i in SquareIter(10):
    print(i)
