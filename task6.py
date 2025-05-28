name = input("enter the name")
print(name)

a = 10 
b = 8
print(a+b)

num1 = int(input("enter first number"))
num2 = int(input("enter second number"))
print(num1+ num2)
print(num1- num2)

a = "10"
b = "5"
print(int(a) + int(b)) 

name = ("dhruvi")
print(name[2:-2])
print(name[-2])
print(name[2:4])

# Write a Python program to find greater and less than a number using if_else.
num1 = int(input("enter first number"))
if (num1 > 0):
 print("big num")
else: 
 print("not big num")

#case
y = int(input("enter the value of y: "))
match y:
     case 0:
          print("y is zero")
     case 2:    
          print("case is 2")
        #   if(y > 0):
          print("d")
     case _:
          print(y)

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



    
    
