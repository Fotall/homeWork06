# задача 1
arr = []
a1 = int(input('A1: '))
d = int(input('введите разность: '))
n = int(input('введите кол-во элементов: '))
an = 0
for i in range(1, n + 1):
    an = a1 + (i - 1) * d
    arr.append(an)
print(arr)

# задача 2
#array = [1,2,5,6,3,88,6,4]
from random import randint
array = []
for i in range(20):
    array.append(randint(1,10))
print(array)
n_min = 3
n_max = 7
array_final = []
array_index = []
for i in array:
    if n_min < array[i] < n_max:
        array_final.append(array[i])
        print(i, end = ' ')
    
print()
print(sorted(array_final))

