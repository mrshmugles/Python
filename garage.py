class Vehicle:

    choices = {
        "1": "power mirrors", 
        "2": "power locks", 
        "3": "remote start", 
        "4": "backup camera", 
        "5": "bluetooth", 
        "6": "cruise control", 
        "7": "heated seats", 
        "8": "cup holders",
        "9": "Done picking options"
    }

    def __init__(self, type):
        self.make = input("\nWhat is the make of your " + type + "? ")
        self.model = input("\nWhat is the model of your " + type + "? ")
        self.color = input("\nWhat is the color of your " + type + "? ")
        self.fueltype = input("\nWhat is the fuel type of your " + type + "? ")
        self.options = []

        choice = ""

        while choice != "9" or len(self.options) == 0:
            if (len(self.options) == 8):
                break

            print("\nWhat options would you like for your " + type + "?")

            for key in sorted(self.choices.keys()):
                if key not in self.options:
                    print(key + ": " + self.choices[key])

            choice = input()

            if choice == "9":
                if len(self.options) < 1:
                    print("\nYou must pick at least 1 option.")
                else:
                    break

            if choice not in self.choices.keys():
                print("\n" + choice + " is not an option.")    
            elif choice in self.options:
                print("\n" + choice + ": " + self.choices[choice] + " was already picked.")
            elif choice != "9":
                self.options.append(choice)

    def output(self):
        picked = ""

        for key in range(len(self.options)):
            picked = picked + self.choices[self.options[key]]

            if key < len(self.options) - 1:
                picked = picked + ", "
                
        print(f"The make is {self.make}.")
        print(f"The model is {self.model}.")
        print(f"The color is {self.color}.")
        print(f"The fuel type is {self.fueltype}.")
        print(f"the additional options selected are: {picked}")

    def getMake(self):
        print(self.make)

    def getModel(self):
        print(self.model)

    def getColor(self):
        print(self.color)

    def getFueltype(self):
        print(self.fueltype)

    def getOptions(self):
        print(self.options)

class Car(Vehicle):
    def __init__(self):
        Vehicle.__init__(self, "car")
        self.enginesize = input("\nWhat is the engine size of the car? ")
        self.numdoors = 0

        while self.numdoors <= 0:
            try:
                ans = input("\nHow many doors does your car have? ")
                ans = int(ans)

                if ans> 0 :
                    self.numdoors = ans
                else:
                    print("\nYou must have more than 0 doors.")
            except:
                print("\n" + ans + " is not an integer")

    def output(self):
        Vehicle.output(self)
        print(f"The engine size is {self.enginesize}.")
        print(f"The car has {self.numdoors} doors.")

    def getenginesize(self):
        print(self.enginesize)

    def getnumdoors(self):
        print(self.numdoors)

class Pickup(Vehicle):
    def __init__(self):
        Vehicle.__init__(self, "pickup")
        self.cabstyle = input("\nWhat is the cab style of your pickup? ")
        self.bedlength = 0

        while self.bedlength <= 0:
            try:
                ans = input("\nHow long is the bed of your pickup? ")
                ans = float(ans)

                if ans > 0 :
                    self.bedlength = ans
                else:
                    print("\nYour bed length must be longer than 0.")
            except:
                print("\n" + ans + " is not a number")

    def output(self):
        Vehicle.output(self)
        print(f"The cab style is {self.cabstyle}.")
        print(f"The bed length of the pickup is {self.bedlength}.")

    def getcabstyle(self):
        print(self.cabstyle)

    def getbedlength(self):
        print(self.bedlength)

def getchoice():
    menu ={
        "1": "Car",
        "2": "Pickup"
    }

    choice = ""

    while choice not in menu.keys():
        print("\nPick an option.")

        for key in sorted(menu.keys()):
            print(key + ": " + menu[key])

        choice = input()

        if choice not in menu.keys():
            print(f"\n{choice} is not valid.")

    if choice =="1":
        return Car()
    elif choice == "2":
        return Pickup()        

done = False
garage = []

while not done:
    choice = input("\nWould you like to add a vehical to your garage?\n(Must have at least 1 car and 1 pickup)\nY/N\n ")

    if choice.upper() == "Y":
        garage.append(getchoice())
    elif choice.upper() == "N":
        cars = 0
        pickup = 0

        if len(garage) == 0:
            print("\nYou must have at least 1 car and 1 pickup in your garage.")
        else:
            for idx in range(len(garage)):
                if isinstance(garage[idx], Car):
                    cars += 1
                elif isinstance(garage[idx], Pickup):
                    pickup += 1

            if cars == 0 or pickup == 0:
                print("\nYou must have at least 1 car and 1 pickup in your garage.")
            else:
                done = True

for idx in range(len(garage)):
    if isinstance(garage[idx], Car):
        print(f"Your {idx + 1} car's info:")
    elif isinstance(garage[idx], Pickup):
        print(f"Your {idx + 1} pickup's info:")

    garage[idx].output()

    if idx < len(garage) - 1:
        print()