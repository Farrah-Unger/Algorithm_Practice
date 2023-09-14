'''
Write a function that, given a string of text (possibly with punctuation and line-breaks), 
returns an array of the top-3 most occurring words, in descending order of the number of occurrences.

Assumptions:
A word is a string of letters (A to Z) optionally containing one or more apostrophes (') in ASCII.
Apostrophes can appear at the start, middle or end of a word ('abc, abc', 'abc', ab'c are all valid)
Any other characters (e.g. #, \, / , . ...) are not part of a word and should be treated as whitespace.
Matches should be case-insensitive, and the words in the result should be lowercased.
Ties may be broken arbitrarily.
If a text contains fewer than three unique words, then either the top-2 or top-1 words should be returned, or an empty array if a text contains no words.

Examples:
top_3_words("In a village of La Mancha, the name of which I have no desire to call to
mind, there lived not long since one of those gentlemen that keep a lance
in the lance-rack, an old buckler, a lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income.")
# => ["a", "of", "on"]

top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e")
# => ["e", "ddd", "aa"]

top_3_words("  //wont won't won't")
# => ["won't", "wont"]
'''
# import string
# from collections import Counter

# def top_3_words(text):

#     translator = str.maketrans("", "", string.punctuation)

#     # Apply the translation table to the input string
#     result = text.translate(translator)

#     freq_map = {}
#     lower = result.lower()
#     split = lower.split()
    
#     word_count = Counter(split)
    
#     top_three = word_count.most_common(3)
# # # Print the results
#     result_list = []
#     for word, count in top_three:
#         result_list.append(word)
    
#     return result_list

# print(top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"))
# print(top_3_words("  //wont won't won't"))
# print(top_3_words("In a village of La Mancha, the name of which I have no desire to call to mind, there lived not long since one of those gentlemen that keep a lance in the lance-rack, an old buckler, a lean hack, and a greyhound for coursing. An olla of rather more beef than mutton, a salad on most nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra on Sundays, made away with three-quarters of his income."))

'''
Write a function that returns the count of characters that have to be removed in order to get a string with no consecutive repeats.

Note: This includes any characters

Examples
'abbbbc'  => 'abc'    #  answer: 3
'abbbbca'  => 'abca'   #  answer: 2
'ab cca'  => 'ab ca'  #  answer: 1
'''

# def count_repeats(txt):
    



# print(count_repeats('abbbbc'))
# print(count_repeats('abbca'))
# print(count_repeats('ab cca'))



'''Maria plays college basketball and wants to go pro. Each season she maintains a record of her play. She tabulates the number of times she breaks her season record for most points and least points in a game. Points scored in the first game establish her record for the season, and she begins counting from there.

Example

Scores are in the same order as the games played. She tabulates her results as follows:

                                     Count
    Game  Score  Minimum  Maximum   Min Max
     0      12     12       12       0   0
     1      24     12       24       0   1
     2      10     10       24       1   1
     3      24     10       24       1   1
Given the scores for a season, determine the number of times Maria breaks her records for most and least points scored during the season.

Function Description

Complete the breakingRecords function in the editor below.

breakingRecords has the following parameter(s):

int scores[n]: points scored per game
Returns

int[2]: An array with the numbers of times she broke her records. Index  is for breaking most points records, and index  is for breaking least points records.
Input Format

The first line contains an integer , the number of games.
The second line contains  space-separated integers describing the respective values of .

'''

# def breakingRecords(scores):
    
#     max_num = scores[0]
#     min_num = scores[0]

#     max_count = 0
#     min_count = 0

#     count_list = []

#     for i in range(1, len(scores)):
#         if scores[i] > max_num:
#             max_num = scores[i]
#             max_count += 1
#         elif scores[i] < min_num:
#             min_num = scores[i]
#             min_count += 1


#     count_list.append(max_count)
#     count_list.append(min_count)

#     return count_list



# print(breakingRecords([10, 5, 20, 20, 4, 5, 2, 25, 1]))
# print(breakingRecords([3, 4, 21, 36, 10, 28, 35, 5, 24, 42]))
# '''Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

# * url = "http://github.com/carbonfive/raygun" -> domain name = "github"
# * url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
# * url = "https://www.cnet.com"                -> domain name = cnet"
# '''
# #think about slicing after the first . and right before the next
# def domain_name(url):
#     pass

# print(domain_name("http://google.com"))
# print(domain_name("http://google.co.jp"))
# print(domain_name("www.xakep.ru"))
# print(domain_name("https://youtube.com"))

'''Pete likes to bake some cakes. He has some recipes and ingredients. Unfortunately he is not good in maths. 
Can you help him to find out, how many cakes he could bake considering his recipes?

Write a function cakes(), which takes the recipe (object) and the available ingredients (also an object) and 
returns the maximum number of cakes Pete can bake (integer). For simplicity there are no units for the amounts 
(e.g. 1 lb of flour or 200 g of sugar are simply 1 or 200). Ingredients that are not present in the objects, 
can be considered as 0.

Examples:

# must return 2
cakes({flour: 500, sugar: 200, eggs: 1}, {flour: 1200, sugar: 1200, eggs: 5, milk: 200})

# must return 0
cakes({apples: 3, flour: 300, sugar: 150, milk: 100, oil: 100}, {sugar: 500, flour: 2000, milk: 2000})
'''

# If the length of recipe > length of available, return 0.

# Create dict for counting availability of each ingredient
# Iterate through available dict:
    # Compare if available[key] matches recipe[key]:
        # divide available value by the recipe value  
        # store that as new value

# return min(dict.values())    
    
# def cakes(recipe, available):
    
#     if len(recipe) > len(available):
#         return 0
    
#     possible_cake = {}

#     for key in available:
#         if key in recipe:
#             cake_value = available[key] // recipe[key]
   
#             if key not in possible_cake:
#                 possible_cake[key] = cake_value

#     return min(possible_cake.values())

# print(cakes({"flour": 500, "sugar": 200, "eggs": 1}, {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200})) #2
# print(cakes({"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}, {"sugar": 500, "flour": 2000, "milk": 2000}))