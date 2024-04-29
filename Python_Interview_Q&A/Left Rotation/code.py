def left_rotation(arr, d):
    n = len(arr)
    # Calculate the effective number of rotations
    d = d % n
    print(d)

    # Create a new array to store the rotated elements
    rotated_arr = [0] * n

    # Perform left rotation
    for i in range(n):
        rotated_arr[i] = arr[(i + d) % n]

    return rotated_arr

# Example usage:
arr = [1, 2, 3, 4, 5]
d = 1
rotated_arr = left_rotation(arr, d)
print(rotated_arr)
