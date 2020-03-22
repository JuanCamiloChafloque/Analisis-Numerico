import numpy
import sympy

def f( x ):
    return x * numpy.cos(x)

def fd( x ):
    return numpy.cos(x) - x * numpy.sin(x)

if __name__ == "__main__":
    
    x = 1.8
    ex = fd( x )
    max = 100
    h_ini = 0.1
    tol = 10e-4
    
    for i in range(max):
        res = (f(x + h_ini) - f(x)) / (f(h_ini))
        if abs(round(res, 4) - round(ex, 4)) < tol:
            print("El valor de h para garantizar un error menor a 10e-4 es: ", h_ini)
            break
        h_ini = h_ini / 10

    