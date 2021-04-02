def bs_new_born(array, item):
    return private_bs_new_born(array, item, 0, len(array)-1)

def private_bs_new_born(array, item, low, high):
    if (array[low] <= array[high]):
        mid = (low + high) // 2
        guess = array[mid]

        if guess == item:
            return mid
        if guess > item:
            return private_bs_new_born(array, item, low, mid - 1)
        else:
            return private_bs_new_born(array, item, mid + 1, high)
    return 'Are you sure?'

my_list = list(range(0, 1000, 1))

print(bs_new_born(my_list, 10))
