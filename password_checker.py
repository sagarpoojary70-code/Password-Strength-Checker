
import string

print("======================================")
print("       PASSWORD STRENGTH CHECKER")
print("======================================")

password = input("Enter your password: ")

# Check password criteria
length = len(password) >= 8
uppercase = any(char.isupper() for char in password)
lowercase = any(char.islower() for char in password)
digit = any(char.isdigit() for char in password)
special = any(char in string.punctuation for char in password)

# Count satisfied criteria
score = sum([length, uppercase, lowercase, digit, special])

print("\n========== SECURITY REPORT ==========")

print("Password Length:", length)
print("Uppercase Letters:", uppercase)
print("Lowercase Letters:", lowercase)
print("Numbers:", digit)
print("Special Characters:", special)

# Classify password strength
if len(password) < 8 or score <= 2:
    print("\nPASSWORD STRENGTH: WEAK")

elif score == 3 or score == 4:
    print("\nPASSWORD STRENGTH: MODERATE")

else:
    print("\nPASSWORD STRENGTH: STRONG")

# Give suggestions
print("\n========== SUGGESTIONS ==============")

if not length:
    print("- Use at least 8 characters.")

if not uppercase:
    print("- Add an uppercase letter.")

if not lowercase:
    print("- Add a lowercase letter.")

if not digit:
    print("- Add a number.")

if not special:
    print("- Add a special character.")

if score == 5 and len(password) >= 8:
    print("Great! All basic password rules are satisfied.")

print("======================================")