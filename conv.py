#!/usr/bin/python

menu = {
    '1': "Binary",
    '2': "Hex",
    '3': "Decimal",
    '4': "Exit"
}

while True:
    options = menu.keys()

    print("Convert From?")
    for entry in options:
        print entry, menu[entry]

    selection = raw_input("Please Select:")
    if selection == '1':
        menuB = {
            '1': "Hex",
            '2': "Decimal"
        }
        optionsB = menuB.keys()

        print("Convert To:")
        for entryB in optionsB:
            print entryB, menuB[entryB]

        selectionB = raw_input("Please Select:")

        if selectionB == "1":
            selectionBH = raw_input("Enter your number:")
            print(hex(int(selectionBH, 2)))
            break
        elif selectionB == "2":
            selectionBD = raw_input("Enter your number:")
            print(int(selectionBD, 2))
            break
        else:
            print("Not a valid choice, please try again")

    elif selection == '2':
        menuH = {
            '1': "Binary",
            '2': "Decimal"
        }
        optionsH = menuH.keys()

        print("Convert To:")
        for entryH in optionsH:
            print entryH, menuH[entryH]

        selectionH = raw_input("Please Select:")

        if selectionH == "1":
            selectionHB = raw_input("Enter your number:")
            # Hex to binary
            break
        elif selectionH == "2":
            selectionHD = raw_input("Enter your number:")
            # hex to decimal
            break
        else:
            print("Not a valid choice, please try again")

    elif selection == '3':
        print "find"
    elif selection == '4':
        break
    else:
        print "Unknown Option Selected!"
