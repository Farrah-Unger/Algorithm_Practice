def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n - 1):
        # Last i elements are already in place
        for j in range(n - i - 1):
            print(i, j)
            # Swap if the current element is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Example usage:
my_list = [5, 2, 9, 1, 3]
bubble_sort(my_list)
print(my_list)  # Output: [1, 2, 3, 5, 9]

# Time complexity is 0(n^2) due to the outer and inner loops
# Space complexity is 0(n) as it's dependent on the length of the array
