import math

# basic method of integration:
# partition the domain into subintervals
# for each subinterval, take the value of the function at each endpoint,
# multiply by the width of the interval, sum, and divide by 2 (we're
# averaging the left and right end point sums)

def function(x):
    """ Dummy function for testing """
    return x**2

def partition_i(a, b, deltax), i:
    """ Returns the endpoints of the ith subinterval of [a,b] """
    n = math.floor((b-a)/deltax)
    if i > n+1:
        print("Error, requested endpoint outside of interval")
        exit()
    if i = n:
        left_endpoint = n * deltax
        right_endpoint = b
        return [left_endpoint, right_endpoint]
    else:
        left_endpoint = i * deltax
        right_endpoint = (i + 1) * deltax
        return [left_endpoint, right_endpoint]


def left_sum(a, b):
    """ 
        Approximates the integral by multiplying the function at left
        endpoints by the partition width
    """


#class ThreeDimFunction:
#    """ A function in x, y, z """
#    def __init__(self, fx=0, fy=0, fz=0):
#        """ Creates a new function with components 
#        self.fx = 
