# Written by: Christian Piper
# Computes the points of a robot arm with the angles and length of sections between joints

# Import libraries
import math

def main():

    # Get the inputs for the lengths
    length_a = input("Enter the length of the first section (between the base and first joint): ")
    length_b = input("Enter the length of the second section (between the first joint and end point): ")

    # Get the angles for the joints
    base_angle = input("Enter the base angle (angle between the first section and the horizontal): ")
    first_joint_angle = input("Enter the first joint's angle (angle between the second section and the horizontal): ")

    # Try to convert each of the inputs to numbers
    try:
        length_a = float(length_a)
        length_b = float(length_b)
        base_angle = float(base_angle)
        first_joint_angle = float(first_joint_angle)
    except:
        print("One of the values you entered was not a number. Make sure you don't include units in your inputs")
        return 0

    # Calculate the X and Y of the sections (end point is relative to the first joint)
    first_joint = [round(math.cos(math.radians(base_angle)) * length_a, 4), round(math.sin(math.radians(base_angle)) * length_a, 4)]
    end_point = [round(math.cos(math.radians(first_joint_angle)) * length_b, 4), round(math.sin(math.radians(first_joint_angle)) * length_b, 4)]

    # Calculate the total transformation of the end point
    total_transform = [round(first_joint[0] + end_point[0], 4), round(first_joint[1] + end_point[1], 4)]

    # Print out the results of all of the math that was just done
    print("First joint position (relative to base joint): " + str(first_joint))
    print("End point position (relative to first joint): " + str(end_point))
    print("End point position (relative to the base joint): " + str(total_transform))


main()