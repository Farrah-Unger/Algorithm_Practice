'''Problem: Find the Missing Number
Given a list of numbers from 1 to n, with one number missing, write a function find_missing_number(nums) that takes the list of numbers as input and returns the missing number.

For example:

Input: [1, 2, 4, 5], Output: 3
Input: [1, 3, 4, 5, 6], Output: 2
Input: [2, 3, 1, 5], Output: 4'''

def find_missing_number(nums):

#   missing_num = None

#   for num in range(1, len(nums) - 1):
#     if nums[num] + 1 != nums[num+1]:
#         missing_num = nums[num] + 1
#         break

#   return missing_num
# ________________________________________________________________________________________________________________________________

    expected_sum = (len(nums) + 1) * (len(nums) + 2) // 2

    actual_sum = sum(nums)

    missing_number = expected_sum - actual_sum

    return missing_number



print(find_missing_number([1, 2, 4, 5]))
print(find_missing_number([1, 3, 4, 5, 6]))
print(find_missing_number([2, 3, 1, 5]))