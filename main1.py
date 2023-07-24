import numpy as np

def pedirTresCosas(tablaArr):
    a=7
    while a!=0:
        print("Qué deseas hacer")
        print("1-Mostrar el panel por pantalla")
        print("2-Pedir dónde quieres poner una X")
        print("0-Salir")
        a=int(input("Dígame la opción"))
        if a==1:
            print(tablaArr)
        elif a==2:
            lugar=int(input("¿Donde deseas colocar la X?"))-1
            tablaArr[lugar]='X'
            print(tablaArr)
        
            
    
    
def cuantasX(tablaArr):
    contador=0;
    for i in tablaArr:
        if i=='X':
            contador=contador+1
    return contador
def convertirGuiones(tablaArr):
    a =tablaArr.size
    for x in range(a):
        tablaArr[x]='-'
    return tablaArr    
    
    #for i in tablaArr:
        



tabla =  ['-','-','-','X','X', '-','X', '-', '-', '-','X','X'];
tablaArr=np.array(tabla)

print(tablaArr)
contadorX=cuantasX(tablaArr)

print("El número total de X es igual a "+str(contadorX))
tablaConvertida= convertirGuiones(tablaArr)
print (tablaConvertida)
pedirTresCosas(tablaConvertida)


