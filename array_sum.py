"""Problem: Array Sum
Write a function array_sum(nums) that takes an array of integers nums as input and returns the sum of all the numbers in the array.

For example:

Input: [1, 2, 3, 4, 5]
Output: 15 (1 + 2 + 3 + 4 + 5 = 15)

Input: [2, 4, 6, 8, 10]
Output: 30 (2 + 4 + 6 + 8 + 10 = 30)

Input: [-1, 0, 1, 2, 3]
Output: 5 (-1 + 0 + 1 + 2 + 3 = 5)"""

def array_sum(nums):
    
    total = 0

    for i in range(len(nums)):
        total += nums[i]
    
    return total
    

print(array_sum([1, 2, 3, 4, 5]))
print(array_sum([2, 4, 6, 8, 10]))
print(array_sum([-1, 0, 1, 2, 3]))

# Time complexity is 0(N) as it depends on the size of the array
# Space complexity is 0(1) as the return is a counter