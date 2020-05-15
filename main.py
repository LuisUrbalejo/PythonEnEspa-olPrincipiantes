#!/usr/bin/python3
# Luis Urbalejo, para Python En Español (Principiantes)
import os, sys   # Librerías que se utilizan mucho
import funciones  # Mis funciones en Repl.it
# Nombres de mis variables....
# Utilizo UpperCamelCase y antepongo:
# str para variables de cadena: strNombre, strArchivo
# int para variables de tipo entero: intNumero, intEdad
# flt para flotantes
# bol para booleanos True y False
# lst para Listas
# tpl para tuplas
# dic para diccionarios
# Y así.... capicci?

# En el episodio de hoy...
# ================================================================== #

# A cada tecla del teléfono se le asignan letras en el siguiente orden 2-abc 3-def 4-ghi 5-jkl 6-mno 7-pqrs 8-tuv 9-wxyz. Cada letra se sustituye por el número al que está asignada + la posición que ocupa (que puede ser 1, 2, 3 ó 4); así la letra “e” será 32, y la letra “s” será 74. El espacio es el separador entre palabras se cifra con un *.
# Caso de prueba:
# cifrar("Hola mundo!")
# "42635321*6182623163"

def Cifrar(strPalabra):
    pass

lstTeclasTelefono = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]







# ================================================================== #
# ORDENAR 4 NUMEROS
# Método 1 .. el mas qlero...
intNum1 = int(input("Ingrese numero 1: "))
intNum2 = int(input("Ingrese numero 2: "))
if intNum1 > intNum2:
    intNum2, intNum1 = intNum1, intNum2
intNum3 = int(input("Ingrese numero 3: "))
if intNum2 > intNum3:
    intNum3, intNum2 = intNum2, intNum3
if intNum1 > intNum2:
    intNum2, intNum1 = intNum1, intNum2
intNum4 = int(input("Ingrese numero 4: "))
if intNum3 > intNum4:
    intNum4, intNum3 = intNum3, intNum4
if intNum2 > intNum3:
    intNum3, intNum2 = intNum2, intNum3
if intNum1 > intNum2:
    intNum2, intNum1 = intNum1, intNum2
print(intNum1, intNum2, intNum3, intNum4)

# Método 2.. burbujeichon
lstNumeros = []
for i in range(4):
    intNum = int(input("Ingrese numero " + str(i + 1) + ": "))
    lstNumeros.append(intNum)
    for x in range(len(lstNumeros) - 1):
        if lstNumeros[x] > lstNumeros[x + 1]:
            lstNumeros[x], lstNumeros[x + 1] = lstNumeros[x + 1], lstNumeros[x]
print(lstNumeros)

# Método 3... El peladitas
lstNumeros = []
for i in range(4):
    intNum = int(input("Ingrese numero " + str(i + 1) + ": "))
    lstNumeros.append(intNum)
print(sorted(lstNumeros))

sys.exit()


# ================================================================== #

# Necesito hacer una máquina de café, para lo cual debo cumplir con los iguientes parametros:
# a) seleccionar el tipo de café (ingresando la opción 1 o 2)
# b) solicitar dinero (100 o 200)
# c) comprobar el valor ingresado o mensaje de dinero incorrecto
# D) realizar función de preparacion
# E) entregar cafe
# F) entregar vuelto

# Además debo contemplar la opción de más vasos de café y almacenar número en una lista y entre cada operación, se debe ofrecer posibilidad de realizar otra operación o abandonar.
# Ah! Y todo esto tengo que hacerlo como si fuera por un teclado numérico...

while True:
    lstMenu = [
        ["Café Regular $100"],
        ["Café Más Caro Pero Más Rico $200"]
    ]
    intOpcion = funciones.MenuPrincipal(lstMenu,None,"\nLISTA DE CAFEs")
    intMoney = int(input("Ingrese Dinero: "))
    if intOpcion == 1 and intMoney >= 100:
        print("Preparando un rico café regular...")
        intCambio = intMoney - 100
    elif intOpcion == 2 and intMoney >= 200:
        print("Preparando un rico café más caro...")
        intCambio = intMoney - 200
    else:
        print("Dinero insuficiente...")
        print("Devolviendo", intMoney, "pesos")
        continue
    print("Su café está listo... disfrute!")
    print("Su cambio es de", intCambio)
    lstMenu = [
        ["Continuar"],
        ["Salir"]
    ]
    if funciones.MenuPrincipal(lstMenu,None,"\nQué desea?") == 2:
        break
sys.exit()


# ================================================================== #

def Suma2Numeros():
    print("\nFunción para SUMAR 2 números")

def Resta2Numeros():
    print("\nFunción para RESTAR 2 números")

def Multiplica2Numeros():
    print("\nFunción para MULTIPLICAR 2 números")

def Salir():
    return "S"

lstMenu =[
    ["Suma de 2 números", "Suma2Numeros()"],
    ["Resta de 2 números", "Resta2Numeros()"],
    ["Multiplica 2 Numeros", "Multiplica2Numeros"],
    ["Salir", "Salir()"]
]

while True:
    x = eval(funciones.MenuPrincipal(lstMenu, 1))
    if x == "S":
        break
print("Salió del while")


sys.exit()



# ================================================================== #
# print(value, ..., sep="", end=""), input(prompt)

# print() se usa para imprimir por pantalla
# puedes imprimir cadenas de texto, numeros, listas, varibles, etc. 
# Su sintaxis:
# print(objetos, ..., sep="separador entre objetos", end="end") # es más completo pero esto es lo básico

print("Hola Mundo")

print("Hola", "Mundo")

strSaludo = "Hola"
strMundo = "Mundo"
strPalabra = strSaludo + " " + strMundo

print(strPalabra)

print(strSaludo, strMundo)

print(strSaludo, "Mundo")

print("Hola", end="")
print(" ", end="")
print(strMundo)

# ================================================================== #
# input()   sirve para capturar/introducir datos por el teclado
# Su sintaxis:
# input("Cadena/Mensaje opcional")
# Siempre retorna un valor tipo string que será lo capturado
# Comunmente se asigna el retorno de input a una variable
print("Escribe tu nombre a continuación")
strNombre = input("Cómo te llamas? ")  # Luis
# Lo que hayas capturado se guardará en la variable strNombre 
print("Hola", "Mundo, digo", strNombre)

# ================================================================== #
# Ahora vamos a imprimir un sencillo Menú principal

print("\nMENU PRINCIPAL:\n")
print("1.- Suma de 2 números")
print("2.- Resta de 2 números")
print("99.- Salir\n")
strOpcion = input("Seleccione una Opción: ")
print("Su opción fue", strOpcion)
print("...")


sys.exit()  # Con sys.exit() marcaremos el final de este ejercicio


# ================================================================== #
lstTexto = [["el es como el agua"], ["es agua es azul y como el cielo"]]
for lstLista in lstTexto:
    intMasRepetido = 0
    strPalabraMasRepetida = ""   # innecesario
    for strPalabra in lstLista[0].split():
        intConteo = lstLista[0].count(strPalabra)
        if intConteo > intMasRepetido:
            intMasRepetido =  intConteo
            strPalabraMasRepetida = strPalabra
    print(strPalabraMasRepetida, "con", intMasRepetido )

sys.exit()  # Con sys.exit() marcaremos el final de este ejercicio


# ================================================================== #
# Por obvias razones esto es un entorno virtual
# Mi carpeta de trabajo es "/home/runner/PythonEnEspanolPrincipiantes"
strRutaDeTrabajo = os.getcwd()
strArchivo = os.path.join(strRutaDeTrabajo, "Nuevotexto.txt")
print(strRutaDeTrabajo, strArchivo)

print(os.listdir(strRutaDeTrabajo))
print(os.path.isfile(strArchivo))

sys.exit()

# ================================================================== #
# Una antigua conjetura indica que todo número primo mayor a 5 puede ser escrito como la suma de tres números primos. Por ejemplo el numero primo 31 puede escribirse como la suma de los primos 3,5,23.

# También podría expresarse como la suma de 5,3,23 lo que se busca son los números más pequeños, escritos en orden ascendente.

# Recordemos que los números primos son aquellos que solo son divisibles por sí mismos y por uno. El número uno no se considera como un numero primo.

# Escriba un programa en Python que reciba como entrada un número entero n, se garantiza que 7 ≤ n ≤ 10000, y de como salida los tres números primos, uno por línea.



n = int(input("Número: "))

if 7 <= n <= 10000:
  Sgtes3Primos=0
  
  while Sgtes3Primos < 3:
    if funciones.EsPrimo(n):
      print(n)
      Sgtes3Primos += 1
    n +=1

sys.exit()


# ================================================================== #
# Escriba un programa que tome un número entero positivo como entrada, lo invierta, luego lo sume al número original, luego otra vez lo invierta y lo suma.

# Este proceso se repite hasta que la suma sea capicúa o se haya hecho 100 sumas. Por ejemplo el 14 lo invertimos y obtenemos 41 sumamos al número original obteniendo 55 es capicúa. Imprimimos 55.
# Otro ejemplo 95 + 59 = 154. Invertimos y sumamos 154 + 451 = 605. Repetimos el proceso 605 + 506 = 1111 que es capicúa.

def proceso(intNumero):
    lstEncontrados = []
    intNumeroDeSumas = 0
    while intNumeroDeSumas <= 100:
        intNumeroInvertido = int(str(intNumero)[::-1])
        intSuma = intNumero + intNumeroInvertido
        # print(intNumero, "+", intNumeroInvertido, "=", intSuma, end="")
        if intSuma == int(str(intSuma)[::-1]):  # Es Capicua?
            # print(intSuma)
            lstEncontrados.append(
                f"{intNumero} + {intNumeroInvertido} = {intSuma}")
            # se supone que break?
        # print()
        intNumero = intSuma
        intNumeroDeSumas += 1
    return lstEncontrados


if __name__ == "__main__":
    while True:  # Este while es por si quieres que siga preguntando
        try:
            intNumero = int(input("Introduzca un número entero positivo: "))
            if intNumero > 0:
                for capicua in proceso(intNumero):
                    print(capicua)
                break
            else:
                print(intNumero, "no es entero positivo...")
        except:
            print("ERROR! ..Un número entero positivo dije!")
