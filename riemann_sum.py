from math import *

# Function for getting the riemann sum of the area under a curve
def riemann_sum(function, a, b, num_div, upper = True, midpoints = False):
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
        if midpoints:
            x = a + (i * div_size) + div_size/2
            height = eval(funcobj)
            rsum += height * div_size

        # Otherwise, compute the regular amounts
        else:

            # Evaluate lower section bound
            x = a + (i * div_size)
            lower_val = eval(funcobj)

            # Evaluate upper section bound
            x = a + ((i + 1) * div_size)
            upper_val = eval(funcobj)

            # If we're looking at upper, we want the highest value
            if upper:
                if (lower_val > upper_val):
                    rsum += lower_val * div_size
                else:
                    rsum += upper_val * div_size

            # If we're looking at lower, we want the lowest value
            else:
                if (lower_val < upper_val):
                    rsum += lower_val * div_size
                else:
                    rsum += upper_val * div_size

    # Return the result, nicely rounded
    return round(rsum, 4)


# Main function
def main():

    # Print to give the user some info
    print("Riemann sum calculator")
    print("Enter a valid Python expression to evaluate")
    print("Use x for the independent variable")

    # Ask for each of the parameters
    function = input("Expression: ")
    a = float(input("a: "))
    b = float(input("b: "))
    num_div = int(input("n: "))

    # Calculate and print the values
    print("Upper: " + str(riemann_sum(function, a, b, num_div, upper = True)))
    print("Lower: " + str(riemann_sum(function, a, b, num_div, upper = False)))
    print("Midpts: "+ str(riemann_sum(function, a, b, num_div, midpoints = True)))


# Main function gets run if this is the only file running
if __name__ == "__main__":
    main()