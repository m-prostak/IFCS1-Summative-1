import random


def generate_equation(max_number):
    """
    Generate and return random equation in the format:
    [NUMBER] [OPERATOR] x =[NUMBER].

    Returns a tuple with the equation as a string (for display purposes)
    and a list (for solving).
    """
    operators = ['+', '-', '*', '/']
    # Get random numbers and random operator from operators list to be
    # used in the equation
    random_number_1 = random.randint(1, max_number)
    random_number_2 = random.randint(1, max_number)
    random_operator = random.choice(operators)
    # Create an equation array with the random values, for use when
    # solving the equation
    equation_arr = [
        random_number_1,
        random_operator,
        'x',
        '=',
        random_number_2
    ]
    # Join the array into a string for use when printing the equation
    equation = ' '.join(map(str, equation_arr))
    return equation, equation_arr


def solve_equation(equation_arr):
    """
    Solves the parsed equation represented by a list.

    Returns the value of 'x' rounded to 2 decimal places.
    """
    # Get values from both sides of the equation
    right_value = int(equation_arr[4])
    left_value = int(equation_arr[0])
    # Get operator from the equation
    operator = equation_arr[1]
    # Solve for 'x' based on the operator
    if operator == '+':
        x = right_value - left_value
    elif operator == '-':
        x = left_value - right_value
    elif operator == '*':
        x = right_value / left_value
    elif operator == '/':
        x = left_value / right_value
    # Round the answer to 2 decimal places
    x = round(x, 2)
    return x
