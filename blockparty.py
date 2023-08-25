'''In a language of your choice, please write a function that will output the indices of the two consecutive elements that have 
the highest max sum in an input array of integers (e.g., maxPair([0, 5, 5, 2]) will return (1, 2)). 
In the case of a tie, the method should return the leftmost pair (e.g., maxPair([0, 4, 3, 1, 2, 3, 4, 0]) will return (1, 2)).'''

    # highest_indices = (i, i+1)
    # max_sum = 0, which will keep getting reassigned
    # when we're adding up the 2 numbers, account for if the sums are equal give the leftmost indices
    # if the max_sum is <= to current, it stays the same. 
    # if the max_sum is > than current, then reassign
    # range(len)-1
    # need pointers i, and i + 1
    
def highest_max_indices(lst):
    if len(lst) < 2:
        return None
        
    
    max_sum = float('-inf')
    for i in range(len(lst)-1):
        if lst[i] + lst[i + 1] > max_sum:
            max_sum = lst[i] + lst[i + 1]
            pair = (i, i+1)
            
    return pair

print(highest_max_indices([0, 4, 3, 1, 2, 3, 4, 0])) # (1,2) # tuple of indices
print(highest_max_indices([0, 5, 5, 2])) # (1,2) # tuple of indices
print(highest_max_indices([])) # None
print(highest_max_indices([2,5,7,9])) # (2,3)
print(highest_max_indices([-2,-5,-7,-9])) # (0,1)
print(highest_max_indices([10, -20, 15, -5]))  # (2,3)

