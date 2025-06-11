# WAP to find particular string using simple for loop and simple if condition.
list = ["onion","potato","tomato"]
item = input("enter the item you want")
for x in list:
    if item in list:
       print("item in this list")
       break
    else:
       print("item is not in list")
       break


