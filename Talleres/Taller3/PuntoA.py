import numpy
import sympy


def f( x ):
    return x * numpy.cos(x)

if __name__ == "__main__":
    
    x = 1.8
    h = [0.1, 0.01, 0.001, 0.0001]
    for i in range(len(h)):
        res = (f(x + h[i]) - f(x)) / f(h[i])
        print(res)
    