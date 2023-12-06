from random import random

def function(x):
    """ Dummy function, takes float and returns float """
    return x**2

def mc_integrate(a, b, n, func):
    """ 
        Integrates func from a to b using Monte Carlo with n samples.
        func is function taking float and returning float. a and b are 
        floats representing the bounds of integration. n is the number of 
        trials
    """
    range_width = b-a
    total = 0
    for i in range(n):
        sample = random()

        sample_scaled = (b - a)*sample + a

        total += func(sample_scaled)

    average = total / n

    integral = average * range_width
    return integral
