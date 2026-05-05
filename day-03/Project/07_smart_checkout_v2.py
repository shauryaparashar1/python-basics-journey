# =========================================
# Project: Smart Checkout System v2
# Description: A menu-based billing system that allows the user to add items,
#              calculate subtotal, apply discounts, add tax, and generate a final bill.
# Upgraded From: The previous one-time billing version
# Improvements:
# - Menu-based flow using while loop
# - Multiple item entry
# - Input validation
# - Clean string handling
# - Better bill formatting
# Author: Shaurya Parashar
# =========================================

print("Welcome to Smart Checkout System v2")

# Stores the running total of all items added to the cart
cart_total = 0

# Main menu loop
while True:
    print("\n--------- MAIN MENU ---------")
    print("1. Add Item")
    print("2. Checkout")
    print("3. Exit")

    choice = input("Enter your choice: ").strip()

    # -------------------------------------------------
    # Option 1: Add Item
    # -------------------------------------------------
    if choice == "1":
        # Take item name and clean extra spaces
        item_name = input("Enter item name: ").strip().title()

        # Take and validate price
        price_input = input("Enter item price: ").strip()
        if price_input == "":
            print("Price cannot be empty.")
            continue

        # Take and validate quantity
        quantity_input = input("Enter item quantity: ").strip()
        if quantity_input == "":
            print("Quantity cannot be empty.")
            continue

        try:
            price = float(price_input)
            quantity = int(quantity_input)
        except ValueError:
            print("Please enter valid numeric values for price and quantity.")
            continue

        # Check for invalid values
        if price < 0:
            print("Price cannot be negative.")
            continue

        if quantity <= 0:
            print("Quantity must be at least 1.")
            continue

        # Calculate subtotal for this item
        subtotal = price * quantity

        # Add item subtotal to cart total
        cart_total += subtotal

        # Show confirmation message
        print(f"Item Added: {item_name} | Price: ₹{price:.2f} | Quantity: {quantity} | Subtotal: ₹{subtotal:.2f}")

    # -------------------------------------------------
    # Option 2: Checkout
    # -------------------------------------------------
    elif choice == "2":
        # If cart is empty, checkout is not possible
        if cart_total == 0:
            print("Cart is empty. Add items first.")
            continue

        # Ask for membership status and coupon code
        membership = input("Are you a member? (yes/no): ").strip().lower()
        coupon_code = input("Enter coupon code if any: ").strip().lower()

        # Start with no discount
        discount = 0

        # Membership discount
        if membership == "yes":
            discount += cart_total * 0.10

        # Coupon discount logic
        if coupon_code == "save10":
            discount += cart_total * 0.10
        elif coupon_code == "welcome5":
            discount += cart_total * 0.05
        elif coupon_code == "":
            pass
        else:
            print("Invalid coupon code. No coupon discount applied.")

        # Calculate final bill
        discounted_total = cart_total - discount
        tax = discounted_total * 0.05
        final_amount = discounted_total + tax

        # Print formatted bill
        print("\n=========== FINAL BILL ===========")
        print(f"Subtotal     : ₹{cart_total:.2f}")
        print(f"Discount     : -₹{discount:.2f}")
        print(f"Tax (5%)     : +₹{tax:.2f}")
        print(f"Final Amount  : ₹{final_amount:.2f}")
        print("==================================")

    # -------------------------------------------------
    # Option 3: Exit
    # -------------------------------------------------
    elif choice == "3":
        print("Thank you for using Smart Checkout System v2.")
        break

    # -------------------------------------------------
    # Invalid menu choice
    # -------------------------------------------------
    else:
        print("Invalid choice. Please select 1, 2, or 3.")