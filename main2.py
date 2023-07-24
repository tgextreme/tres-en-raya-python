import numpy as np

#punto 5
def ocupadoXY(tabla, fila, columna, caracter):
    if tabla[int(fila)-1, int(columna)-1]=="-":
        tabla[int(fila)-1, int(columna)-1]=caracter
        return 1
    else:
        print("elija otro sitio")
        return 0
#código del último día
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
# 4 crear tabla
def crearTabla():
    tabla = np.array ([['-','-','-'],['-','-', '-'],['-', '-', '-']])
    return tabla
# punto 6
def pedirFicha(tabla, caracter):
    continuar=0
    while continuar==0:
        columna = input("Dígame una fila("+caracter+  "): \n")
        fila = input("Dígame la columna ("+caracter+  "): \n")
        continuar= ocupadoXY(tabla, int(fila), int(columna), caracter)
        
        
#punto 4 imprimirla
def imprimirTabla(tabla):

    for x in range(3):
        linea = "|"
        for y in range(3):
            linea = linea+str(tabla[y][x])+"|"
        print(linea)
        
tabla = crearTabla()
imprimirTabla(tabla)
repetir = True
caracterActual="X"
while repetir:
    caracterActual="X"
    print("---------------------------")
    imprimirTabla(tabla)
    pedirFicha(tabla, caracterActual)
 
    
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