def find_equilibrium_index(arr):
    n = len(arr)
    if n == 0:
        return -1
    total_sum = sum(arr)
    left_sum = 0
    for i in range(n):
        right_sum = total_sum - left_sum - arr[i]
        if left_sum == right_sum:
            return i
        left_sum += arr[i]
    return -1
arr = [-7, 1, 5, 2, -4, 3, 0]
result = find_equilibrium_index(arr)
print("Equilibrium index:", result)
arr = [1, 2, 3]
result = find_equilibrium_index(arr)
print("Equilibrium index:", result)
