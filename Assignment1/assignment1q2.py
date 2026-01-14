# Question 2: Order History Tracker (Mutable Parameter)

# This function keeps track of all order IDs across multiple calls.
# It shows how to use mutable parameters safely by avoiding the default mutable argument pitfall.
# Lists are mutable in Python, so if we used 'orders=[]' directly as a default,
# it would keep changing across function calls, which can cause unexpected behavior.
# To prevent that, we use 'orders=None' and create a new list inside the function when needed.

def add_order(order_id, orders=None):
    # If orders is None, create a new empty list
    if orders is None:
        orders = []
    
    # Add the new order ID to the list
    orders.append(order_id)
    
    # Print and return the current list of orders
    print("Current Orders:", orders)
    return orders


# --- Test Calls ---

# Each call here creates a new list because we didn't pass an existing one.
add_order(101)   # Output: Current Orders: [101]
add_order(102)   # Output: Current Orders: [102]

# To keep the order history across multiple calls, 
# we can store the returned list in a variable and pass it again:
order_history = []
order_history = add_order(201, order_history)
order_history = add_order(202, order_history)
order_history = add_order(203, order_history)

print("Final Order History:", order_history)
# Expected Output:
# Current Orders: [201]
# Current Orders: [201, 202]
# Current Orders: [201, 202, 203]
# Final Order History: [201, 202, 203]
