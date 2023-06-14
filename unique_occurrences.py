'''Problem: Unique Occurrences

Given an integer array nums, your task is to determine whether the array has the same number of unique elements as the number of occurrences of each element in the array.

Write a function unique_occurrences(nums) that takes in an integer array nums and returns 
True if the array has the same number of unique elements as the number of occurrences of each element. Otherwise, it should return False.

For example:

unique_occurrences([1, 2, 2, 1, 1, 3]) should return True because the array has 3 unique elements (1, 2, and 3), and the number of occurrences of each element is [3, 2, 1], which also has 3 unique elements.
unique_occurrences([1, 2]) should return False because the array has 2 unique elements (1 and 2), but the number of occurrences of each element is [1, 1], which has only 1 unique element.
'''

# create a dictionary where the key is the value of the index and the value is the amount of times it appears in the array
# create a set from the original array and compare the unique elements to the count

def unique_occurrences(arr):

    unique_hash = {}
    set_arr = set(arr)

    for num in arr:
        if num not in unique_hash:
            unique_hash[num] = 1
        else:
            unique_hash[num] += 1

    set_count = set(unique_hash.values())

    if len(set_arr) == len(set_count):
        return True
    
    return False

    
print(unique_occurrences([1, 2, 2, 1, 1, 3]))
print(unique_occurrences([1, 2]))