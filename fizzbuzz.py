'''"FizzBuzz" is a classic programming problem that is often used as an interview question. The task is to write a program that prints the numbers from 1 to n, replacing numbers that are multiples of 3 with "Fizz", multiples of 5 with "Buzz", and multiples of both 3 and 5 with "FizzBuzz". The program should follow these rules:

Print the numbers from 1 to n.
For numbers that are multiples of 3, print "Fizz" instead.
For numbers that are multiples of 5, print "Buzz" instead.
For numbers that are multiples of both 3 and 5, print "FizzBuzz".'''

def FizzBuzz(n):

    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

#Try Recursively

FizzBuzz(15)