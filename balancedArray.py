'''
We are interested in writing a function that determines if a sequence of numbers contains two pairs (a, b) and (c, d) such that a+b = c+d. 

Your function should accept a list of integers.

For example:
numbers = [3, 10, 4, 5, 2, 14]

3 + 4 = 2 + 5. Therefore your function should return {3, 2, 4, 5} as a set. 

Note that each element of the input list will be unique. Each input will have at most one solution. 
'''
# initialize a hash map where the keys are the sum of the integers being added and the values are the numbers that create the addition equation in tuple form.
# use a nested for loop to avoid repetition of indices
# create two variables to store the current value of the indices being added
# create a sum result to caclulate the sum of the indices being added
# if the sum is already in the hash map, then hold that sum and return the two tuples that add up to the sum in set form
# if the sum is not in the hash map, then add the result : (tuple of integers)



def balanced(numbers):
    
    hash_map = {}

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            x = numbers[i]
            y = numbers[j]
            sum_result = x + y

            if sum_result in hash_map:
                return {x, y, hash_map[sum_result][0], hash_map[sum_result][1]}
            else:
                hash_map[sum_result] = (x, y)

    return "No solution"
    

print(balanced([3, 10, 4, 5, 2, 14])) #set([3, 2, 4, 5])
print(balanced([60, 0, 10, -35, 90])) # set()
print(balanced([]))