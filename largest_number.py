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

# def find_target_sum(list1, target):

#     result = []

#     for i in range(len(list1)-1):
#         for j in range(1, len(list1)):
#             if list1[i] + list1[j] == target:
#                 result.append(i)
#                 result.append(j)

#     return result


# print(find_target_sum([1,4,7,13], 17))
import json
import json

def isValid(stale, latest, otjson):
    cursor = 0
    otjson_dict = json.loads(otjson)
    new_stale = stale  # Create a new string to keep track of changes

    for item in otjson_dict:
        if item["op"] == "skip":
            cursor += item['count']
            if cursor > len(new_stale):
                return False
        
        elif item["op"] == "delete":
            count = item['count']
            if cursor + count > len(new_stale):
                return False
            new_stale = new_stale[:cursor] + new_stale[cursor+count:]
        
        elif item["op"] == "insert":
            chars = item["chars"]
            new_stale = new_stale[:cursor] + chars + new_stale[cursor:]
            cursor += len(chars)
    
    # After processing all operations, check if the resulting string matches the latest
    return new_stale == latest

# # Test cases
# print(isValid(
#     "Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.",
#     "Repl.it uses operational transformations.",
#     '[{"op": "skip", "count": 40}, {"op": "delete", "count": 47}]'
# ))  # Output: True

# print(isValid(
#     "Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.",
#     "Repl.it uses operational transformations.",
#     '[{"op": "skip", "count": 45}, {"op": "delete", "count": 47}]'
# ))  # Output: False

# print(isValid(
#     "Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.",
#     "We use operational transformations to keep everyone in a multiplayer repl in sync.",
#     '[{"op": "delete", "count": 7}, {"op": "insert", "chars": "We"}, {"op": "skip", "count": 4}, {"op": "delete", "count": 1}]'
# ))  # Output: True

# ... and so on for other test cases


# Test cases
print(isValid("Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.",
              "Repl.it uses operational transformations.",
              '[{"op": "skip", "count": 40}, {"op": "delete", "count": 47}]'))  # Output: True

print(isValid("Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.",
              "Repl.it uses operational transformations.",
              '[{"op": "skip", "count": 45}, {"op": "delete", "count": 47}]'))  # Output: False

print(isValid(
    'Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.',
    'Repl.it uses operational transformations.',
    '[{"op": "skip", "count": 40}, {"op": "delete", "count": 47}, {"op": "skip", "count": 2}]')
)  # false, skip past end

print(isValid(
    'Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.',
    'We use operational transformations to keep everyone in a multiplayer repl in sync.',
    '[{"op": "delete", "count": 7}, {"op": "insert", "chars": "We"}, {"op": "skip", "count": 4}, {"op": "delete", "count": 1}]'
) ) # true

print(isValid(
    'Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.',
    'We can use operational transformations to keep everyone in a multiplayer repl in sync.',
    '[{"op": "delete", "count": 7}, {"op": "insert", "chars": "We"}, {"op": "skip", "count": 4}, {"op": "delete", "count": 1}]'
))  # false

print(isValid(
    'Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.',
    'Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.',
    '[]'
) ) # true


# function isValid(stale, latest, otjson) {
#     let cursor = 0;
#     const otjsonArray = JSON.parse(otjson);

#     for (const item of otjsonArray) {
#         if (item.op === "skip") {
#             cursor += item.count;
#             if (cursor > stale.length) {
#                 return false;
#             }
#         } else if (item.op === "delete") {
#             const count = item.count;
#             if (cursor + count > stale.length) {
#                 return false;
#             }
#             cursor += count;
#         }
#     }

#     // After processing all operations, check if the resulting string matches the latest
#     return stale === latest;
# }

# // Test cases
# console.log(isValid(
#     "Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.",
#     "Repl.it uses operational transformations.",
#     '[{"op": "skip", "count": 40}, {"op": "delete", "count": 47}]'
# )); // Output: true

# console.log(isValid(
#     "Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.",
#     "Repl.it uses operational transformations.",
#     '[{"op": "skip", "count": 45}, {"op": "delete", "count": 47}]'
# )); // Output: false

# // ... and so on for other test cases
