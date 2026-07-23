"""
Break
Continue
Pass
"""

print("Break Example")

for i in range(10):

    if i == 5:
        break

    print(i)

print("\nContinue Example")

for i in range(10):

    if i % 2 == 0:
        continue

    print(i)

print("\nPass Example")

for i in range(5):

    if i == 2:
        pass

    print(i)
