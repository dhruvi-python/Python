# W.A.P to skip the (Banana) from the list using Continue Statement List1 -(apple,banana,mango)
list1 = ("apple","banana","mango")
for fruit in list1:
    if fruit == "banana":
        continue 
    print(fruit)

# W.A.P to break the for loop when (Banana) get in if Condition.
vegitables =["onion","tomato","potato","cucumber"]
for vegitables in vegitables:
    if vegitables == "tomato":
        print("tomato,breaking the loop")
        break
    print("vegitables")




