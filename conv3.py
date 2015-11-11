#!/usr/bin/python

import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    menu = {
        '1': "Binary",
        '2': "Hex",
        '3': "Decimal",
        '4': "Exit"
    }
    options = list(menu.keys())
    options.sort()

    print("Convert From?")
    for entry in options:
        print(entry, menu[entry])

    selection = input("Please Select:")
    if selection == '1':
        menuB = {
            '1': "Hex",
            '2': "Decimal"
        }
        optionsB = list(menuB.keys())
        optionsB.sort()

        print("Convert To:")
        for entryB in optionsB:
            print(entryB, menuB[entryB])

        selectionB = input("Please Select:")

        if selectionB == "1":
            # Binary to hex
            selectionBH = input("Enter your number:")
            print(hex(int(selectionBH, 2))[2:])
            break
        elif selectionB == "2":
            # Binary to decimal
            selectionBD = input("Enter your number:")
            print(int(selectionBD, 2))
            break
        else:
            cls()
            print("Not a valid choice, please try again \n")

    elif selection == '2':
        menuH = {
            '1': "Binary",
            '2': "Decimal"
        }
        optionsH = list(menuH.keys())
        optionsH.sort()

        print("Convert To:")
        for entryH in optionsH:
            print(entryH, menuH[entryH])

        selectionH = input("Please Select:")

        if selectionH == "1":
            selectionHB = input("Enter your number:")
            # Hex to binary
            print(bin(int(selectionHB, 16))[2:])
            break
        elif selectionH == "2":
            selectionHD = input("Enter your number:")
            # hex to decimal
            print(int(selectionHD, 16))
            break
        else:
            cls()
            print("Not a valid choice, please try again \n")

    elif selection == '3':
        menuD = {
            '1': "Binary",
            '2': "Hex"
        }
        optionsD = list(menuD.keys())
        optionsD.sort()

        print("Convert To:")
        for entryD in optionsD:
            print(entryD, menuD[entryD])

        selectionD = input("Please Select:")

        if selectionD == "1":
            selectionD = input("Enter your number:")
            # Decimal to binary
            print(bin(int(selectionD, 10))[2:])
            break
        elif selectionD == "2":
            selectionDH = input("Enter your number:")
            # Decimal to hex
            print(hex(int(selectionDH, 10))[2:])
            break
        else:
            cls()
            print("Not a valid choice, please try again \n")

    elif selection == '4':
        break
    else:
        cls()
        print("Unknown Option Selected! \n")
