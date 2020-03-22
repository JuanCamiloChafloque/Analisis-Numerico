import numpy
import sympy


def f( x ):
    return x * numpy.cos(x)

def fd2( x ):
    return - 2 * numpy.sin(x) - x * numpy.cos(x)

if __name__ == "__main__":
    
    x = 1.8
    M = abs(fd2(x))
    h = [0.1, 0.01, 0.001, 0.0001]
    for i in range(len(h)):
        err = abs(h[i] * M) / 2
        print(err)
    