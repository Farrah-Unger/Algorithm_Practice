'''Challenge: Word Frequency Count
Write a function that takes a string as input and returns a dictionary containing the frequency count of each word in the string. You can assume that the input string only contains lowercase alphabets and spaces. The words in the string are separated by a single space, and there are no leading or trailing spaces.

Example:
Input: "the quick brown fox jumps over the lazy dog"
Output: {'the': 2, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1}

You can implement this algorithm by defining a function word_frequency that takes a string as input and returns a dictionary with word frequencies. Remember to handle edge cases, such as an empty string.'''

test_string = 'the quick brown fox jumps over the lazy dog'

def word_frequency():

    freq_dict= {}
    split_string = test_string.split()
    for word in split_string:
        if word not in freq_dict:
            freq_dict[word] = 1
        else:
            freq_dict[word] += 1
    
    print(freq_dict)
    return freq_dict

word_frequency()