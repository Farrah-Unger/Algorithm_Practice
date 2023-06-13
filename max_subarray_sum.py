'''Problem: Maximum Subarray Sum
Given an array of integers, find the contiguous subarray with the largest sum and return the sum.

For example:
Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6
Explanation: The subarray [4, -1, 2, 1] has the largest sum of 6.'''


# Initializing max_till_now = 0
# Initializing max_ending = 0
# Repeat steps 4 to 6 for every element in the array
# Set max_ending = max_ending + a[i]
# if (max_ending<0) then set max_ending = 0
# if (max_till_now < max_ending) then set max_till_now = max_ending
# return max_till_now


def max_subarray_sum(array):
    
    max_sum = 0
    max_ending = 0
    for num in range(len(array)):
        max_ending = max_ending + array[num]
        if max_ending < 0:
            max_ending = 0
        elif max_sum < max_ending:
            max_sum = max_ending     
    
    return max_sum
        

print(max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))