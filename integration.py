import math

# basic method of integration:
# divide domain into n subintervals
# multiply the width of each subinterval (deltax) by the average value of
# the function on the subinterval
# this is equivalent to the trapezoid rule

def function(x):
    """ Dummy function for testing """
    return x**2

def trapezoid_sum(a, b, n, func):
    """ 
        Integrates func from a to b via trapezoid sum with n slices 
    """
    deltax = (b-a)/n
    integral = 0
    for i in range(0, n):
        trapezoid_i = \
                (func(a + i*deltax)+func(a + (i+1)*deltax))*deltax/2
        integral += trapezoid_i
        
    return integral
