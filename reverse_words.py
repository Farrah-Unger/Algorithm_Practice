'''Reverse Words in a String

Write a function that takes a string as input and returns the string with the order of the words reversed.

For example, if the input string is "Hello World!", the function should return "!World Hello".

You can assume that the input string does not contain leading or trailing spaces, and the words are separated by 
a single space. The function should handle punctuation and special characters as part of the words.
'''


def reverse_words(s):
    
    # reversed_str = ""
    # word = ""
    
    # for char in s:
    #     if char.isalnum():  # Check if the character is alphanumeric
    #         word += char
    #     else:
    #         if word:  # Append the reversed word to the result if it exists
    #             reversed_str = word + " " + reversed_str
    #             word = ""
    
    # if word:  # Append the last word to the result
    #     reversed_str = word + " " + reversed_str
    
    # return reversed_str.rstrip()  # Remove trailing spaces

# slicing method
    words = s.split()
    reversed_words = words[::-1]
    reversed_str = ' '.join(reversed_words)
    return reversed_str
    
# Example usage:
input_string = "Hello World!"
result = reverse_words(input_string)
print(result)  # Output: "!World Hello"
