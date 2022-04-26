'''Assignment 0

This assignment is a giveaway assignment.
By completing this assignment, you will familiarize yourself with this
    course's submission mechanics.
'''

def three_number_average(x, y, z):
    '''Item 1.
    Three Number Average. 3 points.

    Returns the average of three numbers.

    Parameters
    ----------
    x: int
        the first number
    y: int
        the second number 
    z: int
        the third number

    Returns
    -------
    float
        the average of x, y, and z
    '''
    # Write your code below this line
x = int (input(" Enter the First Number: "))

y = int (input(" Enter the second number: "))

z = int (input(" Enter the third number: "))

average=(x+y+z)/3

print("The average of the three numbers is ", average)
