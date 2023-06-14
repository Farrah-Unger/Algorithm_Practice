'''Problem: Count Unique Characters
Write a function that takes a string as input and returns the count of unique characters in the string. Treat uppercase and lowercase letters as distinct characters.

For example:
Input: "Hello World"
Output: 8
Explanation: The string "Hello World" contains 8 unique characters: 'H', 'e', 'l', 'o', 'W', 'r', 'd'.'''

# def count_unique_characters(string):

#     string_set = set(string)


#     return len(string_set)

# print(count_unique_characters("Hello World"))

'''Problem: Reverse Words in a String
Write a function that takes a string as input and returns the same string with the words reversed. A word is defined as a sequence of non-space characters.

For example:
Input: "Hello World"
Output: "World Hello"'''

# def reverse_words(string):

#     reverse_str = ''

#     for word in string.split():
#         reverse_str = word + ' ' + reverse_str 

#     return reverse_str

# print(reverse_words("Hello World"))

'''Problem: Palindrome Check
Write a function that takes a string as input and returns True if the string is a palindrome, and False otherwise. A palindrome is a word, phrase, number, or sequence of characters that reads the same backward as forward, disregarding spaces, punctuation, and capitalization.

For example:
Input: "Racecar"
Output: True

Input: "Hello World"
Output: False'''

def is_palindrome(string):

    lower_string = string.lower()
    reverse_str = ''
    string1 = ''

    for letter in range(len(lower_string) -1, -1, -1):
        reverse_str += lower_string[letter]
    print(reverse_str)
    
    for letter in range(len(lower_string)):
        string1 += lower_string[letter]
    print(string1)

    if len(reverse_str) != len(string1):
        return False
    elif reverse_str == string1:
        return True
    return False

      # if lower_string == lower_string[::-1]:
    #     return True
    # return False
    


print(is_palindrome("Racecar"))
print(is_palindrome("Hello World"))