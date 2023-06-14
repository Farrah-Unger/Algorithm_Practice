'''Write a Python function that takes in a string and returns the count of each character in the string as a dictionary. The keys in the dictionary should be the characters, and the values should be the corresponding counts.

For example, if the input string is "hello", the function should return {'h': 1, 'e': 1, 'l': 2, 'o': 1}.'''

def character_count(string):

    if not string:
        raise ValueError('string cannot be empty')

    letter_hash = {}

    for letter in string:
        if letter not in letter_hash:
            letter_hash[letter] = 1
        else:
            letter_hash[letter] += 1

    return letter_hash

print(character_count('hello'))
print(character_count(''))
