"""
Input validation examples.
"""

username = "admin"
password = "python123"

if username == "admin" and password == "python123":
    print("Login Successful")
else:
    print("Invalid Credentials")


age = 16

if age < 0:
    print("Invalid age")
elif age >= 18:
    print("Adult")
else:
    print("Minor")
