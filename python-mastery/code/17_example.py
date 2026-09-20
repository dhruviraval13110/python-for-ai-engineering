"""Chapter 17: exploratory visualization."""

import matplotlib.pyplot as plt

values = [10, 14, 13, 19, 22]
plt.plot(values, marker="o")
plt.title("Example trend")
plt.xlabel("Observation")
plt.ylabel("Value")
plt.tight_layout()
plt.show()
