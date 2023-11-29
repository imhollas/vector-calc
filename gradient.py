def function(x, y, z):
    """
        Real-valued function of x, y, and z
    """
    value = x**2 + y**2 + z**2
    return value


def partial(func, direction, step, x, y, z):
    """
        Approximates the partial derivative of a function (func )in 
        specified direction. Direction should be string: 'x', 'y', or 'z'.
        Step size is step.
    """
    if direction == 'x':
        diff = (func(x+step, y, z)-func(x-step, y, z))/(2 * step)
        return diff
    if direction == 'y':
        diff = (func(x, y+step, z)-func(x, y-step, z))/(2 * step)
        return diff
    if direction == 'z':
        diff = (func(x, y, z+step)-func(x, y, z-step))/(2 * step)
        return diff
    else:
        print("Error: invalid partial derivative direction.")


def grad(func, step, x, y, z):
    """
        Returns the gradient of a function (func)
    """

    partialx = partial(func, 'x', step, x, y, z)
    partialy = partial(func, 'y', step, x, y, z)
    partialz = partial(func, 'z', step, x, y, z)

    return [partialx, partialy, partialz]
