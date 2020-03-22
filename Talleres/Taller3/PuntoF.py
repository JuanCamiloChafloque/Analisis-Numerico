import numpy
import sympy

def f( x ):
    return x * numpy.cos(x)

def fd( x ):
    return numpy.cos(x) - x * numpy.sin(x)


if __name__ == "__main__":
    
    x = 1.8
    h = 0.001
    x1 = x - (2 * h)
    x2 = x - h
    x3 = x + h
    x4 = x + (2 * h)
    
    ex = fd(x)
    
    res = (-f(x4) + 8 * f(x3) - 8 * f(x2) + f(x1)) / (12 * h)
    print(res)
    
    err = abs(ex - res)
    print("El error con el metodo de los 5 puntos es: ", err)
    