# Write a Python program to check if a person is eligible to donate blood using a nested if.
age = int(input("enter your age"))
weight = float(input("enter your weight"))
if age > 18:
 print("you can donate a blood")
if (weight < 50):
  print("you can not donted a blood")
else:
 print("you can donate but check your blood percentage")

# Write a Python program to calculate grades based on percentage using # if-else ladder.
percentage = int(input("write your percentage = "))
if (percentage <= 100) and (percentage >= 90):
  print("grade A+")
elif (percentage <= 89) and (percentage >= 71):
   print("grade A")
elif (percentage <= 70) and (percentage >= 61):
   print("grade B")
elif (percentage <= 60) and (percentage >= 51):
   print("grade C")
elif(percentage <= 50):
   print("grade D")

                 