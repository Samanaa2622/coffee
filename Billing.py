from Order import orders
def calculate_total():
    total = 0
    for order in orders:
        total += order["price"] * order["quantity"]
    return total
def calculate_discount(total):
    if total > 1000000:
        discount = total * 0.10
    else:
        discount = 0
    return discount
def print_invoice():
    if len(orders) == 0:
        print("No orders available to print an invoice.")
        return
    total = calculate_total()
    discount = calculate_discount(total)
    final_amount = total - discount
    print("\n========== Final Invoice ==========")
    for order in orders:
        print("Product:", order["product"])
        print("Quantity:", order["quantity"])
        print("-----------------------------------")
    print("Total amount:", total, "Toman")
    print("Discount:", discount, "Toman")
    print("Final amount:", final_amount, "Toman")
    print("===================================")
