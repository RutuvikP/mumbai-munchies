inventory = {}
sales_records = []

def add_snack():
    snack_id = input("Enter the snack ID: ")
    snack_name = input("Enter the snack name: ")
    price = float(input("Enter the snack price: "))
    availability = input("Is the snack available? (yes/no): ")

    inventory[snack_id] = {
        'name': snack_name,
        'price': price,
        'availability': availability.lower() == 'yes'
    }

    print("Snack added to the inventory.")

def remove_snack():
    snack_id = input("Enter the snack ID to remove: ")

    if snack_id in inventory:
        del inventory[snack_id]
        print("Snack removed from the inventory.")
    else:
        print("Snack not found in the inventory.")

def update_availability():
    snack_id = input("Enter the snack ID to update availability: ")

    if snack_id in inventory:
        availability = input("Is the snack available? (yes/no): ")
        inventory[snack_id]['availability'] = availability.lower() == 'yes'
        print("Snack availability updated.")
    else:
        print("Snack not found in the inventory.")

def record_sale():
    snack_id = input("Enter the snack ID sold: ")

    if snack_id in inventory:
        if inventory[snack_id]['availability']:
            sales_records.append(snack_id)
            inventory[snack_id]['availability'] = False
            print("Sale recorded.")
        else:
            print("Snack is not available for sale.")
    else:
        print("Snack not found in the inventory.")

def display_menu():
    print("\n===== Snack Inventory Management =====")
    print("1. Add a snack to the inventory")
    print("2. Remove a snack from the inventory")
    print("3. Update snack availability")
    print("4. Record a sale")
    print("5. Quit\n")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_snack()
        elif choice == '2':
            remove_snack()
        elif choice == '3':
            update_availability()
        elif choice == '4':
            record_sale()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
