# =========================================
# Topic: Smart Shopping Checkout Simulator
# Description: A simple billing system that calculates subtotal, applies discounts, and adds tax
# Author: Shaurya Parashar
# =========================================

# ---- Input ----
item = input("Enter item name: ")
price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))
is_member = input("Are you a member (yes/no): ").lower()
coupon_code = input("Enter your coupon code: ").upper()

# ---- Calculations ----
subtotal = price * quantity

# Initialize discount value
discount = 0

# ---- Discount Rules ----
# Apply 10% discount if subtotal is 1000 or more
if subtotal >= 1000:
    discount += subtotal * 10 / 100
    print("10% discount applied")

# Apply 5% member discount if customer is a member
if is_member == "yes":
    discount += subtotal * 5 / 100
    print("5% member discount applied")

# Apply flat ₹200 coupon discount for valid coupon code
if coupon_code == "SAVE10":
    discount += 200
    print("Flat ₹200 discount applied")
elif coupon_code != "":
    print("Invalid coupon")

# Safety check: discount should never exceed subtotal
if discount > subtotal:
    discount = subtotal

# ---- Tax and Final Amount ----
# Calculate amount after discount
amount_after_discount = subtotal - discount

# Add 5% tax on discounted amount
tax = amount_after_discount * 5 / 100

# ---- Final Bill Summary ----
final_amount = amount_after_discount + tax

print("\n--- BILL SUMMARY ---")
print("Item:", item)
print("Quantity:", quantity)
print("Subtotal: ₹", subtotal)
print("Total Discount: ₹", discount)
print("Tax: ₹", tax)
print("Final Amount: ₹", final_amount)

# ---- Notes ----
# Practiced input handling, type casting, operators, if-else logic, discounts, and tax calculation