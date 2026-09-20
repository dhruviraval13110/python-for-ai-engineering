"""Chapter 01: names and objects."""

values = [10, 20]
alias = values
alias.append(30)
copy = values.copy()
copy.append(40)
print("original:", values)
print("copy:", copy)
