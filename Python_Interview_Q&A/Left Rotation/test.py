def left_rotation(arr, d):
    n = len(arr)
    # Perform left rotation
    print(d % n)
    rotated_arr = arr[d % n:] + arr[:d % n]
    return rotated_arr

# Example usage:
arr = [1, 2, 3, 4, 5]
d = 3
rotated_arr = left_rotation(arr, d)
print(rotated_arr)  # Output: [3, 4, 5, 1, 2]
