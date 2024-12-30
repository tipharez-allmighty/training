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
