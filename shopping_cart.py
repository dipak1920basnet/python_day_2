# Partial guidence exercises

laptop_price = 270000
mouse_price = 300
keyboard_price = 2000

laptop_quantity = 10
mouse_quantity = 30
keyboard_quantity = 20

# Update the state and store it 
laptop_total = laptop_price * laptop_quantity
mouse_total = mouse_price * mouse_quantity
keyboard_total = keyboard_price  * keyboard_quantity

cart_total = laptop_total + mouse_total + keyboard_total

print(f"Laptop total: {laptop_total}")
print(f"Mouse total: {mouse_total}")
print(f"Keyboard total {keyboard_total}")

print()
print(f"Cart total: {cart_total}")


# Adding a discount rule: 
if cart_total > 1000:
    print("You get 10% discount")