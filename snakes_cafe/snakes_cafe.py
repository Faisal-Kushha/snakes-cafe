"""
 An application for a restaurant menu that allow any client to order online
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
    {"choice": "Appetizers", "options": ["Wings", "Cookies", "Spring", "Rolls"]},
    {"choice": "Entrees", "options": ["Salmon", "Steak", "Meat", "Tornado", "A Literal Garden"]},
    {"choice": "Desserts", "options": ["Ice Cream", "Cake", "Pie"]},
    {"choice": "Beverages", "options": ["Coffee", "Tea", "Unicorn Tears"]},
]

# How to print a list of items, and each one of them will appear on a new line, I got help with this from GeekesforGeeks: https://www.geeksforgeeks.org/print-lists-in-python-4-different-ways

for i in range(len(menu)):
    print(menu[i]["choice"])
    print("---------")
    options = menu[i]["options"]
    print(*options, sep="\n")
    print(" ")



# The > character represents user input line and should be printed out with a trailing space, I got help with this from ==> StackOverFlow: https://stackoverflow.com/questions/8599440/new-line-for-input-in-python
orders = []
user_order = ""
while user_order != "quit":
    print("**************************************")
    user_order = input(f"** What would you like to order? **\n>")

    if user_order != 'quit':
        orders.append(user_order)
        
    elif user_order == 'quit':
        continue
    print("**************************************")
    print(f"** An order of {user_order} have been added to your list**")
   
print("**************************************")
print("Your orders list")
for x in range(len(orders)):
    print(orders[x], sep="\n")
print("**************************************")