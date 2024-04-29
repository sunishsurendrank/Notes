a = [10,12,800,9,5,100]

def find_max_number(arr):
    length = len(arr)
    max = a[0]
    for i in range(length):
        if max < a[i]:
            max = a[i]
    return max

def find_min_number(arr):
    length = len(arr)
    min = a[0]
    for i in range(length):
        if min > a[i]:
            min = a[i]
    return min
number = find_max_number(a)
print(number)
number = find_min_number(a)
print(number)