# Name: Rishi Scaro, Date: 10/08/2026, Description: This program takes a date as input and outputs the date’s season in the northern hemisphere.

month = str(input("Enter the month (e.g., January, February, etc.): "))
day = int(input("Enter the day (1-31): "))

months_31 = ["January", "March", "May", "July", "August", "October", "December"] # (These months have 31 days)
months_30 = ["April", "June", "September", "November"]

if month in months_31: 
    max_days = 31
elif month in months_30:
    max_days = 30
elif month == "February":
    max_days = 28
else: 
    max_days = 0 

if day < 1 or day > max_days: # (Checks if the day is valid for the given month)
    print("Invalid.")
else:
    if month == "March": 
        if day >= 20:
            print("Spring")
        else:
            print("Winter")
    elif month == "June":
        if day >= 21:
            print("Summer")
        else:
            print("Spring")
    elif month == "September":
        if day >= 22:
            print("Fall")
        else:
            print("Summer")
    elif month == "December":
        if day >= 21:
            print("Winter")
        else:
            print("Fall")
    elif month in ["January", "February"]:
        print("Winter")
    elif month in ["April", "May"]:
        print("Spring")
    elif month in ["July", "August"]:
        print("Summer")
    else:
        print("Fall")
