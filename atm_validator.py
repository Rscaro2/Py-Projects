# Name: Rishi Scaro, Date: 10/15/2026, Description: This program validates ATP pin numbers and checks if they are valid. 

correct_pin = 5555
attempts = 0

while attempts < 3:
    pin = int(input("Enter your 4-digit PIN: "))

    if pin == correct_pin:
        print("Your PIN is correct.")
        break
    else:
        attempts += 1

        if attempts < 3:
            print("Incorrect PIN. Please try again.")
        else:
            print("Your card is locked.")
   