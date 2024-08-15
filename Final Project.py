# Final Project
# Date Created: April 6th, 2023
# Date last modified: April 10th, 2023
# This program is designed to be used in an insurance company
# It will take the clients personal info, then the car's info,ask the client some questions to add possible discounts.
# Finally, it will print and display the quote on the screen and print it to a separate file to email it to the client

# Defining Functions
def basePrice():
    base = 500
    return base


def fullCover():
    base = 500
    return base


def oneWay():
    base = basePrice() - 150
    return base


def winterDisc():
    discount = basePrice() * 0.15
    return discount


def familyDisc():
    discount = basePrice() * 0.05
    return discount


def gDisc():
    discount = basePrice() * 0.25
    return discount


def ageDisc():
    discount = basePrice() * 0.10
    return discount


def tax():
    cost = basePrice() * 0.13
    return cost


# Welcoming Message
print("Welcome to Belairdircet Insurance")
print("We guarantee the best insurance prices nationwide")
print("Lets start off by some personal info to create your file\n")

# Client Name
clientName = {'firstName': input("First Name: "),
              'lastName': input("Last Name: ")}

# Client Address
print("\nPLease enter your address below")
clientAddress = {"streetNum": input("Street number: "),
                 "streetName": input("Street Name: "),
                 "unitNumber": input("Unit number: "),
                 "city": input("City: "),
                 "province": input("Province: "),
                 "postalCode": input("Postal Code: "),
                 "phoneNum": input("Phone number: ")}

# Vehicle Info
print("\nPLease enter your vehicle's information below")
carInfo = {"make": input("Make: "),
           "model": input("Model: "),
           "production year": input("Production Year: "),
           "milage": input("Milage: "),
           "doors": input("Number of Doors: "),
           "vin": input("VIN Number: ")}

# Policy Type
while True:
    print("\n1. Full Coverage")
    print("2. One Way Coverage")
    try:
        coverageType = int(input("Please select the coverage type you are looking to get: "))

        if coverageType == 1 or coverageType == 2:
            break
        print("\nPlease try again by selecting a valid option.\n")
    except ValueError:
        print("\nPlease try again by selecting a valid option.\n")

print("\n Next, we will go over some details and try to give you some discounts")

# Winter Tires Check
while True:
    winterTires = input("\nDo you have winter tires (Y: Yes / N: No): ")
    while not (winterTires.capitalize() == "Y" or winterTires.capitalize() == "N"):
        winterTires = input("\nTry again by selecting a valid option: Y/N:  ")
    if winterTires.capitalize() == "Y":
        print("\nA 10% Discount will be applied to your price")
    break

# Family Discount
while True:
    familyDiscount = input("\nDo you have any family members insured with Belairdirect (Y: Yes / N: No): ")
    while not (familyDiscount.capitalize() == "Y" or familyDiscount.capitalize() == "N"):
        familyDiscount = input("\nTry again by selecting a valid option: Y/N:  ")
    if winterTires.capitalize() == "Y":
        print("\nA 5% Discount will be applied to your price")
    break

# G License Discount
while True:
    gLicense = input("\nDo you have your G License (Y: Yes / N: No): ")
    while not (gLicense.capitalize() == "Y" or gLicense.capitalize() == "N"):
        gLicense = input("\nTry again by selecting a valid option: Y/N:  ")
    if gLicense.capitalize() == "Y":
        print("\nA 20% Discount will be applied to your price")
    break

# Age Discount
while True:
    try:
        age = int(input("\nHow old are you: "))
        if age < 16:
            print("Were sorry! You are too young to drive")
            break
        elif 16 <= age <= 25:
            break
        elif age > 25:
            print("\n A 5% Discount will be applied to your price\n")
            break
    except ValueError:
        print("\nPlease try again by selecting a valid option.\n")

# Final Email
with open('quote.txt', 'wt') as quote:
    # Customer Name
    print("\n\n\n\n\t\t\t   ", clientName["firstName"], clientName['lastName'])
    quote.write("\n\n\n\n\t\t\t   " + clientName["firstName"] + " " + clientName['lastName'])

    # Customer Phone Number
    print("\t\t\t\t", clientAddress["phoneNum"])
    quote.write("\t\t\t\t" + clientAddress["phoneNum"])

    # Customer Address
    print("\t\t\t  ", clientAddress["unitNumber"], "-", clientAddress["streetNum"],
          clientAddress["streetName"])
    print("\t\t\t", clientAddress["city"], clientAddress["province"], clientAddress["postalCode"])
    quote.write(
        "\t\t\t  " + clientAddress["unitNumber"] + "-" + clientAddress["streetNum"] + " " + clientAddress[
            "streetName"])
    quote.write("\t\t\t" + clientAddress["city"] + " " + clientAddress["province"] + " " + clientAddress[
        "postalCode"])

    # Vehicle Info
    print(carInfo["production year"], "-", carInfo["make"], carInfo["model"])
    print("Milage: ", carInfo["milage"], "\nNumber of doors: ", carInfo["doors"], "\nVIN Number: ", carInfo["vin"])
    quote.write(carInfo["production year"] + "-" + carInfo["make"] + " " + carInfo["model"])
    quote.write("Milage: " + carInfo["milage"] + "\nNumber of Doors: " + carInfo["doors"] + "\nVIN Number: " +
                carInfo["vin"])

    # Quote Price
    # Base Price
    print("\n Monthly Payment Summary:\n")
    if coverageType == 1:
        print("Base Price: \t\t$", basePrice())
        quote.write("Base Price: \t\t$ 500")
        quotePrice = basePrice()
    if coverageType == 2:
        print("Base Price: \t\t$", oneWay())
        quote.write("Base Price: \t\t$ 350")
        quotePrice = oneWay()
    # Winter Tire Discount
    if winterTires.capitalize() == "Y":
        print(f"Winter Tire Discount: \t\t$", "{0:.2f}".format(winterDisc()))
        quote.write("Winter Tire Discount: \t\t$" + "{0:.2f}".format(winterDisc()))
        totalAW = quotePrice - winterDisc()

    # Family Discount:
    if familyDiscount.capitalize() == "Y":
        print("Family Discount: \t\t$", "{0:.2f}".format(familyDisc()))
        quote.write("Family Discount: \t\t$" + "{0:.2f}".format(familyDisc()))
        totalAF = totalAW - familyDisc()

    # G License discount
    if gLicense.capitalize() == "Y":
        print("G License Discount Discount: \t\t$", "{0:.2f}".format(gDisc()))
        quote.write("G License Discount: \t\t$" + "{0:.2f}".format(gDisc()))
        totalAG = totalAF - gDisc()

    # Age Discount
    if age > 25:
        print("Age Discount: \t\t$", "{0:.2f}".format(ageDisc()))
        quote.write("Age Discount: \t\t$" + "{0:.2f}".format(ageDisc()))

        totalAA = totalAG - ageDisc()
    # Tax
    print("Tax: \t\t$", "{0:.2f}".format(tax()))
    quote.write("Tax: \t\t$" + "{0:.2f}".format(tax()))
    totalAT = totalAA + tax()

    # Final Calculation
    print("Your total insurance monthly payment on the ", carInfo["production year"], carInfo["make"], carInfo["model"],
          " will be: $", totalAT)
    quote.write("Your total insurance monthly payment on the " + carInfo["production year"] + carInfo["make"] +
                carInfo["model"] + " will be: $" + "{0:.2f}".format(totalAT))
    print("\t\tThanks for contacting Belairdirect")
