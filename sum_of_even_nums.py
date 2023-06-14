'''Question:
Write a Python function that takes in a list of integers and returns the sum of all even numbers in the list. If the list is empty or contains no even numbers, 
the function should return 0.

For example, if the input list is [1, 2, 3, 4, 5, 6], the function should return 12 (since the even numbers in the list are 2, 4, and 6).'''

def sum_of_even_numbers(list1):

    sum = 0
    for num in list1:
        if num % 2 == 0:
            sum += num
    
    return sum


print(sum_of_even_numbers([1, 2, 3, 4, 5, 6]))