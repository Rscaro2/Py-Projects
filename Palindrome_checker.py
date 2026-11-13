# Name: Rishi Scaro, Date: 11/05/2026, Description: This program checks if a given word or phrase is a palindrome.

user_string = input("Enter a word or phrase: ")


original_string = user_string.replace(" ", "")


reversed_string = original_string[::-1]


if original_string == reversed_string:
    print(f"'{user_string}' is a palindrome!")
else:
    print(f"'{user_string}' is not a palindrome.")


print(f"Original string: {original_string}")
print(f"Reversed string: {reversed_string}")