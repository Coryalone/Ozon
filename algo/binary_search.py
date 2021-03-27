

import random

#print(arr)

def random_generate(length):
    x = []
    for i in range(1, length):
        x.append(random.randint(1, length))
    return x
global i

data = list(range(1, 10))
def binary_search(arr,   x, high, counter):
    #counter = 0
    # проверяем базовый случай
    if high >= arr[0]:
        counter += 1
        mid = (arr[0] + high) // 2
        if arr[mid] == x:
            return f'индекс {mid}, шагов{counter}'
        elif arr[mid] > x:
            return binary_search(arr,   x, mid - 1, counter)
        else:
            return binary_search(arr,   x, mid + 1, counter)
    else:
        return -1

print(binary_search(data, 6, len(data), 0))
