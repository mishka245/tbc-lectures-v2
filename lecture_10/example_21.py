
def create_order(order_type, name, quantity=1, *args, **kwargs):
    print("Order type:", order_type)
    print("Food:", name)
    print("Quantity:", quantity)
    if args:
        print("Extras:")
        for extra in args:
            print("\t", extra)

    if kwargs:
        print("Special instructions:")
        for key, value in kwargs.items():
            print(f"\t{key}: {value}")

create_order("Takeaway", "Pizza", 2)
print("*" * 50)
create_order("Dine-in", "ხინკალი", 99, "ძმარი", "პილპილი")
print("*" * 50)
create_order("Delivery", "ხინკალი", 99, "ძმარი", "პილპილი", special="მწვანილის გარეშე გაგვიკეთეთ 49 ცალი <3")

