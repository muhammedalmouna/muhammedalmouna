# Assignment 3
# Date Created: March 28th, 2023
# Last modified: April 1st, 2023
# This program is the cashier's system in the restaurant, it will be taking customer's info, then customer's order, and
# finally printing the receipt for the customer after calculating the total with taxes and any applicable discounts


# Step 1: creating functions
def mealCost():
    cost = mealPrice[mealOrder] * quantity
    return cost


def discount1():
    discount = mealCost() * 0.15
    return discount


def discount2():
    discount = mealCost() * 0.20
    return discount


def discount3():
    discount = mealCost() * 0.25
    return discount


def studentDiscount():
    discount = mealCost() * 0.10
    return discount


def tip1():
    tip = mealCost() * 0.10
    return tip


def tip2():
    tip = mealCost() * 0.15
    return tip


def tip3():
    tip = mealCost() * 0.20
    return tip


def tip4():
    tip = 0
    return tip


def deliveryFee():
    cost = 5
    return cost


def tax():
    cost = mealCost() * 0.13
    return cost


# Creating Dictionaries
mealPrice = {1: 15,
             2: 20,
             3: 25,
             4: 7,
             5: 12,
             6: 16}

# Welcoming Display
print("\n\t\tWelcome to Arnold's Amazing Eats II")
print("\nPlease enter your first and last name below")

customerName = {'firstName': input("First Name: "),
                'lastName': input("Last Name: ")}

# Step 2: Taking the customer's address and any notes.
print("\nPLease enter your address below")
customerAddress = {"streetNum": input("Street number: "),
                   "streetName": input("Street Name: "),
                   "unitNumber": input("Unit number: "),
                   "city": input("City: "),
                   "province": input("Province: "),
                   "postalCode": input("Postal Code: "),
                   "Instructions": input("Would you like to add any instructions for deliveries from this address: "),
                   "phoneNum": input("Phone number: ")}

# Displaying the menu
print("\nPLease Select a meal from the menu below\n")
print("1. Chicken Shawarma      \t $15")
print("2. Beef Shawarma      \t 	 $20")
print("3. Poutine Shawarma \t	 $25")
print("4. Chicken Wings      \t 	 $07")
print("5. Rice Chicken      	\t $12")
print("6. Rice Beef         	\t $16")

orderMenu = {1: "Chicken Shawarma",
             2: "Beef Shawarma",
             3: "Poutine Shawarma",
             4: "Chicken Wings",
             5: "Rice Chicken",
             6: "Rice Beef"}

# Taking Order
while True:
    try:
        mealOrder = int(input("\nWhat would you like to order: "))
        if 1 <= mealOrder <= 6:
            break
        print("Please try again by selecting a valid option")
    except ValueError:
        print("Please try again by selecting a valid option")
while True:
    try:
        quantity = int(input("\nHow many meals would you like to order: "))
        if 1 <= quantity:
            break
        print("Please try again by choosing at least One meal")
    except ValueError:
        print("Please try again by selecting a valid option")

# Confirming Order
print("\nYour order is", quantity, "meals of", orderMenu[mealOrder])
confirm = input("\nCan you please confirm your order: Y/N:   ")
while not (confirm.capitalize() == "Y" or confirm.capitalize() == "N"):
    confirm = input("Try again by selecting a valid option: Y/N:   ")
    if confirm.capitalize() == "N":
        print("Re run the program to start over")
else:
    print("\nThank you for confirming your order! Your order will be ready soon!")

# Student discount:
student = input("\nAre you a student: Y/N:  ")
while not (student.capitalize() == "Y" or student.capitalize() == "N"):
    student = input("Try again by selecting a valid option: Y/N:  ")
if student.capitalize() == "Y":
    print("\nYou will be getting a %10 Discount!")

# Delivery
delivery = input("\nWould you like your order delivered: Y/N:  ")
while not (delivery.capitalize() == "Y" or delivery.capitalize() == "N"):
    delivery = input("Try again by selecting a valid option: Y/N:  ")
if delivery.capitalize() == "Y":
    print("\nDelivery fee will be $5")
while True:  # Tip
    try:
        if delivery.capitalize() == "Y":
            tip = int(input("\nTip\n1. %10\n2. %15\n3. %20\n4. Skip\nPlease Select an option: "))
            if 1 <= tip <= 4:
                break
        elif delivery.capitalize() == "N":
            tip = 0
            break
        print("Try again by choosing a valid option")
    except ValueError:
        print("Please try again by selecting a valid option")

# Order Nested Dictionary
orderSum = {"Meal Order:": mealOrder, "Meal Price: ": mealPrice, "Quantity: ": quantity}

# Receipt
with open('receipt.txt', 'wt') as receipt:
    # Customer Name
    print("\n\n\n\n\t\t\t   ", customerName["firstName"], customerName['lastName'])
    receipt.write("\n\n\n\n\t\t\t   " + customerName["firstName"] + " " + customerName['lastName'])

    # Customer Phone Number
    print("\t\t\t\t", customerAddress["phoneNum"])
    receipt.write("\t\t\t\t" + customerAddress["phoneNum"])

    # Customer Address (if applicable):
    if delivery.capitalize() == "Y":
        print("\t\t\t  ", customerAddress["unitNumber"], "-", customerAddress["streetNum"],
              customerAddress["streetName"])
        print("\t\t\t", customerAddress["city"], customerAddress["province"], customerAddress["postalCode"])
        receipt.write(
            "\t\t\t  " + customerAddress["unitNumber"] + "-" + customerAddress["streetNum"] + " " + customerAddress[
                "streetName"])
        receipt.write("\t\t\t" + customerAddress["city"] + " " + customerAddress["province"] + " " + customerAddress[
            "postalCode"])

    # Delivery Instructions
    print("\t\t\t\t", customerAddress["Instructions"])

    # Order Summary
    print("\n\n\n Order", "\t\t\t", "", "\t\t Quantity", "\t\t\t", "   ", "Total\n\n", orderMenu[mealOrder], "\t \t\t",
          quantity, "\t \t \t \t \t", "$", mealCost())
    receipt.write("\n\n\n Order" + "\t\t\t" + "" + "\t\t Quantity" + "\t\t\t" + "   " + "Total\n\n" + " " + orderMenu[
        mealOrder] + "\t \t\t" + str(quantity) + "\t \t \t \t \t" + "$" + str(mealCost()))

    # Discount
    if 1 < mealCost() < 100:
        print(" Discount\t\t\t\t  \t\t\t\t\t   - $", "{0:.2f}".format(discount1()))
        receipt.write(" Discount\t\t\t\t  \t\t\t\t\t   - $" + "{0:.2f}".format(discount1()))
        totalAD = mealCost() - discount1()
    elif 100 < mealCost() < 500:
        print(" Discount\t\t\t\t\t\t\t\t\t   - $", "{0:.2f}".format(discount2()))
        receipt.write(" Discount\t\t\t\t\t\t\t\t\t   - $" + "{0:.2f}".format(discount2()))
        totalAD = mealCost() - discount2()
    elif mealCost() > 500:
        print(" Discount\t\t\t\t\t\t\t\t\t   - $", "{0:.2f}".format(discount3()))
        receipt.write(" Discount\t\t\t\t\t\t\t\t\t   - $" + "{0:.2f}".format(discount3()))
        totalAD = mealCost() - discount3()

    # Student Discount
    if student.capitalize() == "Y":
        totalASD = totalAD - studentDiscount()
        print(" Student Discount", "\t\t\t\t\t\t", " ", "    -", "$", "{0:.2f}".format(studentDiscount()))
        receipt.write(" Student Discount" + "\t\t\t\t\t\t" + " " + "    -" + "$" + "{0:.2f}".format(studentDiscount()))
    if student.capitalize() == "N":
        totalASD = totalAD

    # Delivery
    if delivery.capitalize() == "Y":
        print(" Delivery fee\t\t\t\t\t\t\t\t\t", "$", "{0:.2f}".format(deliveryFee()))
        receipt.write(" Delivery fee\t\t\t\t\t\t\t\t\t" + "$" + "{0:.2f}".format(deliveryFee()))
        totalAFD = totalASD + 5

        # Tip
        if tip == 1:
            print(" Tip\t\t\t\t\t\t\t\t\t\t     $", "{0:.2f}".format(tip1()))
            receipt.write(" Tip\t\t\t\t\t\t\t\t\t\t     $" + "{0:.2f}".format(tip1()))
            totalAT = totalAFD + tip1()
        if tip == 2:
            print(" Tip\t\t\t\t\t\t\t\t\t\t     $", "{0:.2f}".format(tip2()))
            receipt.write(" Tip\t\t\t\t\t\t\t\t\t\t     $" + "{0:.2f}".format(tip2()))
            totalAT = totalAFD + tip2()
        if tip == 3:
            print(" Tip   \t\t\t\t\t\t\t\t\t\t     $", "{0:.2f}".format(tip3()))
            receipt.write(" Tip\t\t\t\t\t\t\t\t\t\t     $" + "{0:.2f}".format(tip3()))
            totalAT = totalAFD + tip3()
        if tip == 4:
            totalAT = totalAFD
    if delivery.capitalize() == "N":
        totalAFD = totalASD
        totalAT = totalAFD + tip4()

    # TAX
    print(" HST\t\t\t\t\t\t\t\t\t\t     $", "{0:.2f}".format(tax()))
    receipt.write(" HST\t\t\t\t\t\t\t\t\t\t     $" + "{0:.2f}".format(tax()))
    total = totalAT + tax()

    # Total amount
    print(" Total\t\t\t\t\t\t\t\t\t\t\t $", "{0:.2f}".format(total))
    receipt.write(" Total\t\t\t\t\t\t\t\t\t\t\t $" + "{0:.2f}".format(total))

    # Goodbye Message
    print("\n Thanks for visiting Arnold's Amazing Eats II\n\t\t\t\tVisit Us Soon")
    receipt.write("\n Thanks for visiting Arnold's Amazing Eats II\n\t\t\t\tVisit Us Soon")