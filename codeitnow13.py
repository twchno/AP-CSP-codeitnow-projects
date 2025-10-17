#dylan King
#codeitnow13
#10/10/25

total_price = 0.0
total_items = 0
def add_tax():
    taxed_price = total_price * 1.07
    taxed_price = round(taxed_price, 2)
    print(f"Your total price with tax is ${taxed_price}.")
    exit()

def keep_adding():
    more = input("Add another item? (yes or no)\n")
    if more == "no":
        add_tax()
    elif more == "yes":
        add_items()
    else:
        print("Invalid option, try again.")

def add_items():
    global total_price
    global total_items
    price = float(input("How much does the item cost: \n"))
    total_price += price
    total_price = round(total_price, 2)
    total_items += 1
    print(f"You have {total_items} in your cart. The total price before tax is ${total_price}.\n")
    keep_adding()

if __name__ == "__main__":
    add_items()
