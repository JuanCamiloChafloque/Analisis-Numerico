library(pracma)
library(PolynomF)

funcCorriente <- function(x){
    return (-83333.33 * x^4 + 341666.7 * x^3 - 525191.7 * x^2 + 358719.9 * x - 91858.4)
    #return (-4 * 83333.33 * x^3 + 3 * 341666.7 * x^2 - 2 * 525191.7 * x + 358719.9)
}

x <- c(1, 1.01, 1.02, 1.03, 1.04)
y <- c(3.1, 3.12, 3.14, 3.18, 3.24)
h <- 0.01
R <- 0.142
L <- 0.98

pol <- poly_calc(x, y)
plot(x, y, pch=19, cex=0.8, col = "red", xlab="t", ylab="I(t)", main="Corriente vs. Tiempo")
curve(pol, add="T")


i1 <- (funcCorriente(1    + h) - funcCorriente(1))    / h
i2 <- (funcCorriente(1.01 + h) - funcCorriente(1.01)) / h
i3 <- (funcCorriente(1.02 + h) - funcCorriente(1.02)) / h
i4 <- (funcCorriente(1.03 + h) - funcCorriente(1.03)) / h
i5 <- (funcCorriente(1.04 + h) - funcCorriente(1.04)) / h

E1 <- L * i1 + R * y[1]
E2 <- L * i2 + R * y[2]
E3 <- L * i3 + R * y[3]
E4 <- L * i4 + R * y[4]
E5 <- L * i5 + R * y[5]