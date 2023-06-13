'''Problem: Given a list of integers, find the longest subarray with an equal number of even and odd elements. 
If multiple subarrays have the same maximum length, return any one of them.

For example, given the input list: [2, 4, 6, 3, 1, 8, 7], the longest subarray with an equal number of even and odd elements is [6, 3, 1, 8], with a length of 4.'''

# Here's a step-by-step approach to solving the problem:

# Initialize a variable max_length to store the length of the longest subarray found so far.
# Initialize a variable start_index to keep track of the starting index of the longest subarray.
# Create a dictionary called prefix_sums to store the cumulative difference between the count of even and odd elements encountered so far and their respective indices. The key in the dictionary represents the cumulative difference, and the value represents the index at which the cumulative difference is first encountered.
# Initialize prefix_sums[0] to -1, which represents the cumulative difference between even and odd elements when starting from the beginning of the list.
# Iterate through the input list and compute the cumulative difference between the count of even and odd elements encountered so far.
# If the cumulative difference is already present in prefix_sums, it means that the subarray between the current index and the index stored in prefix_sums has an equal number of even and odd elements. Check if the length of this subarray is greater than max_length. If so, update max_length and start_index.
# If the cumulative difference is not present in prefix_sums, add it to the dictionary with the current index as the value.
# After iterating through the entire list, extract the longest subarray using start_index and max_length.
# Return the longest subarray.

def longest_subarray(nums):
    max_length = 0
    start_index = 0
    prefix_sums = {0: -1}
    count_diff = 0

    for i, num in enumerate(nums):
        if num % 2 == 0:
            count_diff += 1
        else:
            count_diff -= 1
        
        if count_diff in prefix_sums:
            length = i - prefix_sums[count_diff]
            if length > max_length:
                max_length = length
                start_index = prefix_sums[count_diff] + 1
        else:
            prefix_sums[count_diff] = i

    return nums[start_index: start_index + max_length]


print(longest_subarray([2, 4, 6, 3, 1, 8, 7]))
print(longest_subarray([]))