"""Chapter 03: expressions."""

def eligible(age: int, verified: bool) -> bool:
    return age >= 18 and verified

for age, verified in [(20, True), (17, True), (20, False)]:
    print(eligible(age, verified))
