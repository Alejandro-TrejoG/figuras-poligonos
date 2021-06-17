import matplotlib.pylab as p


def cuadrilatero_DDA(x1, y1, lado):
    arregloX = [x1, x1 + lado, x1 + lado, x1]
    arregloY = [y1, y1, y1 + lado, y1 + lado]
    lados = 4
    j = 0
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
        dx = x2 - x1
        dy = y2 - y1
        if abs(dx) > abs(dy):
            steps = abs(dx)
            print("steps = dx = ", dx)
        else:
            steps = abs(dy)
            print("steps = dy = ", dy)

        xinc = float(dx / steps)
        yinc = float(dy / steps)

        i = 0
        for i in range(steps + 1):
            p.plot(round(x1), round(y1), "bs")
            x1 += xinc
            y1 += yinc

            print("x => ", round(x1))
            print("y => ", round(y1))
        j += 1
    p.title("RECTANGULO EN DDA")
    p.show()


def rectangulo_DDA(arregloX, arregloY):
    lados = 4
    j = 0
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
        dx = x2 - x1
        dy = y2 - y1
        if abs(dx) > abs(dy):
            steps = abs(dx)
            print("steps = dx = ", dx)
        else:
            steps = abs(dy)
            print("steps = dy = ", dy)

        xinc = float(dx / steps)
        yinc = float(dy / steps)

        i = 0
        for i in range(steps + 1):
            p.plot(round(x1), round(y1), "bs")
            x1 += xinc
            y1 += yinc

            print("x => ", round(x1))
            print("y => ", round(y1))
        j += 1
    p.title("RECTANGULO EN DDA")
    p.show()


def triangulo_DDA(arregloX, arregloY):
    lados = 3
    j = 0
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
        dx = x2 - x1
        dy = y2 - y1
        if abs(dx) > abs(dy):
            steps = abs(dx)
            print("steps = dx = ", dx)
        else:
            steps = abs(dy)
            print("steps = dy = ", dy)

        xinc = float(dx / steps)
        yinc = float(dy / steps)

        i = 0
        for i in range(steps + 1):
            p.plot(round(x1), round(y1), "bs")
            x1 += xinc
            y1 += yinc

            print("x => ", round(x1))
            print("y => ", round(y1))
        j += 1
    p.title("TRIANGULO EN DDA")
    p.show()