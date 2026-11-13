# Name: Rishi Scaro, Date: 10/29/2026, Description: This program simulates basic password validation, strength scoring, and breach simulation.

def validate_password(password): 
    has_length = len(password) >= 8 
    has_uppercase = any(char.isupper() for char in password) 
    has_lowercase = any(char.islower() for char in password) 
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in "!@#$%^&*" for char in password)
    return (has_length and has_uppercase and has_lowercase and has_digit and has_special) 

def score_password(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if any(char.isupper() for char in password):
        score += 1
    if any(char.islower() for char in password):
        score += 1
    if any(char.isdigit() for char in password): 
        score += 1 
    if any(char in "!@#$%^&*" for char in password):
        score += 1 
    if score <= 2:
        strength_label = "Weak" 
    elif score <= 4:
        strength_label = "Moderate"
    else:
        strength_label = "Strong"
    return score, strength_label

breached_passwords = ["123456", "password", "letmein", "qwerty", "admin"]

def check_breach(password): 
    if password in breached_passwords: 
        return "Compromised"
    else: 
        return "Safe"


user_passwords = [
   	 "P@ssword123", "123456", "helloWorld", "Passw0rd!",
   	 "admin", "Secure2024#", "guest", "MyPass!",
    	"Qwerty123", "letmein"
]

print("Password Audit Report")
print("=" * 40)

for password in user_passwords:
     valid = validate_password(password)
     score, strength_label = score_password(password)
     breach_status = check_breach(password)
     print("\nPassword:", password)
     print("Valid:", valid)
     print(f"Strength: {strength_label} ({score}/5)")
     print("Breach Status:", breach_status)
     print("-" * 40)


