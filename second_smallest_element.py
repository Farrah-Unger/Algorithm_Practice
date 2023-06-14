'''Question:
Write a Python function that takes in a list of integers and returns the second smallest number from the list. If the list has fewer than two elements, 
the function should return None.

For example, if the input list is [5, 2, 8, 1, 9], the function should return 2.'''

# remove the min element and return the new min
# sort the array and return the second index [1]

def second_smallest_number(lst):

    # if len(lst) < 2:
    #     return None

    # sorted_lst = sorted(lst)
    # return lst[1]

    #  min_num = min(lst)

    # for num in lst:
    #     if num == min_num:
    #         lst.remove(min_num)
    
    # return min(lst)

    min_num = float('inf')
    second_min = float('inf')

    for num in lst:
        if num < min_num:
            second_num = min_num
            min_num = num
        elif num < second_num and num != min_num:
            second_num = num

    return second_num
        

print(second_smallest_number([5, 2, 8, 1, 9]))