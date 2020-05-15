#!/usr/bin/python3
# Luis Urbalejo, para Python En Español (Principiantes)

# ================================================================== #
def PideEntero(strTexto="", intMin=0, intMax=0):
    
    while True:
        try:
            intNumero = int(input(strTexto))
            if intMin and intMax:
                if intMin <= intNumero <= intMax:
                    return intNumero
                else:
                    print("No está en el rango", intMin, "-", intMax)
                    continue
            return intNumero
        except:
            pass
        
# ================================================================== #
def MenuPrincipal(lstMenu, intRetorno=None, strMenuPpal="\nM E N U   P R I N C I P A L\n"):
    while True:
        print(strMenuPpal)
        for intIndice in range(len(lstMenu)):
           print(intIndice + 1, lstMenu[intIndice][0])
        try:
            intOpcion = int(input("\nSeleccione una Opción: "))
            if 1 <= intOpcion <= len(lstMenu):
                if intRetorno == None:
                    return intOpcion
                return lstMenu[intOpcion -1][intRetorno]
        except:
            pass

# ================================================================== #
def EsPar(intNumero): 
    # Cómo saber si es par?
    # Todo número par es divisible entre 2
    # Así que si dividimos entre 2 y hay residuo NO es par 
    return (intNumero % 2) == 0 

# ================================================================== #
def EsPrimo(intNumero):
    if intNumero < 2:
        return False
    for intN in range(2, intNumero):
        if intNumero % intN == 0:
            return False
    return True

    