##Hotel billing system
menu={
    'Pizza':40,
    'Burger':60,
    'Salad':80,
    'Coffee':90,
}


print("Welcome to Python Restaurant")
print("Pizza: Rs 40\nBurger: Rs 60\nSalad: Rs 80\nCoffee: Rs 90")
order_total=0

item_1=input("enter name of item you want to enter=")
if item_1 in menu:
    order_total+=menu[item_1]
    print(f"you item '{item_1}' has been added to your order")
else :
    print(f"Ordered item'{item_1}' is not available yet")

another_item=input("Do you want to add another item ? (Yes/No)")
if another_item=='Yes':
    item_2=input("enter name of second item=")
    if item_2 in menu:
        order_total+=menu[item_2]
        print(f"you item '{item_2}' has been added to your order")
    else :
        print(f"Ordered item'{item_2}' is not available !")
print(f"the total amount of items to pay is {order_total}")


