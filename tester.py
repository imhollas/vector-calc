import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import math

from trapezoid import trapezoid_sum
from montecarlo import mc_integrate
from ccquadrature import cc_integrate
# convention is that integrating functions take inputs in the form
# (a, b, n, func)

# our test function for integrating is an exponential, we test the
# integral from 0 to 1, which analytically is Euler's number.
def test_func(x):
    return math.exp(x) + 1 


def stdev(array):
    """
        Returns the standard deviation of array, where array is a list of
        floats.
    """
    mean = 0
    for xi in array:
        mean += xi
    mean /= len(array)

    variance = 0
    for xi in array:
        variance += (mean - xi)**2

    variance /= len(array)
    standard_deviation = variance ** 0.5

    return standard_deviation


def error(integrator, n):
    """
        Returns the error of a numerical integration function (integrator)
        when using n iterations/
    """
    numerical_val = integrator(0, 1, n, test_func)
    epsilon = abs(numerical_val - math.e)
    return epsilon


def test(integrator):
    """
        Tests the function integrator from N = 10 to N = 10^5. Graphs results
    """
    errors = []
    list_of_n = []
    for k in range(1, 71):
        n = int(10 ** (0.1 * k))
        errors.append(error(integrator, n) / math.e)
        list_of_n.append(n)
    
    # generating data to plot ideal curve 
    #x = np.linspace(5, 25, 10000)

    plt.xscale("log")
    plt.yscale("log")
    plt.plot(list_of_n, errors, 'ro')
    #plt.plot(x, x**(-0.75))
    plt.xlabel("N, the number of trials")
    plt.ylabel("Fractional error")
    plt.show()

test(mc_integrate)
