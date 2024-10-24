# ctrl + G
def order_food(item, *args):
    print("Ordered food", item)
    if args:
        print("Extras:")
        for extra in args:
            print("\t", extra)


order_food("Pizza")
order_food("Pizza", "Extra cheese")
order_food("Pizza", "Extra cheese", "Extra peperoni")
