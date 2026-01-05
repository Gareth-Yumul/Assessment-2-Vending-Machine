#John Gareth Kyle C. Yumul

#Will be used for exits
import sys

#Menu for Filipino Vending Pagkain
Categories = {
    "Inumin": {
        "I1": {"Name": "Buko Juice", "Price": 4.00, "Stock": 5},
        "I2": {"Name": "Melon Juice", "Price": 4.00, "Stock": 3},
        "I3": {"Name": "Calamansi Juice", "Price": 3.00, "Stock": 7},
        "I4": {"Name": "Buko Pandan Shake", "Price": 6.00, "Stock": 6},
        "I5": {"Name": "Gulaman", "Price": 3.50, "Stock": 1},
        "I6": {"Name": "Ice Coffee", "Price": 3.00, "Stock": 2},
        "I7": {"Name": "Iskrambol", "Price": 2.50, "Stock": 4},
    },
    
    "Pagkain": {
        "P1": {"Name": "Dinuguan", "Price": 4.00, "Stock": 9},
        "P2": {"Name": "Adobo", "Price": 4.00, "Stock": 4},
        "P3": {"Name": "Kare-Kare", "Price": 3.00, "Stock": 7},
        "P4": {"Name": "Sisig", "Price": 6.00, "Stock": 5},
        "P5": {"Name": "Pinakbet", "Price": 3.50, "Stock": 3},
        "P6": {"Name": "Bicol Express", "Price": 3.00, "Stock": 8},
        "P7": {"Name": "Laing", "Price": 2.50, "Stock": 6},
    }
}


#Suggestions with Pair
Suggestions = {
    "Ice Coffee": "Dinuguan",
    "Buko Juice": "Pinakbet",
    "Sisig": "Calamansi Juice",
    "Adobo": "Melon Juice",
    "Iskrambol": "Kare-Kare",
    "Buko Pandan Shake": "Laing",
    "Gulaman":"Bicol Express",
    "Dinuguan": "Ice Coffee",
    "Pinakbet": "Buko Juice",
    "Calamansi Juice": "Sisig",
    "Melon Juice": "Adobo",
    "Kare-Kare": "Iskrambol",
    "Laing": "Buko Pandan Shake",
    "Bicol Express": "Gulaman"
}

#This will be used for the list of order that the user will make
Cart = []
total_cost = 0.0

#This display for user to see what choices he/she gets
print("WELCOME TO FILIPINO VENDING PAGKAIN!")

while True:
    print("Select a category:")
    print("1 - Inumin")
    print("2 - Pagkain")
    print("3 - Finish Order <3")
    
    #Choices that the user can make
    choice = input("Enter your choice: ")
    if choice ==  "1":
        user_picked = "Inumin"
    elif choice == "2":
        user_picked = "Pagkain"
    elif choice == "3":
        break
    else:
        print("Invalid Option! Only pick from 1-3") # If user input wrong number
        continue
    
    #Displays the menu for user on its specific choice
    print(f"\n {user_picked} Menu")
    for code, item in Categories[user_picked].items():
        print(f"{code}: {item['Name']} - AED {item['Price']:.2f} | Stock: {item['Stock']}")
    
    #Asks user to input item code like: I1, I2, or D1, D2
    item_code = input("Enter item code: ").upper()
    if item_code not in Categories[user_picked]:
        print("Invalid item Code!") #If user enter wrong input of item code
        continue
    
    #If item runs out after user's order
    item = Categories[user_picked][item_code]
    if item["Stock"] <= 0:
        print("Item is out of stock! :<") #If item runs out when user order again
        continue
    
    #Adds item to the order of user
    Cart.append(item)
    total_cost += item["Price"]
    item["Stock"] -= 1 
    print(f"{item['Name']} added to your order.")
    print(f"Current total:AED {total_cost:.2f}")
    
    #Suggests item for user's choice in each order
    if item["Name"] in Suggestions:
        print(f"Suggestion: Try {Suggestions[item['Name']]}")

#If user mistakenly input an order which in not in the list    
if not Cart:
    print("You did not order.")
    sys.exit()

#Adding the list of user's order    
print("Final Bill:")
for item in Cart:
    print(f"{item['Name']} - AED {item['Price']:.2f}")
print(f"Total Amount:AED {total_cost:.2f}")

#If user input money that is not enough for his/her order
money = float(input("Insert Money:AED "))
if money < total_cost:
    print("Not enough money! Your order has been cancelled.")
    sys.exit()
 
#Final Output
change = money - total_cost
print("Calculating your order...")
print(f"Change returned:AED {change:.2f}")
print("Salamat po and please come again!")