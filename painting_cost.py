# Name: Rishi Scaro, Date: 2026-10-01, Description: This script Calculates the cost of paint with given dimensions and cost of paint per can. 

wall_height = float(input("Enter the height of the wall in feet: "))
wall_width = float(input("Enter the width of the wall in feet: "))
wall_area =  wall_height * wall_width
cost_per_can = float(input("Enter the cost of paint per can in dollars: "))
print() # Using print() to create a blank line for better readability of the output. 

print(f"Wall area: {wall_area:.1f} sq ft")

paint_needed = wall_area / 350
print(f"Paint needed: {paint_needed:.3f} gallons") 

import math 
cans_needed = math.ceil(paint_needed) 
print(f"Cans needed: {cans_needed} can(s)")
print()

paint_cost = cans_needed * cost_per_can
sales_tax = paint_cost * 0.07
total_cost = paint_cost + sales_tax

print(f"Paint cost: ${paint_cost:.2f}")
print(f"Sales tax: ${sales_tax:.2f}")
print(f"Total cost: ${total_cost:.2f}")
print()
