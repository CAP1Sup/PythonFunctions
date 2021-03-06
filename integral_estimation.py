from math import *
import argparse

# Function for getting the riemann sum of the area under a curve
def riemann_sum(function, a, b, num_div, est_type):
    """
    str(function), float(a), float(b), int(num_div), bool(right) -> float
    Return the left/right Riemann sum of the given function with num_div divisions,
    from [a, b]
    The function passed in will be eval()'d with x as the current x value.
    """

    # Compile the function so it can be executed
    funcobj = compile(function, "Riemann input formula", "eval")

    # Declare accumulator for the total sum
    rsum = 0

    # Calculate the section width
    div_size = (b - a) / num_div

    # Loop though the sections
    for i in range(0, num_div):

        # Compute the midpoints if specified
        if est_type == "midpts":
            height = evaluate_function(funcobj, a + (i * div_size) + div_size/2)
            rsum += height * div_size

        # Otherwise, compute the regular amounts
        else:

            # Evaluate lower and upper section bounds
            left_val = evaluate_function(funcobj, a + (i * div_size))
            right_val = evaluate_function(funcobj, a + ((i + 1) * div_size))

            # If we're looking at upper, we want the highest value
            if est_type.lower() == "upper":
                if (left_val > right_val):
                    rsum += left_val * div_size
                else:
                    rsum += right_val * div_size

            # If we're looking at lower, we want the lowest value
            elif est_type.lower() == "lower":
                if (left_val < right_val):
                    rsum += left_val * div_size
                else:
                    rsum += right_val * div_size

            # Left side only
            elif est_type.lower() == "left":
                rsum += left_val * div_size

            # Right side only
            elif est_type.lower() == "right":
                rsum += right_val * div_size

            # Throw an error if there's no type found
            else:
                raise ValueError("Invalid estimation type!")

    # Return the result, nicely rounded
    return round(rsum, 4)


# Trapezoidal sum
def trapezoidal_sum(function, a, b, num_sectors):

    # Compile the function so it can be executed
    funcobj = compile(function, "Trapezoidal input formula", "eval")

    # Create an accumulator for the function sum
    function_sum = 0.0

    # Calculate the section size
    div_size = (b - a) / num_sectors

    # Calculate the sum of the y values
    for index in range(0, num_sectors + 1):

        # Add the next function values to the sum
        function_sum += 2 * evaluate_function(funcobj, a + (div_size * index))

    # Remove a single instance of the first and last function values (not needed)
    function_sum -= (evaluate_function(funcobj, a) + evaluate_function(funcobj, b))

    # Multiply by the division size / 2 to get the area under the curve
    area = (div_size / 2) * function_sum

    # Return the resulting area (rounded)
    return round(area, 4)


# Quick and easy way of evaluating a function at a point
def evaluate_function(function_object, x):
    return eval(function_object)


# Main function gets run if this is the only file running
if __name__ == "__main__":

    # Create an instance of the parser
    parser = argparse.ArgumentParser()

    # Add the type argument
    parser.add_argument('-t', '--type', help='The type of estimation. Can be "Riemann" or "Trapezoid"')

    # Parse the args from the command line
    args = parser.parse_args()

    # Riemann sum
    if (args.type == "Riemann"):

        # Print to give the user some info
        print("Riemann sum calculator")
        print("Enter a valid Python expression to evaluate")
        print("Use x for the independent variable")
        print("Expression should be in Python format. (ex equation y = x^2 + 2x + 3 should be entered as 'x**2 + 2*x + 3')")

        # Ask for each of the parameters
        function = input("Expression: ")
        a = compile(input("a: "), "a", "eval")
        b = compile(input("b: "), "b", "eval")
        num_div = int(input("Subintervals: "))

        # Calculate and print the values
        print("Upper: " + str(riemann_sum(function, eval(a), eval(b), num_div, "upper")))
        print("Lower: " + str(riemann_sum(function, eval(a), eval(b), num_div, "lower")))
        print("Midpts: "+ str(riemann_sum(function, eval(a), eval(b), num_div, "midpts")))
        print("Left: "+ str(riemann_sum(function, eval(a), eval(b), num_div, "left")))
        print("Right: "+ str(riemann_sum(function, eval(a), eval(b), num_div, "right")))

    else:
        # Trapezoid area estimation

        # Print to give the user some info
        print("Trapezoid integral estimator")
        print("Enter a valid Python expression to evaluate")
        print("Use x for the independent variable")
        print("Expression should be in Python format. (ex equation y = x^2 + 2x + 3 should be entered as 'x**2 + 2*x + 3')")

        # Ask for each of the parameters
        function = input("Expression: ")
        a = compile(input("a: "), "a", "eval")
        b = compile(input("b: "), "b", "eval")
        num_div = int(input("Subintervals: "))

        # Calculate and print the values
        print("Trapezoidal Sum: " + str(trapezoidal_sum(function, eval(a), eval(b), num_div)))