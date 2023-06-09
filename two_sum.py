'''TWO SUM
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
'''

# def two_sum(nums, target):
#   # Approach 1 # ENUMERATE function

#   lookup = {}  
#   for index, num in enumerate(nums):
#     second_num = target - num
#     if second_num in lookup:
#       return[lookup[second_num],index]
#     lookup[nums[index]] = index  
#   return []

  # Approach # 2 # hash map #
 # lookup = {}
 # for i in range(len(nums)):
 #   second_num = target-nums[i]
 #   if second_num in lookup:
 #     return(lookup[second_num], i)
 #   lookup[nums[i]] = i
   
 
  # # Both solutions: time O(n) -> n is len of nums list, iterates through list once, performing constant time operations for each element. Space O(n) -> dictionary stores n key-value pairs, resulting in O(n) space. 
    
# print(two_sum([3,4,1], 0))
# print(two_sum([2,7,11,15], 9)) # [0,1]
# print(two_sum([3,2,4], 6)) # [1,2]
# print(two_sum([3,3], 6)) # [0,1]

def two_sum(arr, target):
  
  if not arr:
    return []

  hash_map = {}
  result = []

  for index, num in enumerate(arr):
    total = target - num
    if total in hash_map:
      return [hash_map[total], index]
    hash_map[num] = index

  return []

  

print(two_sum([2, 7, 11, 15], 9))
print(two_sum([], 5))