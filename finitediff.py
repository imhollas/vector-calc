import math
import matplotlib.pyplot as plt
import numpy as np
# the idea in finite_diff is implemented elsewhere. the purpose of this 
# script is to test how the error decreases with step/

def finite_diff(func, x0, step):
    """ 
        Approximates the derivative of func at x0 using a centered 
        difference and a step size of step.
    """
    approximation = (func(x0 + step) - func(x0 - step))/(2 * step)
    return approximation


def error(step):
    """ Returns the fractional error in finite diff """
    numerical_val = finite_diff(math.exp, 1, step)
    epsilon = abs(math.e - numerical_val)
    return epsilon

errors = []
step_sizes = []
for n in range(1, 131):
    deltax = 10**(-0.1 * n)
    errors.append(error(deltax) / math.e)
    step_sizes.append(deltax)


plt.xscale("log")
plt.yscale("log")
plt.plot(step_sizes, errors, 'ro')
plt.xlabel("Step size")
plt.ylabel("Fractional error")
plt.show()
