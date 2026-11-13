# Rishi Scaro, 9/23/26, This script preforms basic math operations. 
import random 
# Generates two random numbers between 1 and 100.
num1 = random.randint(1, 100)
num2 = random.randint(1, 100)

# Performing basic math operations
Addition = num1 + num2
Subtraction = num1 - num2
Multiplication = num1 * num2
Division = num1 / num2
Modulus = num1 % num2
exponentiation = num1 ** num2

print(f"Generated numbers: {num1} and {num2}")
print(f"Addition: {num1} + {num2} = {Addition}")
print(f"Subtraction: {num1} - {num2} = {Subtraction}")
print(f"Multiplication: {num1} * {num2} = {Multiplication}")
print(f"Division: {num1} / {num2} = {Division:.2f}")
print(f"Modulus: {num1} % {num2} = {Modulus}")
print(f"Exponentiation: {num1} ** {num2} = {exponentiation}")

# Explaning the difference between division and modulus
print("Division gives the quotient, while modulus gives the remainder of the division.")