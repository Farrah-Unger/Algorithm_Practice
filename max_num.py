"""Find the max number in a list of integers"""

def find_max_num(list1):
    
    # max_num = max(list1)

    # return max_num
# ________________________________________________________________
# trying with reassignment

    max_num = 0

    for num in list1:
        if num > max_num:
            max_num = num
    
    return max_num

print(find_max_num([1,7,9,12,5,3]))
print(find_max_num([25,98,42,1,78]))
print(find_max_num([43,71,87,22,95]))

# Time complexity is 0(N) as it is dependent on the array length
#  Space complexity is 0(1) as it is dependent on the integer