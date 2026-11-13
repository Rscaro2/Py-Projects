# Name: Rishi Scaro, Date: 2025-10-01, Description: This script generates usernames based on given first name, last name, and ID number. 

first_name = input("Enter your first name: ") 
last_name = input("Enter your last name: ")
idNumber = input("Enter your ID number: ")

print(f"The student's login name is: {first_name[0:3]}{last_name[0:3]}{idNumber[-3:]}")

# [0:3] means the first three letters of the first and last name, and [-3:] means the last three digits of the ID number.
