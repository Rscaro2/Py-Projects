# Name: Rishi Scaro, Date: 10/08/2026, Description: This script calculates the weekly paycheck for an employee based on how many hours they worked.

hours_worked = float(input("Enter number of hours worked: "))

if (hours_worked <= 40):
    weekly_pay = hours_worked * 20
else: 
    regular_pay = 40 * 20
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * 30
    weekly_pay = regular_pay + overtime_pay

print("Weekly paycheck: $", weekly_pay)

