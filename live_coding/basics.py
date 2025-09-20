from typing import Generator


# String of dict values
dict_1 = {
    2: "2",
    4: "4",
}

f = " ".join(
    (
        value for value in dict_1.values()
    )
)

# Create a list of squares for all even numbers from 1 to 20.
square = lambda x: [value ** 2 for value in range(x + 1)]

# print(square(20))

# Transform a dictionary {‘a’:1, ‘b’:2, ‘c’:3} into {‘a’:2, ‘b’:4, ‘c’:6} using a comprehension.

dict_1 = {"a":1, "b":2, "c":3}
dict_1 = {
    key: value * 2 for key, value in dict_1.items()
}
# print(dict_1)

# Flatten a nested list [[1,2],[3,4],[5]] into [1,2,3,4,5].
list_1 = [[1,2],[3,4],[5]]

def flatten_list_rec(nested_list: list) -> list:
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten_list_rec(item))
        else:
            flat_list.append(item)
    return flat_list

def flatten_list_stack(nested_list: list) -> list:
    stack = [nested_list]
    flat_list = []
    
    while stack:
        current = stack.pop()
        
        if isinstance(current, list):
            for item in current[::-1]:
                stack.append(item)
        else:
            flat_list.append(current)
    
    return flat_list
            
# print(flatten_list_stack(list_1))
