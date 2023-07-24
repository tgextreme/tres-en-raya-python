
import numpy as np
from pprint import pp


def crearTabla():
    tabla = [["-"]*3]*3
    tabla = np.array(tabla)
    return tabla


def imprimirTabla(tabla):

    for x in range(3):
        linea = "|"
        for y in range(3):
            linea = linea+str(tabla[x][y])+"|"
        print(linea)


def checkGanador(tabla, caracter):
    if(tabla[0][0] == caracter and tabla[0][1] == caracter and tabla[0][2] == caracter):
        return False
    if(tabla[1][0] == caracter and tabla[1][1] == caracter and tabla[1][2] == caracter):
        return False
    if(tabla[2][0] == caracter and tabla[2][1] == caracter and tabla[2][2] == caracter):
        return False

    if(tabla[0][0] == caracter and tabla[0][1] == caracter and tabla[0][2] == caracter):
        return False
    if(tabla[1][0] == caracter and tabla[1][1] == caracter and tabla[1][2] == caracter):
        return False
    if(tabla[2][0] == caracter and tabla[2][1] == caracter and tabla[2][2] == caracter):
        return False

    if(tabla[0][0] == caracter and tabla[1][0] == caracter and tabla[2][0] == caracter):
        return False
    if(tabla[0][1] == caracter and tabla[1][1] == caracter and tabla[2][1] == caracter):
        return False
    if(tabla[0][2] == caracter and tabla[2][1] == caracter and tabla[2][2] == caracter):
        return False

    if(tabla[0][0] == caracter and tabla[1][1] == caracter and tabla[2][2] == caracter):
        return False
    if(tabla[2][0] == caracter and tabla[1][1] == caracter and tabla[0][2] == caracter):
        return False
    return True


def pedirFicha(tabla, caracter):
    columna = input("Dígame una columna: \n")

    fila = input("Dígame la fila: \n")
    tabla[int(fila)-1, int(columna)-1] = caracter


tabla = crearTabla()
imprimirTabla(tabla)
repetir = True
caracterActual="X"
while repetir:
    caracterActual="X"
    print("---------------------------")
    imprimirTabla(tabla)
    pedirFicha(tabla, caracterActual)
    #probando que todo funciona correctamente
    
    repetir= checkGanador(tabla,"X")
    if(repetir==False):
        break;
    print("---------------------------")
    imprimirTabla(tabla)
    caracterActual="O"
    pedirFicha(tabla, caracterActual)
    repetir= checkGanador(tabla,"O")
    if(repetir==False):
        break;
    
print("---------------------------")
imprimirTabla(tabla)
print ("Ha ganado "+caracterActual)