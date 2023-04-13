import numpy as np

n = int(input())
words_array = np.array([])
for ind in range(n):
    word = input()
    if words_array[words_array == word]:
        continue
    words_array = np.append(words_array, word)
    
print(words_array)
print(len(words_array))