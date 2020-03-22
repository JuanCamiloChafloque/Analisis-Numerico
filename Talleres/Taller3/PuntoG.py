import numpy
import sympy

def f( x ):
    return x * numpy.cos(x)

def fd( x ):
    return numpy.cos(x) - x * numpy.sin(x)

def fd2( x ):
    return - 2 * numpy.sin(x) - x * numpy.cos(x)

if __name__ == "__main__":
    
    x = 1.8
    h = 0.001 
    ex = fd2(x)
    
    res = (f(x + h) - 2 * f(x) + f(x - h)) / (h**2)
    print(res)
    
    err = abs(ex - res)
    print("El error es: ", err)