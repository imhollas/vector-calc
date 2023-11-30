# this script does a numerical solution to one of the homework problems,
# maximizing f(x,y) = xy + 1/x + 1/y in the first quadrant (x, y > 0)/

from gradient import grad
from lineintegrals import dot
import random

def norm(u):
    """ Returns the Euclidean norm of the vector u """
    length = dot(u, u)
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
    while norm(current_grad) > 10**(-5):
        scaled_current_grad = []
        # this loop makes scaled_current_grad equal to current_grad scaled 
        # by -0.1 times diffstep
        for i in range(len(initial_pos)):
            scaled_current_grad.append(current_grad[i] * (-0.1) * diffstep)

        # updating the position by stepping one tenth the value of the grad
        for n, x in enumerate(current_position):
            current_position[n] = x + scaled_current_grad[n]

        # updating the value of the gradient
        current_grad = grad(func, diffstep, current_position)
        trial_num += 1

    print(trial_num)
    print(current_grad)
    return current_position

initial_test = [7.3, 2.2]
print(descent(function, initial_test, 0.01))


for i in range(100):
    # these generate random points in the unit disk
    randx = (random.random() - 0.5)*2
    randy = (random.random() - 0.5) * (1 - randx**2)**(0.5)



