# Dictionaries

# Count Word Frequency
def count_word_frequency(words):
    result = {}.fromkeys(words, 0)
    for word in words:
        if word in result.keys():
            result[word] +=1
    return result    
