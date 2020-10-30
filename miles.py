while True:
    try:
        miles = float(input("Number of miles driven:"))
    except:
        print("You must enter a number")
        continue
    else:
        break

def math():
            mtkconversion = 1.60934
            kilometers = miles * mtkconversion
            print(f"\nMiles driven: {miles} \nKilometers driven: {kilometers}")

math()