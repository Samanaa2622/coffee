from Menu import menu
orders=[]
def add_order():
    product=input("Enter product name: ")
    if product not in menu:
        print("Not available")
        return
    quantity=int(input("Enter quantity: "))    
    order={
        "product":product,
        "price":menu[product],
        "quantity":quantity
       
    }
    orders.append(order)
    print("Order added successfully!")
def show_orders():
    if len(orders)==0:
        print("No orders have been registered yet.")
        return
    print("....Your Orders ....")
    for order in orders:
        print("Product:", order["product"])
        print("Price:", order["price"])
        print("Quantity:", order["quantity"])
        print("......................")
