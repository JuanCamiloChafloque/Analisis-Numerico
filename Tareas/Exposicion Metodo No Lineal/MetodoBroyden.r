#Metodo de Boyden

library(pracma)
library(Matrix)

F1 <- function(x) {
    x1 <- x[1]; x2 <- x[2]; x3 <- x[3]
    as.matrix(c(x1^2 + x2^2 + x3^2 - 1,
                x1^2 + x3^2 - 0.25,
                x1^2 + x2^2 - 4*x3), ncol = 1)
}

F2 <- function(x) {
    x1 <- x[1]; x2 <- x[2]
    as.matrix(c(4*x1^2 - 20*x1 + 0.25*x2^2 + 8,
                0.5*x1*x2^2 + 2*x1 - 5*x2 + 8), ncol = 1)
}

x0_0 <- as.matrix(c(1, 1, 1))
x0_1 <- as.matrix(c(0, 0))
sol <- broyden(F1, x0_0)
cat("Los ceros del sistema no lineal son: ", sol$zero, " con un numero de ", sol$niter, " iteraciones")
