# 1. Prompt the user to input a value, until user enters some value.
while True:
    user_input = input("Enter a value (type 'quit' to terminate): ")
    if user_input.lower() == 'quit':
        print("Exiting program...")
        break
    else:
        print("entered:", user_input)

# 2. From the string "Monty Python's Flying Circus", display the words along with its length.
string = "Monty Python's Flying Circus"
words = string.split()

for word in words:
    print(f"{word}: {len(word)}")

# 3.Prompt the user to input any numbers between 1 and 9. If User enters any other number, prompt 
# the user to input again. If the user enters the valid number, display the below two patterns.

while True:
    try:
        num = int(input("Enter a number between 1 and 9: "))
        if 1 <= num <= 9:
            break
        else:
            print("Please enter a number between 1 and 9.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# first pattern
for i in range(1, num + 1):
    for j in range(i):
        print(i, end=" ")
    print()

print()

# second pattern
for i in range(1, num + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# 4. Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 
# 1500 and 2700 (both included).
numbers = [num for num in range(1500, 2701) if num % 7 == 0 and num % 5 == 0]
print(numbers)

# 5. Write a Python program that accepts a word from the user and reverse it.
word = input("Enter a word: ")
reversed_word = word[::-1]
print("Reversed word:", reversed_word)

# 6. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
for num in range(7):
    if num != 3 and num != 6:
        print(num)
# 7. Write a Python Script to validate the mobile number provided by the user.
def validate_mobile_number(number):
    if len(number) != 10:
        return False
    if number[0] not in ['5', '6', '7', '8', '9']:
        return False
    if not number.isdigit():
        return False
    return True

def check_phone():
    mobile_number = input("Enter your mobile number: ")
    if validate_mobile_number(mobile_number):
        print("Valid mobile number.")
    else:
        print("Invalid mobile number. Please enter a 10-digit number...")

check_phone()

# 8. Write a Python Script to accept two strings from the user and concatenate the strings. Make sure 
# you have entered only strings.
def concatenate_strings(str1, str2):
    if isinstance(str1, str) and isinstance(str2, str):
        return str1 + str2
    else:
        return "Please enter valid strings."

def main():
    string1 = input("Enter the first string: ")
    string2 = input("Enter the second string: ")
    result = concatenate_strings(string1, string2)
    print("Concatenated string:", result)

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
result = concatenate_strings(string1, string2)
print("Concatenated string:", result)

# 9. Write a Python Script to get the number from the user. The number entered should be between 
# 1 and 500.
def get_number():
    while True:
        try:
            number = int(input("Enter a number between 1 and 500: "))
            if 1 <= number <= 500:
                return number
            else:
                print("Number must be between 1 and 500. Try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

number = get_number()
print("You entered:", number)

# 10. Write a Python Script that accepts the string from the user. Remove the vowels from the string 
# entered and have only the consonants.
def remove_vowels(string):
    vowels = 'aeiouAEIOU'
    return ''.join(char for char in string if char not in vowels)

user_string = input("Enter a string: ")
result = remove_vowels(user_string)
print("String without vowels:", result)
