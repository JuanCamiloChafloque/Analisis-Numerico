import numpy
import sympy

def f( x ):
    return x * numpy.cos(x)

def fd( x ):
    return numpy.cos(x) - x * numpy.sin(x)

if __name__ == "__main__":
    
    x = 1.8
    h = 0.001
    ex = fd(x)
    
    res = (f(x + h) - f(x - h)) / (2*h)
    print(res)
    
    err = abs(ex - res)
    print("El error es de: ", err)