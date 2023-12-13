import math
import time
from ccquadrature import cc_integrate

def function_3d(x, y, z):
    """ 
        Represents a vector field in three dimensions. Given a point, it
        returns a vector [f_x, f_y, f_z].
    """
    f_x = -y**3
    f_y = x**3
    f_z = 0

    return [f_x, f_y, f_z]


def path(t):
    """
        Dummy path. Gives a point in space (in Cartesian coordinates) given
        the value of its parameter t.
    """
    x = math.cos(t)
    y = math.sin(t)
    z = 0

    return [x, y, z]


def velocity(t, deltat, pathfunc):
    """
       Approximates velocity on the path at point t with step size deltat. 
    """
    diffx = (pathfunc(t+deltat)[0]-pathfunc(t-deltat)[0])/(2*deltat)
    diffy = (pathfunc(t+deltat)[1]-pathfunc(t-deltat)[1])/(2*deltat)
    diffz = (pathfunc(t+deltat)[2]-pathfunc(t-deltat)[2])/(2*deltat)

    # normalizing the velocity vector, so its norm is 1
    length = (diffx**2 + diffy**2 + diffz**2)**0.5
    diffx /= length
    diffy /= length
    diffz /= length

    return [diffx, diffy, diffz]


def dot(v, u):
    """
        Returns the dot product of vectors v and u.
    """
    if len(v) != len(u):
        print("Invalid input to dot product: vectors of different"\
                " dimensions")
    dot_product = 0
    # this loop multiplies the elements at each index of v and u together
    # and sums them
    for i in range(0, len(v)):
        dot_product += v[i]*u[i]

    return dot_product


def line_integral(vecfield, pathfunc, t0, t1, n):
    """
        Computes the line integral of vecfield along pathfunc from t0 to t1
        by dividing into n segments.

        vecfield should be a function of x, y, z returning an array
        [f_x, f_y, f_z]. pathfunc should be a function of a parameter
        representing a path in R^3, so it returns an array [x, y, z] 
        representing a coordinate. t0 and t1 are the bounds of integration
        and n is the number of segments to divide the domain into for
        integrating.
    """
    stepwidth = 0.0001 # step size for approximating derivatives
    # integration
    def integrand(t):
        """
            This generates the function to be integrated by trapezoid_sum
        """
        velocity_vec = velocity(t, stepwidth, pathfunc)
        position = pathfunc(t)

        x_pos = position[0]
        y_pos = position[1]
        z_pos = position[2]
        
        field_at_t = vecfield(x_pos, y_pos, z_pos)

        value = dot(velocity_vec, field_at_t)
        return value
    
    return cc_integrate(t0, t1, n, integrand)

# testing on integrating F(x,y) = [-y^3, x^3] around the unit circle
t0 = time.time()
approximation = line_integral(function_3d, path, 0, 2*math.pi, 20)
t1 = time.time()
true = 3 * math.pi / 2
print("Approximated as {0}".format(approximation))
print("True values is {0}".format(true))
print("Difference is {0}".format(abs(approximation-true)))
print("Time taken was {0}".format(t1 - t0))
