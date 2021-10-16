"""
 An application for a restaurant menu that allow any client to order online
"""

"""
Once the program run, it will print an intro message, additionally the program will tell the user how to exit.
"""
quiting = "quit"
print("**************************************")
print("**    Welcome to the Snakes Cafe!   **")
print("**    Please see our menu below.    **")
print("**                                  **")
print(f"**  To quit at any time, type {quiting}  **")
print("**************************************")
print(" ")
menu = [
    {"choice": "Appetizers", "options": [
        "Wings", "Cookies", "Spring", "Rolls"]},
    {"choice": "Entrees", "options": [
        "Salmon", "Steak", "Meat", "Tornado", "A Literal Garden"]},
    {"choice": "Desserts", "options": ["Ice Cream", "Cake", "Pie"]},
    {"choice": "Beverages", "options": ["Coffee", "Tea", "Unicorn Tears"]},
]

""" 
How to print a list of items, and each one of them will appear on a new line, I got help with this from GeekesforGeeks: https://www.geeksforgeeks.org/print-lists-in-python-4-different-ways

The loop will go through the menu and print as required
"""
for i in range(len(menu)):
    print(menu[i]["choice"])
    print("---------")
    options = menu[i]["options"]
    print(*options, sep="\n")
    print(" ")


""" 
The > character represents user input line and should be printed out with a trailing space, I got help with this from ==> StackOverFlow: https://stackoverflow.com/questions/8599440/new-line-for-input-in-python

The program will ask the user for an order
"""
orders = []
user_order = ""
print("**************************************")
user_order = input(
    f"What would you like to order? \n**************************************\n>")

"""
The program will print an acknowledgment, when a user enters an item.
"""
while user_order:
    if user_order.lower() != 'quit':
        orders.append(user_order)
        print(
            f"\n** {orders.count(user_order)} order of {user_order} have been added to your meal**\n")
        user_order = input(f">")
    else:
        break
print("\n**************************************")
print("Your orders list")
for x in range(len(orders)):
    print(orders[x], sep="\n")
print("**************************************")
