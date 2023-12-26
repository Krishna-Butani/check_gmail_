def arithmatic(a,b,i):    
    match(i):
        case 1:
            print("Sum: ",a+b)
        case 2:
            print("Subtraction: ",a-b)
        case 3:
            print("Multiplication: ",a*b)
        case 4:
            print("Division: ",a/b)
        case 5:
            print("Modulo: ",a%b)
        case 6:
            print("Floor Division: ",a//b)
        case 7:
            print("Exponent Power: ",a**b)
        case _:
            print("Invalid")

print("1.sum")
print("2.sub")
print("3.mul")
print("4.dived")
print("5.modulo")
print("6.Floor division")
print("7.exponent power")

a = int(input("Enter a First number: "))
b = int(input("Enter a second number: "))
i = int(input("Enter a choice number: "))
arithmatic(a,b,i)