

# try:
#     num1 = int(input("Enter a numerator: "))
#     num2 = int(input("Enter a denominator: "))
#     result = num1 / num2
#     print("Result:", result)
# except ValueError:
#     print("Invalid input. Please enter integers.")
# except ZeroDivisionError:
#     print("Cannot divide by zero.")
# else:
#     print("Division performed successfully.")
# finally:
#     print("End of the program.")

# def find_sum(num1, num2):

#     if not isinstance(num1, int) or not isinstance(num2, int):
#         raise TypeError("Inputs must be integers")
#     if num1 < 0 or num2 < 0:
#         raise ValueError("Inputs must be positive integers")

#     return num1 + num2


# print(find_sum(-2, 4))

# def find_sum(num1, num2):
#     if not isinstance(num1, int) or not isinstance(num2, int):
#         raise TypeError("Inputs must be integers")
#     if num1 < 0 or num2 < 0:
#         raise ValueError("Inputs must be positive integers")
#     return num1 + num2

# try:
#     print(find_sum(-2, 4))
# except TypeError as e:
#     print("TypeError:", str(e))
# except ValueError as e:
#     print("ValueError:", str(e))

# def do_weird_number_math(apple):
#     print("We're entering the do_weird_number_math function! Value of apple:", apple)

#     try:
#         if apple < 10:
#             banana = apple / (apple - 3)

#         print("Value of banana:", banana)
#         print("Value of carrot:", carrot)
#     except ZeroDivisionError as err:
#         print(f"apple is 3, so it tried to divide by zero. {err}")
#     except UnboundLocalError as err:
#         print(f"apple is valid, but banana was never given a value, so we get an error. {err}")
#     except NameError as err:
#         print(f"We're trying to print carrot, but carrot is never defined before this. {err}")

#     print("**************")

# # The following line raises a ZeroDivisionError
# do_weird_number_math(3)

# # The following line raises an UnboundLocalError
# do_weird_number_math(5555)

# # This line raises a NameError
# do_weird_number_math(8)


# def multiply_number(num1, num2):
#     try:
#         if isinstance(num1, int) and isinstance(num2, int) and num1 > 0 and num2 > 0:
#             return num1 * num2 
#         elif not isinstance(num1, int) or not isinstance(num2, int):
#             raise TypeError('num must be an integer')
#         else:
#             raise ValueError('num must be positive')
#     except TypeError as e:
#         print(e)
#     except ValueError as e:
#         print(e)

# print(multiply_number('3', 5))
# print(multiply_number(-2, 7))
# print(multiply_number(5, 10))


def divide_numbers(num1, num2):

    try:
        if isinstance(num1, int) and isinstance(num2, int):
            return num1 / num2
        elif num1 == 0 or num2 == 0:
            raise ZeroDivisionError('num cannot be 0')
        else:
            raise TypeError("pull it together please")
    except ZeroDivisionError as e:
        print(e)
    except TypeError as e:
        print(e)

result = divide_numbers('5', 1)
print(result)




