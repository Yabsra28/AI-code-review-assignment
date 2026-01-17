# Write your corrected implementation for Task 1 here.
# Do not modify `task1.py`.
def calculate_average_order_value(orders):
    if not orders:
        return 0.0

    total = 0.0
    count = 0

    for order in orders:
        if order.get("status") != "cancelled":
            total += float(order.get("amount", 0))
            count += 1

    if count == 0:
        return 0.0

    return total / count
