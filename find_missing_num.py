'''Problem: Finding the Missing Number

You are given an array of distinct integers from 0 to n, where n is the length of the array. 
However, one number is missing from the array. Your task is to write a function that finds and returns the missing number.
Input:

nums: A list of distinct integers from 0 to n, where n is the length of the array. The length of the list is (n + 1).
Output:

Return the missing number as an integer.
'''

# Initialize a variable n with the length of the input list nums.
# Calculate the expected sum of numbers from 0 to n using the formula expected_sum = n * (n + 1) / 2.
# Iterate through each element num in the input list nums:
# Subtract num from the expected_sum.
# After the iteration, the value of expected_sum will be the missing number.
# Return the value of expected_sum as the missing number.

def find_missing_number(nums):

    # max_nums = max(nums)
    
    # for i in range(max_nums + 1):
    #     if i not in nums:
    #         return i

    # ---------------------------------------------------------------- 
    n = len(nums)
    expected_sum = n * (n + 1) / 2

    for i in nums:
        expected_sum -= i
    
    return expected_sum


print(find_missing_number([3, 1, 0, 5, 2])) # 4
