print("Welcome to Fiber Optic Calcualtions")
company_name = input("Company name:")
feet = int(input("Number of feet of Fiber optic cable to be installed:"))

if feet > 500:
    price = feet * .5
elif feet > 250:
    price = feet * .7
elif feet > 100:
    price = feet * .8    
else:
    price = feet * .87

print(f"\nCompany name: {company_name.strip().title()} \nNumber of feet of Fiber optic cable to be installed: {feet} \nCost of install: {price}")
