def cociente(num1,num2):
    return num1 / num2
def resto(num1,num2):
    return num1 % num2
def incremento2(num1):
    if num1 < 0:
        num1 = num1 + 1
        print("Correctly incremented number ", num1)
    else:
        num1 = num1 - 1
        print("The number decreased correctly ", num1)
def PareImpar(n):
    for i in range(0, n +1):
        n = i
        result = n
        if n % 2 == 0:
            print("The ",  n ," is even")
        else:
            print("The " , n ," is odd")
    return result

while(True):
    try:
        print(" 0.Exit \n","1.Division\n","2.Increase and Decrease\n","3.Even and odd\n")
        opcion = int(input("Choose one of these options (0,1,2,3): "))
        if opcion == 1:
            num1 = int(input("Enter a dividend: "))
            num2 = int(input("Enter a divisor: "))
            print("Quotient = ", cociente(num1,num2))
            print("Rest = ", resto(num1,num2))
        elif opcion == 2:
            num1 = int(input("Enter a number: "))
            incremento2(num1)
        elif opcion == 3:
            num1 = int(input("Enter a number: "))
            PareImpar(num1)
        elif opcion == 0:
            break
        else:
            print("Put one of the options")
    except Exception as error:
        print("Not an option :)")
        print(error)