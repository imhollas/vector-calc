import math

# basic method of integration:
# divide domain into n subintervals
# multiply the width of each subinterval (deltax) by the average value of
# the function on the subinterval
# this is equivalent to the trapezoid rule

def function(x):
    """ Dummy function for testing """
    return 1 + math.exp(x)

def trapezoid_sum(a, b, n, func):
    """ 
        Integrates func from a to b via trapezoid sum with n slices 
    """
    deltax = (b-a)/n
    integral = (func(a)+func(b))*deltax/2
    for i in range(1, n):
        integral += deltax * func(a + i*deltax)
        
    return integral


