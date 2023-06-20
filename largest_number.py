'''Problem: Largest Number

Given a list of positive integers, write a function to find the largest number that can be formed by concatenating the elements of the list.

For example:

Input: [54, 546, 548, 60]
Output: 6054854654'''

# Convert the list of integers to a list of strings so that we can perform string concatenation.
# Implement a custom comparison function to compare two numbers as strings. The function should compare a and b as ab and ba and return the result of the comparison.
# Sort the list of strings using the custom comparison function. This will place the numbers in the desired order to form the largest number.
# Join the sorted list of strings into a single string.
# Return the resulting string as the largest number.

# from functools import cmp_to_key

# def largest_number(list1):
#     # Convert the list of integers to a list of strings
#     string_list = [str(num) for num in list1]

#     # Implement custom comparison logic
#     def compare(a, b):
#         if int(a + b) > int(b + a):
#             return -1
#         elif int(a + b) < int(b + a):
#             return 1
#         else:
#             return 0

#     # Sort the string list using the custom comparison function
#     sorted_list = sorted(string_list, key=cmp_to_key(compare))

#     # Concatenate the sorted strings to form the largest number
#     largest_num = ''.join(sorted_list)

#     return largest_num

# print(largest_number([54, 546, 548, 60]))

'''Problem:
Given an array of integers, find the maximum element in the array.

Input:
An array of integers.

Output:
The maximum element in the array.'''

# def max_nums(array):

#     max_num = 0

#     for num in array:
#         if num > max_num:
#             max_num = num
    
#     return max_num

# print(max_nums([2,7,37,5,-2]))

'''Problem:
Given a list of integers, find the two numbers that, when added together, give a specific target sum. You need to return the indices of the two numbers in the list.

Input:

A list of integers.
A target sum, an integer value.
Output:

A pair of indices (i, j) representing the positions of the two numbers in the list.
If there are multiple valid solutions, return any one of them.
If no solution exists, you can return any appropriate indication (e.g., None, -1, or an empty pair).'''

def find_target_sum(list1, target):

    result = []

    for i in range(len(list1)-1):
        for j in range(1, len(list1)):
            if list1[i] + list1[j] == target:
                result.append(i)
                result.append(j)

    return result


print(find_target_sum([1,4,7,13], 17))
