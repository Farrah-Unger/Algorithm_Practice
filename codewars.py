# def find_it(seq):
#     appearance_dict = {}
    
#     for num in seq:
#         if num not in appearance_dict:
#             appearance_dict[num] = 1
#         else:
#             appearance_dict[num] += 1
    
#     for key, value in appearance_dict.items():
#         if value % 2 != 0:
#             return key

    

# print(find_it([1,2,2,3,3,3,4,3,3,3,2,2,1]))
# print(find_it([1,1,2]))
# print(find_it([0,1,0,1,0]))

'''You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.

Examples
[2, 4, 0, 100, 4, 11, 2602, 36]
Should return: 11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21]
Should return: 160 (the only even number)'''

# def find_outlier(integers):
    
#     even_list = []
#     odd_list = []

#     for num in integers:
#         if num % 2 == 0:
#             even_list.append(num)
#         else:
#             odd_list.append(num)
    
#     if len(even_list) == 1:
#         return even_list[0]
#     else:
#         return odd_list[0]

    

# print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))
# print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))

'''In a factory a printer prints labels for boxes. For one kind of boxes the printer has to use colors which, for the sake of simplicity, are named with letters from a to m.

The colors used by the printer are recorded in a control string. For example a "good" control string would be aaabbbbhaijjjm meaning that the printer used three times color a, four times color b, one time color h then one time color a...

Sometimes there are problems: lack of colors, technical malfunction and a "bad" control string is produced e.g. aaaxbbbbyyhwawiwjjjwwm with letters not from a to m.

You have to write a function printer_error which given a string will return the error rate of the printer as a string representing a rational whose numerator is the number of errors and the denominator the length of the control string. Don't reduce this fraction to a simpler expression.

The string has a length greater or equal to one and contains only letters from ato z.

Examples:
s="aaabbbbhaijjjm"
printer_error(s) => "0/14"

s="aaaxbbbbyyhwawiwjjjwwm"
printer_error(s) => "8/22"'''

# def print_error(s):

# # numerator is error
# # denominator is length of the string
#     string_poss = "abcdefghijklmnopqrstuvwxyz"
#     n = len(s)
#     error_count = 0

#     for error in s:
#         if error in string_poss[14:]:
#             error_count += 1
        
#     return f"{error_count}/{n}"



# print(print_error("aaabbbbhaijjjm"))
# print(print_error("aaaxbbbbyyhwawiwjjjwwm"))

'''Take 2 strings s1 and s2 including only letters from a to z. Return a new sorted string, the longest possible, containing distinct letters - each taken only once - coming from s1 or s2.

Examples:
a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) -> "abcdefklmopqwxy"

a = "abcdefghijklmnopqrstuvwxyz"
longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"'''

# def longest(a1, a2):

#     set1 = set(a1)
#     set2 = set(a2)

#     final_Set = set1.union(set2)

#     sorted_str = ''.join((sorted(final_Set)))

#     return sorted_str

# print(longest("xyaabbbccccdefww","xxxxyyyyabklmopq"))

''' A coding competition is being organized  on the HackerRank platform. All participants need to be grouped into teams where each team has exactly two candidates and the sums of their skills must be qual for all teams. The efficiency of a team is the product of the skills of its members, e.g for a team with skills[2,3], the efficiency of the team is 2 * 3 = 6.

Find the sum of the efficiencies of the teams. If there is no way to create teams that satisfy the conditions, return -1.

Example:
The skills of the candidates are skill = [1, 2, 3, 2]. They can be paired as [[1, 3],[2,2]]. The sum of skills  for each team is the same, i.e, 4.
The efficiency is computed as:
- Efficiency of [1, 3] = 1 * 3 = 3
- Efficiency of [2, 2] = 2 * 2 = 4

Return the sum of efficiencies, 3 + 4 =7'''

# def getTotalEfficiency(skill):
  
#     if len(skill) % 2 !=  0:
#         return -1

#     total_sum = 0
#     for num in skill:
#         total_sum += num

#     if total_sum % 2 != 0:
#         return -1
    

# print(getTotalEfficiency([5, 4, 2, 1]))
# Sample input
# skill[] size, n = 4
#  skill = [5, 4, 2, 1]

# Form teams as [[1, 5], [4,2]]. The sums of each pair are 6.
# - Efficiency of [1, 5] = 1 * 5 = 5
# - Efficinecy of [4, 2] = 4 * 2 = 8

# # sample input
# skill[] size, n = 6
# skill = [2, 1, 1, 4, 3, 5]

# # sample output
# -1

'''
You are going to be given an array of integers. Your job is to take that array and find an index N where the sum of the integers to the left of N is equal to the sum of the integers to the right of N. If there is no index that would make this happen, return -1.

For example:

Let's say you are given the array {1,2,3,4,3,2,1}:
Your function will return the index 3, because at the 3rd position of the array, the sum of left side of the index ({1,2,3}) and the sum of the right side of the index ({3,2,1}) both equal 6.

Let's look at another one.
You are given the array {1,100,50,-51,1,1}:
Your function will return the index 1, because at the 1st position of the array, the sum of left side of the index ({1}) and the sum of the right side of the index ({50,-51,1,1}) both equal 1.

Last one:
You are given the array {20,10,-80,10,10,15,35}
At index 0 the left side is {}
The right side is {10,-80,10,10,15,35}
They both are equal to 0 when added. (Empty arrays are equal to 0 in this problem)
Index 0 is the place where the left side and right side are equal.

Note: Please remember that in most programming/scripting languages the index of an array starts at 0.

Input:
An integer array of length 0 < arr < 1000. The numbers in the array can be any integer positive or negative.

Output:
The lowest index N where the side to the left of N is equal to the side to the right of N. If you do not find an index that fits these rules, then you will return -1.

Note:
If you are given an array with multiple answers, return the lowest correct index.'''

# def find_even_index(arr):


#     for n in range(len(arr)-1):
#         left = sum(arr[:n])
#         right = sum(arr[n+1:])
#         if left == right:
#             return n
#     return -1



# print(find_even_index([1,2,3,4,3,2,1]))
# print(find_even_index([1,100,50,-51,1,1]))
# print(find_even_index([10,-80,10,10,15,35,20]))

'''Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

Examples:
Input: 42145 Output: 54421

Input: 145263 Output: 654321

Input: 123456789 Output: 987654321'''

# def descending_order(num):

#     new_string = str(num)
    
#     sorted_digits = sorted(new_string, reverse=True)

#     return int(''.join(sorted_digits))
        

# print(descending_order(42145))

'''Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

It should remove all values from list a, which are present in list b keeping their order.

array_diff([1,2],[1]) == [2]
If a value is present in b, all of its occurrences must be removed from the other:

array_diff([1,2,2,2,3],[2]) == [1,3]'''

# def array_diff(a, b):
    
    # freq_dict = {}

    # for i in a:
    #     if i not  in freq_dict:
    #         freq_dict[i] = 1
    #     else:
    #         freq_dict[i] += 1
    
    # for i in b:
    #     if i in freq_dict:
    #         del freq_dict[i]
    #     return list(freq_dict)

    # for key, val in freq_dict.items():
    #     if val > 1:
    #         result = []
    #         result.append(key)
    #         return result

#     result = []

#     for element in a:
#         if element not in b:
#             result.append(element)

#     return result

# print(array_diff([1,2],[1]))
# print(array_diff([1,2,2,2,3],[2]))
# print(array_diff([1,2,2],[1])) #[2,2]

'''Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

Example
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
The returned format must be correct in order to complete this challenge.

Don't forget the space after the closing parentheses!'''

# def create_phone_number(n):
    
#     new_str = ''
#     for num in str(n):
#         if num.isnumeric():
#             new_str += num


#     return f"({new_str[0:3]}) {new_str[3:6]}-{new_str[6:]}"


# print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))

'''Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

Examples:

spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" 
spinWords( "This is a test") => returns "This is a test" 
spinWords( "This is another test" )=> returns "This is rehtona test"'''

# def spin_words(sentence):
    
#     new_str = ''
#     for word in sentence.split():
#         if len(word) >= 5:
#             new_str += word[::-1] + ' '
#         elif len(word) < 5:
#             new_str += word + ' '
    
#     return new_str.rstrip()

# print(spin_words("Hey fellow warriors"))
# print(spin_words("This is a test"))
# print(spin_words("This is another test"))

'''There is an array with some numbers. All numbers are equal except for one. Try to find it!

find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
It’s guaranteed that array contains at least 3 numbers.

The tests contain some very huge arrays, so think about performance.'''

# def find_uniq(arr):
    
#     freq_dict = {}

#     for i in arr:
#         if i in freq_dict:
#             freq_dict[i] += 1
#         else:
#             freq_dict[i] = 1
        
#     for key, val in freq_dict.items():
#         if val == 1:
#             return key

# print(find_uniq([ 1, 1, 1, 2, 1, 1 ]))
# print(find_uniq([ 0, 0, 0.55, 0, 0 ]))

'''Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]'''

# def move_zeros(lst):
    
#     # zero_lst = []

#     # for num in lst:
#     #     if num == 0:
#     #         lst.remove(num)
#     #         zero_lst.append(num)
    
#     # final_list = lst + zero_lst

#     # return final_list
#     non_zero_lst = [num for num in lst if num != 0]
#     zero_count = len(lst) - len(non_zero_lst)
#     final_list = non_zero_lst + [0] * zero_count
#     return final_list

# print(move_zeros([1, 0, 1, 2, 0, 1, 3]))
# print(move_zeros([9, 9, 1, 2, 1, 1, 3, 1, 9, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0]))

'''Write a function that takes a string of braces, and determines if the order of the braces is valid. It should return true if the string is valid, and false if it's invalid.

This Kata is similar to the Valid Parentheses Kata, but introduces new characters: brackets [], and curly braces {}. Thanks to @arnedag for the idea!

All input strings will be nonempty, and will only consist of parentheses, brackets and curly braces: ()[]{}.

What is considered Valid?
A string of braces is considered valid if all braces are matched with the correct brace.

Examples
"(){}[]"   =>  True
"([{}])"   =>  True
"(}"       =>  False
"[(])"     =>  False
"[({})](]" =>  False'''

def valid_braces(string):
  
    if len(string) % 2 != 0:
        return False
    
    valid_map = {
        "(" : ")",
        "[" : "]",
        "{" : "}"
    }

    stack = []

    for left_paren in string:
        if left_paren == "(" or left_paren == "[" or left_paren == "{":
            stack.append(left_paren)

    
    for right_paren in string:
        if right_paren == ")" and right_paren == valid_map.values() or right_paren == "]" or right_paren == "}" :
            stack.pop()
    
    print(stack)

    # myStack = []

    # for left_paren in string:
    #     if left_paren == "(" or left_paren == "[" or left_paren == "{":
    #         myStack.append(left_paren)
    # print(myStack) 

    # for right_paren in string[::-1]:
    #     if right_paren == "}" or right_paren == "]" or right_paren == ")":
    #         myStack.pop()
    # print(myStack)

print(valid_braces("(){}[]"))
print(valid_braces("([{}])"))
print(valid_braces("(}"))
print(valid_braces("[(])"))
print(valid_braces("[({})](]"))