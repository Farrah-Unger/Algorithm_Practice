'''Balanced Parentheses

Write a function that takes a string containing parentheses as input and checks whether the parentheses are balanced or not. A string of parentheses is considered balanced if each opening parenthesis has a corresponding closing parenthesis in the correct order.

For example, if the input string is "((()))", the function should return True since the parentheses are balanced. If the input string is "(()))", the function should return False since the parentheses are not balanced.'''

def check_balanced_parentheses(s):
    # Your implementation here
    # left_parens = '('
    # right_parens = ')'

    # left_counter = 0
    # right_counter = 0

    # for left_parens in s:
    #     left_counter += 1
    
    # for right_parens in s:
    #     right_counter += 1
    
    # if left_counter == right_counter:
    #     return True
    
    # return False
    
    stack = []

    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if len(stack) == 0 or stack[-1] != '(':
                return False
            stack.pop()

    return len(stack) == 0



input_string = "((()))"
result = check_balanced_parentheses(input_string)
print(result)  # Output: True
