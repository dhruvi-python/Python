num1 = int(input("enter your first number"))
num2 = int(input("enter your second number"))
print("enter 1 for addition")
print("enter 2 for substraction")
print("enter 3 for division")
print("enter 4 for multiplixen")
choice = int(input("enter your choice"))
match choice:
    case 1:
        print(num1 + num2)
    case 2:
        print(num1 - num2)
    case 3:
        print(num1 // num2)
    case 4:
        print( num1 * num2)
    case _:
        print(choice)
