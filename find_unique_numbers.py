'''Problem: Given a list of integers, find the two numbers that appear only once. All other numbers in the list appear exactly twice. Return the two unique numbers in any order.

Example:
Input: [2, 4, 6, 8, 10, 2, 6, 10]
Output: [4, 8]'''

def find_unique_numbers(lst):

    if not lst:
        return []

    num_hash = {}
    result = []

    for i in lst:
        if i in num_hash:
            num_hash[i] += 1
        else:
            num_hash[i] = 1

    for key, val in num_hash.items():
        if val == 1:
            result.append(key)
    
    return result

print(find_unique_numbers([2, 4, 6, 8, 10, 2, 6, 10]))