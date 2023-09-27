# Cafe Menu
menu = {
    "Sandwiches": ["Python sandwich", "Trojan sandwich", "Veggie Wrap"],
    "Beverages": ["Mystic Mocha", "Malware Macchiato", "Brain Juice", "Orange Juice"],
    "Books": ["Power of Positivity", "Chronicles of Cloud", "Lazy Linux", "Growth Mindset"]
}
# Displaying the Menu
print("Welcome to Chapter & Chai! Here's our menu:")
for category, items in menu.items():
    print(f"\n{category}:")
    for item in items:
        print(f"- {item}")
# Employee Access to Menu
employee_access = input("\nDo you have employee access? (yes/no) ")
if employee_access.lower() == "yes":
    print("\nEmployee Menu Options:")
    print("- Update menu items")
    print("- Add new menu items")
    update_menu = input("\nWhat would you like to do? Please enter 'update' or 'add': ")
    if update_menu.lower() == "update":
        print("\nCurrent Menu:")
        for category, items in menu.items():
            print(f"\n{category}:")
            for item in items:
                print(item)
        category = input("\nEnter the category you want to update: ")
        if category in menu:
            print(f"\nCurrent items in {category}:")
            for item in menu[category]:
                print(item)
            item_to_update = input("\nEnter the item you want to update: ")
            if item_to_update in menu[category]:
                new_item = input("\nEnter the new item name: ")
                menu[category][menu[category].index(item_to_update)] = new_item
                print("\nMenu has been updated successfully!")
            else:
                print("\nItem not found in the menu. Please try again.")
        else:
            print("\nCategory not found in the menu. Please try again.")
    elif update_menu.lower() == "add":
        category = input("\nEnter the category you want to add to: ")
        if category in menu:
            new_item = input("\nEnter the new item name: ")
            menu[category].append(new_item)
            print("\nNew item has been added to the menu successfully!")
        else:
            print("\nCategory not found in the menu. Please try again.")
# Ordering from the Menu
order = input("\nWhat would you like to eat or drink? Please enter the item name: ")
print(f"\nYou have ordered: {order}.")
if order in [item for items in menu.values() for item in items]:
    print("Great choice!")
else:
    print("I'm sorry, but that item is not currently available on our menu.")
order2= input ("\nPlease choose something from the Menu and enter here: ")
read = input("\nNow what would you like to read? Please enter the book of your choice:")
print (f"\nYou have chosen to read: {read}. Great choice, read and sip! " )
Customer_info = input("\nWhat is your name? ")
Customer_address = input ("\n What is your Full address?")
print(f"\nThank you, {Customer_info}! You have ordered: {order} and {read} to read. We will deliver it to {Customer_address}. We hope you enjoy!")