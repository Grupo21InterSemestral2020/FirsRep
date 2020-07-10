def calcularSuma(numini,numfin):
    suma=0
    for num in range(numini,numfin+1):
        suma += num
    return suma

def calcularSuma2(numini,numfin):
    suma=0
    for num in range(numini,numfin+1):
        suma += num
    print(f"La suma es:{suma}")

#probar la funciom
print(f"La suma es:{calcularSuma(1,10)}")
calcularSuma2(10,100)