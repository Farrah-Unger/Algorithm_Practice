'''139. Word Break
Medium

Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence 
of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false

Constraints:

1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
'''
# take word from wordDict and check against s
# if wordDict[i] in s, then slice s to remove that word
# check next word to see if it exists
# if all the words in s exists, it's True

# def wordBreak(s, wordDict):
#     list_of_lengths = (lambda x:[len(i) for i in x])(wordDict)
#     print("list_len",list_of_lengths)
#     for i in range(len(wordDict)):
#         print("i",i)
#         word_len = len(wordDict[i])
#         if wordDict[i] in s:
#             s = s[list_of_lengths[i]:] # s[:len(i)+1]
#             print("s",s)
#             continue
#         else:
#             return False
#     return True

# print(wordBreak("leetcode", ["leet","code"])) # True
# print(wordBreak("applepenapple", ["apple","pen"])) # True
# print(wordBreak( "catsandog", ["cats","dog","sand","and","cat"])) # False
# print(wordBreak( "catsandog", ["cats","an","dog"])) # True
# # print(wordBreak("bb", ["a","b","bbb","bbbb"])) # True


'''https://leetcode.com/problems/maximum-subarray/
Given an integer array nums, find the 
subarray with the largest sum, and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

'''
# two pointers -> i, j ?
# initialize max_sum variable to be the entire sum of array
# current_sum variable -> sum(nums[i:j])
# max_sum = max(current_sum, max_sum)
# current sum is at 0
# everytime we add the num 

# Initialize two variables: max_sum to keep track of the maximum subarray sum encountered so far, and current_sum to keep track of the sum of the current subarray.

# Iterate through the array of numbers. For each number:

# Add the current number to current_sum.
# If current_sum becomes negative, reset it to zero. This is because a negative sum isn't beneficial to the overall sum, so it's better to start a new subarray from the next element.
# Update max_sum with the maximum value between itself and current_sum. This step ensures you're always tracking the maximum subarray sum encountered.

# Continue this process for all elements in the array.

# def maxSubArray(nums):
#     if len(nums) == 1:
#         return nums[0]

#     max_sum = float("-inf'") 
#     current_sum = 0
    

#     for num in nums: 
#         current_sum += num
#         current_sum = max(current_sum,num)
#         max_sum = max(max_sum, current_sum) # 6
#     print(max_sum)
    
    

# # print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))#6  
# print(maxSubArray([-2,-1,-3,-1-5,-4]))#6  
# # print(maxSubArray([1]))#1
# # print(maxSubArray([5,4,-1,7,8]))#23


# # Neetcode solution #
# maxSub = nums[0]
# currSum = 0
# for n in nums:
#     if currSum < 0:
#         currSum = 0
#     currSum += n
#     maxSub = max(maxSub, currSum)
# return maxSub

'''Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. 
Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.

 

Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).'''

# def removeDuplicates(nums):

#     if len(nums) == 0:
#         return 0
    
#     unique_count = 1  # Initialize count for the first element (it's always unique)
    
#     for i in range(1, len(nums)):
#         if nums[i] != nums[i - 1]:
#             nums[unique_count] = nums[i]
#             unique_count += 1
    
#     return unique_count

#     # i=1
#     # while(i<len(nums)):
#     #     if nums[i-1]==nums[i]:
#     #         nums.pop(i)
#     #         i-=1
#     #     i+=1
#     # return len(nums)         

# print(removeDuplicates([1,1,2]))
# print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))

'''27. Remove Element
Easy
927
1.2K
Companies
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.
Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int val = ...; // Value to remove
int[] expectedNums = [...]; // The expected answer with correct length.
                            // It is sorted with no values equaling val.

int k = removeElement(nums, val); // Calls your implementation

assert k == expectedNums.length;
sort(nums, 0, k); // Sort the first k elements of nums
for (int i = 0; i < actualLength; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.


Example 1:

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).'''

# def removeElement(nums, val):

#     count = 0

#     for i in range(len(nums)-1, -1, -1):
#         if nums[i] == val:
#             count += 1
#             nums.remove(nums[i])

#     return count

# # print(removeElement([3,2,2,3], 3))
# print(removeElement([0,1,2,2,3,0,4,2], 2))

'''28. Find the Index of the First Occurrence in a String
Easy
4.5K
233
Companies
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
'''

# def strStr(haystack, needle):

    # if needle not in haystack:
    #     return -1 

    # new_str = ""

    # for letter in haystack:
    #     if letter in needle:
    #         new_str += letter
    # print(new_str)

    # if new_str == needle:
    #     return haystack[needle]

#     if not needle:
#         return 0
    
#     for i in range(len(haystack) - len(needle) + 1):
#         if haystack[i:i + len(needle)] == needle:
#             return i
    
#     return -1


# print(strStr("sadbutsad", "sad"))
# print(strStr("leetcode", "leeto"))

'''Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4'''

# def searchInsert(nums, target):
# Binary Search Logic:

# Start with defining a left pointer at the beginning of the array and a right pointer at the end of the array.
# Calculate the middle index between the left and right pointers.
# Compare the value at the middle index with the target value:
# If they are equal, you found the target and can return the index.
# If the middle value is less than the target, it means the target should be on the right half. Update the left pointer to the middle + 1.
# If the middle value is greater than the target, it means the target should be on the left half. Update the right pointer to the middle - 1.
# Repeat steps 2-3 until the left pointer is less than or equal to the right pointer.    

    # left = 0
    # mid = len(nums) // 2
    # right = len(nums) -1
 

    # if target == nums[mid]:
    #     return mid
    # elif target < nums[mid]:
    #     nums = nums[:mid]
    #     left += 1
    # elif target > nums[mid]:
    #     nums = nums[mid:]
    #     right -= 1


#     left = 0
#     right = len(nums) - 1

#     while left <= right:
#         mid = (left + right) // 2  # Calculate mid within the loop
        
#         if target == nums[mid]:
#             return mid
#         elif target < nums[mid]:
#             right = mid - 1
#         else:
#             left = mid + 1

#     return left


# # print(searchInsert([1,3,5,6], 5)) 
# print(searchInsert([1,3,5,6], 2)) 
# print(searchInsert([1,3,5,6], 7)) 

'''
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.'''

#Psudeocode
# Enumerate 

# def canJump(nums):

# #   new_dict = {}

# #   for i, j in enumerate(nums):
# #     new_dict[i] = j
# #   print(new_dict)

#     for i in range(len(nums)-1, -1, -1):
#         print(nums[i])


# print(canJump([2,3,1,1,4])) #True
# print(canJump([3,2,1,0,4])) #False

# def birthdayCakeCandles(candles):
    
#     # max_num = 0
#     # count = 0
    
#     # for height in candles:
#     #     if height > max_num:
#     #         max_num = height
#     #         count += 1
#     # print(count)
#     # print(max_num)

#     freq_dict = {}

#     for num in candles:
#         if num in freq_dict:
#             freq_dict[num] += 1
#         else:
#             freq_dict[num] = 1

#     max_num = max(freq_dict)
    
#     for key, val in freq_dict.items():
#         if key == max_num:
#             return val



# print(birthdayCakeCandles([3,1,2,3]))

'''Given a time in -hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

Example


Return '12:01:00'.


Return '00:01:00'.

Function Description

Complete the timeConversion function in the editor below. It should return a new string representing the input time in 24 hour format.

timeConversion has the following parameter(s):

string s: a time in  hour format
Returns

string: the time in  hour format
Input Format

A single string  that represents a time in -hour clock format (i.e.:  or ).'''

# def timeConversion(s):
#     pass

# print(timeConversion('12:01:00'))

'''HackerLand University has the following grading policy:

Every student receives a  in the inclusive range from  to .
Any  less than  is a failing grade.
Sam is a professor at the university and likes to round each student's  according to these rules:

If the difference between the grade and the next multiple of 5 is less than 3, round  up to the next multiple of 5.
If the value of grade is less than 38, no rounding occurs as the result will still be a failing grade.
Examples

84 round to  (85 - 84 is less than 3)
29 do not round (result is less than 40)
57 do not round (60 - 57 is 3 or higher)
Given the initial value of  for each of Sam's  students, write code to automate the rounding process.

Function Description

Complete the function gradingStudents in the editor below.

gradingStudents has the following parameter(s):

int grades[n]: the grades before rounding
Returns

int[n]: the grades after rounding as appropriate'''



# print(floor(82))


# def gradingStudents(grades):

#     def myround(x, base=5):
#         return base * round(x/base)

#     result = []

#     for grade in grades:
#         update = myround(grade, base=5)
#         if grade < 38:
#             result.append(grade)
#         elif update - grade == 2 or update - grade == 1:
#             result.append(update)
#         else:
#             result.append(grade)

#     return result
        
# print(gradingStudents([73,67,38,33]))

'''739. Daily Temperatures
Medium

Given an array of integers temperatures represents the daily temperatures, return 
an array answer such that answer[i] is the number of days you have to wait after 
the ith day to get a warmer temperature. If there is no future day for which this 
is possible, keep answer[i] == 0 instead.

Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0]

Constraints:
1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100
'''
# Pseudocode
# Initialize result list
# Initialize days_counter as a variable (inside of for loop)
# Iterate through temperatures
# If the next temperature is greater than the current, increment days_counter 
    # Append days_counter to result list
# If the the next temp is lower than current, add 1 to days_counter and continue
# If we're at temperatures[-1], append 0 to result list 
# Return result list

# def dailyTemperatures(temperatures):
#     result = []
#     days_counter = 0



#     for i in range(len(temperatures)-1):
#         current_temp = temperatures[i]
#         comparison_day = i + 1 # right pointer      
        
#         if current_temp > temperatures[comparison_day]: # 75 > 71
#             days_counter += 1
#             comparison_day += 1
#             # for loop or while loop here?
            
#         elif current_temp < temperatures[comparison_day]: # 
#             days_counter += 1
#             result.append(days_counter)
#             days_counter = 0
    

#     if temperatures[-1]:
#         result.append(0)
        
#     print(result)

# print(dailyTemperatures([73,74,75,71,69,72,76,73])) 
# print(dailyTemperatures([73,74,75,71,69,72,76,73])) #[1,1,4,2,1,1,0,0]
# print(dailyTemperatures([30,40,50,60])) #[1,1,1,0]
# print(dailyTemperatures([30,60,90])) # [1,1,0]

'''You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, 
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.'''

# Hint: Since you're merging nums2 into the nums1 array, you can start by positioning the pointers at the end of both arrays (m + n - 1 for nums1 and n - 1 for nums2). 
# This allows you to work in a "backwards" manner, which can help avoid overwriting elements in nums1 and make it easier to handle the zeroes.

# Now, as you iterate through the arrays from the end, compare the elements at the current positions of the pointers. If the element from nums1 is larger, place it at the end of the merged array (position m + n - 1) 
# and decrement the pointer for nums1. If the element from nums2 is larger, place it at the end of the merged array and decrement the pointer for nums2.



def merge(nums1, m, nums2, n) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """

    last = m + n-1

    while m > 0 and n > 0:
        if nums1[m -1] > nums2[n-1]:
            nums1[last] = nums1[m-1]
            m -= 1
        else:
            nums1[last] = nums2[n-1]
            n -= 1
        last -= 1

    while n > 0:
        nums1[last] = nums2[n-1]
        n, last = n -1, last -1
    
    
    return nums1


print(merge([1,2,3,0,0,0], 3, [2,5,6], 3)) # [1,2,2,3,5,6]
print(merge([1], 1, [], 0)) # [1]
print(merge([0], 0, [1], 1)) # [1]