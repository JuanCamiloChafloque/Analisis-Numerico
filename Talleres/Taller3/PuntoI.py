import numpy as np
from matplotlib import pyplot

def f( x ):
    return x * np.exp(x)

if __name__ == "__main__":
    
    x = 1
    h = 0.1
    r = 5.436563656918091
    vx = []
    vy = []
    
    for i in range(15):
        d = (f(x + h) - f(x)) / h
        vx.append( h )
        vy.append( abs(r - d) ) 
        h = h / 10


    cx = np.linspace( vx[0], vx[len(vx) - 1], 50 )
    cy = np.linspace( vy[0], vy[len(vy) - 1], 50 )
    pyplot.plot( cx, cy )
    pyplot.xlabel("h ")
    pyplot.ylabel("Precision ")
    pyplot.title("Derivada de f(x) = x * e^x")
    pyplot.grid()
    pyplot.show()    
