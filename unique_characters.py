'''Problem: Count Unique Characters
Write a function that takes a string as input and returns the count of unique characters in the string. Treat uppercase and lowercase letters as distinct characters.

For example:
Input: "Hello World"
Output: 8
Explanation: The string "Hello World" contains 8 unique characters: 'H', 'e', 'l', 'o', 'W', 'r', 'd'.'''

def count_unique_characters(string):

    string_set = set(string)


    return len(string_set)

print(count_unique_characters("Hello World"))