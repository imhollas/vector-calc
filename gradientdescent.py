# this script does a numerical solution to one of the homework problems,
# maximizing f(x,y) = xy + 1/x + 1/y in the first quadrant (x, y > 0)/

from gradient import grad
from lineintegrals import dot
import random

def average(array):
    """ 
        array is a list containing floats. Returns the mean of the elements 
        of the array 
    """
    avg = 0
    for i in array:
        avg += i

    avg /= len(array)
    return avg


def stdev(array):
    """
        array is a list containing floats. Returns the standard deviation
        of the elements of the array.
    """
    mean = average(array)
    variance = 0
    for xi in array:
       variance += (mean - xi)**2

    
    variance /= len(array)
    standard_deviation = variance ** 0.5

    return standard_deviation


def norm(u):
    """ Returns the Euclidean norm of the vector u """
    length = (dot(u, u))**0.5
    return length


def function(position):
    """ position is list of length 3 """
    x = position[0]
    y = position[1]

    value = x*y + x**(-1) + y**(-1)
    return value


def descent(func, initial_pos, diffstep):
    """
        func is function being optimized, initial_pos is a list representin 
        initial position. diffstep is the step size for approximating the
        gradient.
    """
    current_position = initial_pos
    current_grad = grad(func, diffstep, initial_pos)

    trial_num = 0
    diffstepscaling = -1.0
    while norm(current_grad) > 10**(-5) and trial_num < 10**7:
        scaled_current_grad = []
        # this loop makes scaled_current_grad equal to current_grad scaled 
        # by -0.1 times diffstep
        for i in range(len(initial_pos)):
            scaled_current_grad.append(current_grad[i] * diffstepscaling * diffstep)

        # updating the position by stepping one tenth the value of the grad
        for n, x in enumerate(current_position):
            current_position[n] = x + scaled_current_grad[n]

        # updating the value of the gradient
        current_grad = grad(func, diffstep, current_position)
        trial_num += 1

    return [current_position, trial_num]


# code for testing the function, specifically how many steps it takes
num_steps_list = []
for i in range(1000):
    rand_x = 100 * random.random()
    rand_y = 100 * random.random()
    rand_pos = [rand_x, rand_y]

    result = descent(function, rand_pos, 0.01)
    num_steps = result[1]
    position = result[0]
    
    dist_to_true = ((1-position[0])**2 + (1-position[1])**2)**0.5
    
    # the if statement verifies that we ended in the domain
    # the trial is ignored if this did not happen
    if (0 < position[0] and position[0] < 100) and \
            (0 < position[1] and position[1] < 100) \
            and num_steps != 10**7:
        print("Converged on trial {0}".format(i))
        print("Location was x = {0}, y = {1}".format(position[0], \
                position[1]))

        num_steps_list.append(num_steps)


print(average(num_steps_list))
print(stdev(num_steps_list))
print(num_steps_list)
print(len(num_steps_list)) # this is the number of times it converged
