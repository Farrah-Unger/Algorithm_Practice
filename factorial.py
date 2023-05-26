'''Calculate the Factorial

Write a function that takes a non-negative integer as input and calculates its factorial.

The factorial of a non-negative integer n, denoted by n!, is the product of all positive integers from 1 to n.

For example, if the input is 5, the factorial is calculated as 5! = 5 x 4 x 3 x 2 x 1 = 120.'''

def calculate_factorial(n):

    total = 1
    for num in range(n, 0, -1):
        total *= num
    return total
# Example usage:
num = 5
result = calculate_factorial(num)
print(result)  # Output: 120
