Menu=1
while Menu != 3:
    print("MENU")
    print("1)Suma")
    print("2)Resta")
    print("3)Multiplicacion")
    print("4)Division")
    print("5)(Salir")
    Menu=int(input("Seleción: "))
    if Menu == 1:
        numero1=int(input("Dame un numero:"))
        numero2=int(input("Dame otro numero:"))
        suma= numero1 + numero2
        print(f'La suma de los dos numeros es:{suma}')
    elif Menu==2:
        numero1=int(input("Dame un numero:"))
        numero2=int(input("Dame otro numero:"))
        Resta= numero1 - numero2
        print(f'La resta de los dos numeros es:{Resta}')
    elif Menu==3:
        numero1=int(input("Dame un numero:"))
        numero2=int(input("Dame otro numero:"))
        Multiplicacion= numero1 * numero2
        print(f'La multiplicacion de los dos numeros es:{Multiplicacion}')
    elif Menu==4:
        numero1=int(input("Dame un numero:"))
        numero2=int(input("Dame otro numero:"))
        Division= numero1 / numero2
        print(f'La Division de los dos numeros es:{Division}')
    elif Menu==5:
        break