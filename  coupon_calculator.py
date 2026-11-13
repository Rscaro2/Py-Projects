# Name: Rishi Scaro, Date: 10/08/2026, Description: This program calculates supermarket coupon values based on customer spending amounts. 

total_cost = float(input("Please enter the cost of your groceries:: $"))

if total_cost < 10: 
    print("You do not qualify for a discount coupon.")
elif total_cost >= 10 and total_cost <= 60:
    percentage = 8
    coupon_value = total_cost * 0.08 
elif total_cost > 60 and total_cost <= 150:
    percentage = 10
    coupon_value = total_cost * 0.10
elif total_cost > 150 and total_cost <= 210:
    percentage = 12
    coupon_value = total_cost * 0.12
else:
    percentage = 14
    coupon_value = total_cost * 0.14

if total_cost >= 10:
    print(f"You win a discount coupon of ${coupon_value:.2f} ({percentage}% of your purchase)")
