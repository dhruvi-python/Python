# import pyttsx3
# engine = pyttsx3.init()
# engine.say("hey i am good")
# engine.runAndWait()

# num = 1234
# reversed_number = 0

# while num != 0:
#     digit = num % 10
#     reversed_number = reversed_number * 10 + digit
#     num = num // 10

# print("reversed number :", reversed_number)


# name = ("dhruvi,vanshika,kavya,ruhi")
# reversed_name = 0

# while name != 0:
#     variable = name % 10
#     reversed_name = reversed_name * 10 + digit
#     num = num // 10

# print("reversed name :", reversed_name)
menu = {
    'coffee': 250,
    'pancake': 200,
    'french fries': 180,
    'toast': 150,
}

print("Welcome to our cafe")
print("Menu:")
for item, price in menu.items():
    print(f"{item}: Rs{price}")

order_total = 0
ordered_items = []

while True:
    item = input("\nEnter the name of the item you want (or type 'done' to finish): ").lower()
    if item == 'done':
        break
    if item in menu:
        order_total += menu[item]
        ordered_items.append(item)
        print(f"{item} has been added to your order.")
    else:
        print("Ordered item is not available!")

# Show order summary
print("\nYour Order Summary:")
for i in ordered_items:
    print(f"- {i}: Rs{menu[i]}")

print(f"\nThe total amount of items to pay is Rs{order_total}")






