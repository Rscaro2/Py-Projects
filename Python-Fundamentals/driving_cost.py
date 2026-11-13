# Rishi Scaro, 09/23/26, This script calculates driving costs. 
mpg = float(input("What is your car's miles per gallon? "))
gas_price = float(input("What is the price of gas per gallon? "))

distance1 = 20
distance2 = 75
distance3 = 500 

cost1 = (distance1/ mpg) * gas_price
cost2 = (distance2 / mpg) * gas_price
cost3 = (distance3 / mpg) * gas_price

print(f"The cost of driving 20 miles is:  ${cost1:.2f}")
print(f"The cost of driving 75 miles is:  ${cost2:.2f}")
print(f"The cost of driving 500 miles is: ${cost3:.2f}")