import math

def function(x):
    return math.exp(x)

def cc_integrate(a, b, N, func):
    """
        Integrates func from a to b using Clenshaw-Curtis quadrature and
        N points. func should be a function that receives a float and 
        returns a float. a, b, and N are floats. Assumes b > a.
    """
    def changed_func(x):
        """
            This is a modified version of func such that integrating
            changed_func from -1 to 1 equals func integrated from a to b.
        """
        modified_input = 0.5 * ((b - a) * x + b + a)
        modified_output = func(modified_input)

        result = modified_output * (b - a) / 2

        return result

    # we store the value of changed_func at a set list of points, since we
    # will need each of those values N times
    f_points = []
    for n in range(N+1):
        x = math.cos(n * math.pi / N)
        fn = changed_func(x)
        f_points.append(fn)

    # coeffs is a list of the Fourier coefficient a_2k: a_0, a_2, ... a_N
    coeffs = [] 
    for k in range(0, N+1, 2):
        coeff_2k = (f_points[0] + f_points[N]) / 2
        for i in range(1, N):
            term = f_points[i] * math.cos(k * i * math.pi / N)
            coeff_2k += term

        coeff_2k *= 2 / N
        coeffs.append(coeff_2k)

    integral = coeffs[0]
    for k, a_k in enumerate(coeffs):
        if k != 0:
            series_term = 2 * a_k / (1 - (2 * k)**2) 
            integral += series_term

    return integral
