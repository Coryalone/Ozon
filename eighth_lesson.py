import random
import time

#задание 1

animals = ['питон', 'питон', 'кит', 'собака', 'питон', 'кит', 'кошка', 'горилла', 'кит', 'кошка', 'жираф',\
 'леопард', 'жираф', 'жираф', 'кошка', 'горилла', 'жираф', 'жираф', 'кошка', 'жираф', 'кошка', 'кошка', 'собака', 'кит',
'жираф', 'леопард', 'жираф', 'собака', 'кит', 'кит', 'кит', 'жираф', 'собака', 'собака', 'кит', 'питон', 'леопард',\
 'кошка', 'жираф', 'собака', 'кошка', 'жираф', 'кошка', 'собака', 'кит', 'леопард', 'леопард', 'горилла',
'горилла', 'кит']

def line_search(arr, beast):
    list_of_beasts = []
    for i in range(len(arr)):
        if arr[i] == beast:
            list_of_beasts.append(i)
    return  list_of_beasts 

unique_beasts = set(animals)

for i in unique_beasts:
    print(i, line_search(animals, i))
print()

#задание 2

random_list = [5, 4, 7,40, 10, 40, 20, 30,1]

def bubble_sort(nums):
    #сортирую по умолчанию от меньшего к большему
    swapped = True # чтобы цикл запустился хотябы один раз
    while swapped:
        swapped = False
        for i in range(len(random_list) - 1):
            if nums[i] < nums[i+1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                print(nums)
                swapped = True
print(random_list)
bubble_sort(random_list)
print()

#задание 3

def selection_sort(input_list):
    start_time = time.time() # время старта функции
    for i in range(len(input_list)):
        min_i = i
        for j in range(i + 1, len(input_list)):
            if input_list[min_i] > input_list[j]: min_i = j
        input_list[i], input_list[min_i] = input_list[min_i], input_list[i]
    return time.time() - start_time # время выполнения в секундах

list_of_generetion = [random.randrange(0, 1000) for i in range(1000)]

def list_generate(number):
    list_of_generetion = [random.randrange(0, number) for i in range(number)]
    return list_of_generetion

list_of_numbers = [1000, 2000, 5000, 10000]
for i in range(len(list_of_numbers)):
    print(list_of_numbers[i], selection_sort(list_generate(list_of_numbers[i])))
print()
#размер массива и его наполнение влияет на скорость работы сортировки 

#задание 4

def bubble_sort(nums):
    start_time = time.time() # время старта функции
    #сортирую по умолчанию от меньшего к большему
    swapped = True # чтобы цикл запустился хотябы один раз
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                #print(nums)
                swapped = True
    return time.time() - start_time # время выполнения в секундах
    
for i in range(len(list_of_numbers)):
    print(list_of_numbers[i], bubble_sort(list_generate(list_of_numbers[i])))              

#размер массива и его наполнение влияет на скорость работы сортировки, у обоих сложности О(n**2),\
# но в зависимости от размера массива и его "вредности" скорость работы разная  