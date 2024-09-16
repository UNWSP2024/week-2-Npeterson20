def calculate_total_purchase():
    # # A customer in a store is purchasing five items.  
    tax_rate = 0.07  # 7% sales tax

# Write a program that asks for each item
    item1 = float(input("Enter the price of item 1: "))
    item2 = float(input("Enter the price of item 2: "))
    item3 = float(input("Enter the price of item 3: "))
    item4 = float(input("Enter the price of item 4: "))
    item5 = float(input("Enter the price of item 5: "))

# then displays the subtotal of the sale,
    subtotal = item1 + item2 + item3 + item4 + item5

# the amount of sales tax, and the total.
    sales_tax = subtotal * tax_rate
    total = subtotal + sales_tax

# Assume the sales tax is 7 percent.
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Sales Tax: ${sales_tax:.2f}")
    print(f"Total: ${total:.2f}") 


calculate_total_purchase()
