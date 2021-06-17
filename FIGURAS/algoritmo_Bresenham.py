import matplotlib.pylab as plt


def cuadrilatero_Bresenham(arregloX, arregloY):
    j = 0
    lados = 4
    # Ciclo para determinar los puntos de inicio y final del trazo de cada linea
    while j < lados:
        # If que evalua si es el ultimo lado a pintar
        if j == (lados - 1):
            x1 = arregloX[j]
            y1 = arregloY[j]
            x2 = arregloX[0]
            y2 = arregloY[0]
        else:
            x1 = arregloX[j]
            y1 = arregloY[j]
            x2 = arregloX[j + 1]
            y2 = arregloY[j + 1]
        dx = abs(x2 - x1)
        print("dx= ", dx)
        dy = abs(y2 - y1)
        print("dy= ", dy)
        p = 2 * dy - dx
        print("p ", p)
        if x1 > x2:
            x_1 = x2
            y_1 = y2
            x_2 = x1
            y_2 = y1
        else:
            x_1 = x1
            y_1 = y1
            x_2 = x2
            y_2 = y2
        if dx == 0:
            if y_1 < y_2:
                aux = y_1
                y_1 = y_2
                y_2 = aux
            while y_1 >= y_2:
                plt.plot(x_1, y_1, "bs")
                if p < 0:
                    p = p + 2 * dy
                else:
                    p = p + 2 * dy - 2 * dx
                    y_1 -= 1
        else:
            while x_1 <= x_2:
                plt.plot(x_1, y_1, "bs")
                x_1 += 1
                if p < 0:
                    p = p + 2 * dy
                else:
                    p = p + 2 * dy - 2 * dx
                    y_1 += 1
        j += 1
    plt.title("FIGURA EN BRESENHAM")
    plt.show()


def triangulo_Bresenham(arregloX, arregloY):
    j = 0
    lados = 3
    # Ciclo para determinar los puntos de inicio y final del trazo de cada linea
    while j < lados:
        # If que evalua si es el ultimo lado a pintar
        if j == (lados - 1):
            x1 = arregloX[j]
            y1 = arregloY[j]
            x2 = arregloX[0]
            y2 = arregloY[0]
        else:
            x1 = arregloX[j]
            y1 = arregloY[j]
            x2 = arregloX[j + 1]
            y2 = arregloY[j + 1]
        dx = abs(x2 - x1)
        print("dx= ", dx)
        dy = abs(y2 - y1)
        print("dy= ", dy)
        p = 2 * dy - dx
        print("p ", p)
        if x1 > x2:
            x_1 = x2
            y_1 = y2
            x_2 = x1
            y_2 = y1
        else:
            x_1 = x1
            y_1 = y1
            x_2 = x2
            y_2 = y2
        if dx == 0:
            if y_1 < y_2:
                aux = y_1
                y_1 = y_2
                y_2 = aux
            while y_1 >= y_2:
                plt.plot(x_1, y_1, "bs")
                if p < 0:
                    p = p + 2 * dy
                else:
                    p = p + 2 * dy - 2 * dx
                    y_1 -= 1
        else:
            while x_1 <= x_2:
                plt.plot(x_1, y_1, "bs")
                x_1 += 1
                if p < 0:
                    p = p + 2 * dy
                else:
                    p = p + 2 * dy - 2 * dx
                    y_1 += 1
        j += 1
    plt.title("TRIANGULO EN BRESENHAM")
    plt.show()