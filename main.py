def cociente(num1,num2):
    return num1 / num2
def resto(num1,num2):
    return num1 % num2
def incremento2(num1):
    if num1 < 0:
        num1 = num1 + 1
        print("Número incrementado correctamete ", num1)
    else:
        num1 = num1 - 1
        print("El número disminuyó correctamente ", num1)
def PareImpar(n):
    for i in range(0, n +1):
        n = i
        result = n
        if n % 2 == 0:
            print("El ",  n ," es par")
        else:
            print("El " , n ," es impar")
    return result

while(True):
    opcion = int(input("Elige una de estas opciones (1,2,3): "))
    if opcion == 1:
        num1 = int(input("Ingresa un dividendo: "))
        num2 = int(input("Ingresa un divisor: "))
        print("Cociente = ", cociente(num1,num2))
        print("Resto = ", resto(num1,num2))
    elif opcion == 2:
        num1 = int(input("Ingresa un número: "))
        incremento2(num1)
    elif opcion == 3:
        num1 = int(input("Ingrese un número: "))
        PareImpar(num1)
    else:
        break    



    
