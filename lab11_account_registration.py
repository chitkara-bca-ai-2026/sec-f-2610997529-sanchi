
username = input("Enter your username: ")
password = input("Enter your password: ")

length_check = len(password) >= 8
digit_check = any(ch.isdigit() for ch in password)
uppercase_check = any(ch.isupper() for ch in password)

print("\n================================")
print("      PASSWORD VALIDATION REPORT")
print("================================")

print("Username:", username)
print("Password:", "*" * len(password))

print("\n--- Validation Rules ---")

if length_check:
    print("[PASS] Minimum 8 characters")
else:
    print("[FAIL] Minimum 8 characters")

if digit_check:
    print("[PASS] At least one digit")
else:
    print("[FAIL] At least one digit")

if uppercase_check:
    print("[PASS] At least one uppercase letter")
else:
    print("[FAIL] At least one uppercase letter")

if length_check and digit_check and uppercase_check:
    print("\nPassword is VALID!")
    print("Account created successfully for", username)
else:
    print("\nPassword is INVALID.")