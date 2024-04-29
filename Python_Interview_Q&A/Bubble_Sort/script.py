a = [100,50,1,9,22,97]


def custom_sort(arr):
    length = len(arr)
    for i in range(length-1,-1,-1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr



result = custom_sort(a)
print(result)