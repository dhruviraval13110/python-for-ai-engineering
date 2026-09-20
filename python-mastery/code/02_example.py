"""Chapter 02: types, identity and conversion."""

raw = "42"
value = int(raw)
print(value, type(value))
print(value == 42, value is (42))  # identity is not value equality
