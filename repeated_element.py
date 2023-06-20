'''Problem: Repeated Element

Given a list of integers, write a function to determine if there are any repeated elements in the list. 
The function should return True if there are duplicates and False otherwise.'''

def repeated_element(list1):

    # set_list = set(list1)

    # if len(set_list) != len(list1):
    #     return True
    
    # return False

    # seen_set = set()

    # for element in list1:
    #     if element in seen_set:
    #         return True
    #     seen_set.add(element)

    # return False

        # num_hash = {}

    for num in list1:
        if num not in num_hash:
            num_hash[num] = 1
        else:
            num_hash[num] += 1
    
    for val in num_hash.values():
        if val > 1:
            return True
    
    return False

print(repeated_element([1,2,3,4,5,6,7,8,9,10,11]))
print(repeated_element([1,7,11,1,6,9,13]))
