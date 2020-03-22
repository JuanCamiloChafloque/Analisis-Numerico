#Encontrar en que instante dos coordenadas seran iguales en el intervalo [0, PI/2]

from matplotlib import pyplot
import numpy

def x( t ):
    return 3 * numpy.sin(t)**3 - 1

def y( t ):
    return 4 * numpy.sin(t) * numpy.cos(t)

def h( t ):
    return (3 * numpy.sin(t)**3 - 1) - (4 * numpy.sin(t) * numpy.cos(t))

def hd( t ):
    return 9 * numpy.sin(t)**2 * numpy.cos(t) - 4 * numpy.cos(2*t)

def interseccion( a, b ):
    
    c = (a + b) / 2
    it = 0
    error = []
    tol = 10e-8
    
    
    while abs( b - a ) > tol:
        
        c = ( a + b ) / 2
        fa = h( a )
        fc = h( c )
        error.append(abs( b - a ))
        if fc == 0:
            raiz = c
            break
        elif fa * fc < 0:
            b = c
        else:
            a = c
        raiz = c
        
        it = it + 1
        
    print("La aproximacion de la raiz de la funcion es: ", raiz )
    print("La cantidad de iteraciones que se tuvieron fueron: ", it )
    
def newton( a, b ):
    
    x = (a + b) / 2
    it = 0
    tol = 10e-8
    errorX = []
    errorY = []
    
    raiz = x - ( h(x) / hd(x) ) 

    while abs( raiz - x ) > tol:
        if it > 0:
            errorX.append( abs( raiz - x ) )
        it = it + 1
        x = raiz
        raiz = x - ( h(x) / hd(x) ) 
        if it > 1:
            errorY.append( abs( raiz - x ) )
    
    print("La raiz es aproximadamente: ", raiz )
    print("El numero de iteraciones que se obtuvieron: ", it )
    
if __name__ == "__main__":
    interseccion( 0, numpy.pi/2 )
    newton(0, numpy.pi/2 )
    
    t = numpy.linspace( 0, numpy.pi/2, 2000 )
    fig = pyplot.figure()
    f = fig.add_subplot(111, projection="polar")
    f.plot(t, x(t), label='x(t) = 3sin(t)^3 - 1' )
    f.plot(t, y(t), label='y(t) = 4sin(t)cos(t)' )
    pyplot.title("Coordenadas polares de las funciones X e Y ")
    pyplot.legend(prop = {'size':10}, loc = 'lower right')
    pyplot.show()
    
