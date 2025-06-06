import numpy as np
import matplotlib.pyplot as plt

irrational_values = {
    "√2": np.sqrt(2),
    "√3": np.sqrt(3),
    "π": np.pi,
    "e": np.e
}

plt.figure(figsize=(8, 2))
for i, (label, value) in enumerate(irrational_values.items()):
    plt.scatter(value, 1, label=f"{label} ≈ {value:.4f}", s=100)

plt.xlabel("Number Line")
plt.yticks([])
plt.title("Visualizing Key Irrational Numbers")
plt.legend()
plt.grid()
plt.show()
