menu = {
    'coffe':250,
    'pancake':200,
    'french fires':180,
    'toast':150,
}
# print("""coffee: Rs250
#          pancake: Rs200
#          french fires: Rs180 
#          toast:150
#                              """)

print("welcome to our cafe")
print("coffee: Rs250\npancake: Rs200\nfrench fires: Rs180\ntoast:150")

order_total = 0
 
item = input("enter the name of item you want = ")
if item in menu:
    order_total += menu[item]
    print("your item has been added to your order")
else:
    print("ordered item is not avaialable yet!")
# print("the total amount of items to pay {order_total}")   

another_order = input("do you want anothercitem?(yes/no)")
if another_order =='yes':
    item1 = input("enter the name of second item = ")
    if item1 in menu:
        order_total =+ menu[item1]
        print("item {item1}has been added to order")
else:
    print("order item {item1} is not avaialable!")
print("the total amount of items to pay is {order_total}")   


