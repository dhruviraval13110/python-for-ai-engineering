"""
Nested Loop Examples
"""

print("Pattern")

for i in range(5):
    for j in range(i + 1):
        print("*", end=" ")
    print()

print("\nCoordinates")

for row in range(3):
    for col in range(3):
        print(f"({row},{col})", end=" ")
    print()
