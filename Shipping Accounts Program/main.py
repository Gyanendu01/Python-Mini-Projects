print("Welcome to the Shipping Accounts Program")

# Allowed usernames in the database
usrNameList = ['gyanendu','john','raghu','sukesh','mukesh']
usrName = input("\nHello, what is your username: ")

if usrName.lower() in usrNameList:
    print(f"\nHello {usrName}. Welcome back to your account.\nCurrent shipping prices are as follows:")
    print("\nShipping orders 0 to 100: $5.10 each\nShipping orders 100 to 500: $5.00 each\nShipping orders 500 to 1000: $4.95 each\nShipping orders over 1000: $4.80 each")
    
    # Taking the number of shipping orders from the customer
    while True:
        numOfItems = (input("\nHow many items would you like to ship: "))
        if numOfItems.isdigit():
            numOfItems = int(numOfItems)
            break
        else:
            print("Shipping items must be an integer number.")
    
    # calculating the amount the customer has to pay based on the number of shipping items
    if numOfItems >= 1000:
        print(f"To ship {numOfItems} items it will cost you ${round(numOfItems*4.80,3)} at $4.80 per item")
    elif numOfItems >= 500:
        print(f"To ship {numOfItems} items it will cost you ${round(numOfItems*4.95,3)} at $4.95 per item")
    elif numOfItems >= 100:
        print(f"To ship {numOfItems} items it will cost you ${round(numOfItems*5.00,3)} at $5.00 per item")
    elif numOfItems >= 1:
        print(f"To ship {numOfItems} items it will cost you ${round(numOfItems*5.10,3) } at $5.10  per item")

    # Checking for the confirmation of the order
    confirmation = input("\nWould you like to place this order (y/n): ")
    if confirmation.lower() == "y":
        print(f"Okay. Shipping your {numOfItems} items.")
    else:
        print("Okay, no order is being placed at this time.")

else:
    print("Sorry, you do not have an account with us. Goodbye.")