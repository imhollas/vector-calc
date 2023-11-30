def function(position):
    """
        Real-valued function from R^n to R. position s a list of length n
    """
    value = 0
    # this function returns the distance from origin squared
    for x in position:
        value += x**2

    return value


def grad(func, step, position):
    """
        Returns a numerical approximation of the gradient of a function 
        (func) at position (a list of length n, where n is the dimension of
        the space we are working in).
    """
    partials = []
    for i, val in enumerate(position):
        step_forward = [] 
        for element in position:
            step_forward.append(element)
        step_forward[i] += step

        step_backward = []
        for element in position:
            step_backward.append(element)
        step_backward[i] -= step

        diff_i = (func(step_forward)-func(step_backward))/(2 * step)
        partials.append(diff_i)

    return partials

