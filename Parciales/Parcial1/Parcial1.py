from matplotlib import pyplot
import numpy
#----------------------------------------Parcial 1. Analisis Numerico
#----------------------------------------Juan Camilo Chafloque

def f(x):
    return numpy.log(x + 2)

def g(x):
    return numpy.sin(x)

def h(x):
    return f(x) - g(x)

#--------------------------------Punto 2.a
def algoritmoPuntoA( tol ):
    
    it = 0
    x0 = -1.8
    x1 = -1.7
    errorX = []
    errorY = []
    
    while abs( x1 - x0 ) / abs(x0) > tol:
        
        if it > 1:
            errorY.append( abs( x1 - x0 ) / abs(x0) )
        it = it + 1
        x2 = x1 - ((h(x1) * (x1 - x0)) / (h(x1) - h(x0)))
        x0 = x1
        x1 = x2
        
        errorX.append( abs( x1 - x0 ) / abs(x0) )
        
    print("La aproximacion con el primer algoritmo de la raiz es: ", x2)
    print("El numero de iteraciones hechas fueron: ", it)
    
    x = numpy.linspace( errorX[0], errorX[len(errorX) - 1], 50 )
    y = numpy.linspace( errorY[0], errorY[len(errorY) - 1], 50 )
    pyplot.plot( x, y )
    pyplot.xlabel("Errores X ")
    pyplot.ylabel("Errores Y ")
    pyplot.title("Algoritmo Punto A: \n Errores en X vs. Errores en Y")
    pyplot.grid()
    pyplot.show()
    
#--------------------------------Punto 2.c
def algoritmoPuntoC( tol ):
    
    it = 0
    x0 = -1.8
    x1 = -1.7
    errorX = []
    errorY = []

    while abs( x1 - x0 ) / abs(x0) > tol:
        
        if it > 1:
            errorY.append( abs( x1 - x0 ) / abs(x0) )
        
        it = it + 1
        x2 = x1 - (h(x1) * ((x1 - x0) / (h(x1) - h(x0))))
        x0 = x1
        x1 = x2
        
        errorX.append( abs( x1 - x0 ) / abs(x0) )
        
    print("La aproximacion de la raiz con el segundo algoritmo es: ", x2)
    print("El numero de iteraciones hechas fueron: ", it)

    x = numpy.linspace( errorX[0], errorX[len(errorX) - 1], 50 )
    y = numpy.linspace( errorY[0], errorY[len(errorY) - 1], 50 )
    pyplot.plot( x, y )
    pyplot.xlabel("Errores X ")
    pyplot.ylabel("Errores Y ")
    pyplot.title("Algoritmo Punto C: \n Errores en X vs. Errores en Y")
    pyplot.grid()
    pyplot.show()

if __name__ == "__main__":
    
    x = numpy.linspace( -5, 5, 50 )
    pyplot.plot( x, f(x), label='f(x) = ln(x + 2)' )
    pyplot.plot( x, g(x), label='g(x) = sin(x)' )
    pyplot.legend(prop = {'size':10}, loc = 'lower right')
    pyplot.xlabel("Valores X")
    pyplot.ylabel("Valores Y")
    pyplot.title("Interseccion f(x) y g(x)")
    pyplot.grid()
    pyplot.show()
    
    algoritmoPuntoA( 10e-8 )
    algoritmoPuntoC( 10e-8 )


