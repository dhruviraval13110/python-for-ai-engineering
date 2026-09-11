"""
Nested if statement example.
"""

age = 22
has_license = True

if age >= 18:
    if has_license:
        print("You can drive.")
    else:
        print("License required.")
else:
    print("Underage.")
