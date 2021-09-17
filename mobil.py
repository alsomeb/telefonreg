mobilnummer = {}

while True:
    namn = input("Skriv in namn: ")
    if namn.isalpha() == False:
        print("Bara bokstäver är tillåtet!")
        continue #Reset

    while True: #mobilnr check att det är siffror!
        telnr = input(f"Vilket tel-nr har {namn}: ")
        if telnr.isnumeric() == False:
            print("Ange siffror, ej bokstäver!")
            continue #Reset
        else:
            mobilnummer[namn] = telnr
            if len(mobilnummer) == 1:
                break

    print("******Telefon register lookup******")
    while True:
        namn = input("Skriv namn: ")
        if namn.isalpha() == False:
            print("Bara bokstäver tillåtet!")
            continue #Reset

        if namn not in mobilnummer:
            print("Detta namn finns inte i tel register, prova ett annat!")
            continue # reset
        mobilnr = mobilnummer[namn]
        print(f"telefonnr: {telnr}")
        break
    break
