def recursive_function(x):
    if x == 0:
        return 0
    else:
        return x + recursive_function(x-1)

result = recursive_function(10000)
print(result)


