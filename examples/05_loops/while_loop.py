"""
Python While Loop Examples
"""

count = 1

while count <= 5:
    print(count)
    count += 1

print("\nCountdown")

num = 5

while num > 0:
    print(num)
    num -= 1

print("Blast Off 🚀")

# Infinite Loop Example
# while True:
#     print("Press Ctrl+C to stop")

password = ""

while password != "python":
    password = input("Enter password: ")

print("Access Granted")
