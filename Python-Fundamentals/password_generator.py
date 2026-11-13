# Name: Rishi Scaro, Date: 2026-10-01, Description: This script generates passwords with a given favorite color, a pet’s name, and a number
print()
favorite_color = input("Enter your favorite color: ")
pet_name = input("Enter your pet's name: ")
number = input("Enter a number: ")
print()
print(favorite_color + " " + pet_name + " " + number)
print()

first_password = favorite_color + "_" + pet_name
second_password = number + favorite_color + number

print("Your First Password is: " + first_password) 
print("Your Second Password is: " + number + favorite_color + number) 
print() 

print("Number of characters in " + first_password + ":", len(first_password))
print("Number of characters in " + second_password + ":", len(second_password))
print()
