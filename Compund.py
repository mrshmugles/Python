initialinvestment = float(input("What is the Initial Investment: "))
interestrate = float(input("What is the annualized interest rate: "))
years = 0
goal = initialinvestment * 2

while initialinvestment < goal:
    years = years+1 
    initialinvestment = initialinvestment * (1 + interestrate) 


print (f"\nIt will take {years} years to double your money ending with ${round (initialinvestment, 2)}\n")