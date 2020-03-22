import numpy
import sympy

#x0
#x1 = x0 + h
#x2 = x0 + 2h

#fd = -(f(x0 + 2h) + 4 * f(x0 + h) - 3*f(x0)) / 2h


def f( x ):
    return x * numpy.cos(x)

if __name__ == "__main__":
    
    x = 1.8
    h = 0.001
    
    res = (-f(x + 2 * h) + 4 * f(x + h) - 3 * f(x)) / (2 * h)
    print(res)
    