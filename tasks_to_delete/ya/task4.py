import numpy as np

n = int(input())
words_array = np.array([])
for ind in range(n):
    word = input()
    if np.in1d(words_array, word, assume_unique=True).any():
        continue
    words_array = np.append(words_array, word)

print(len(words_array))