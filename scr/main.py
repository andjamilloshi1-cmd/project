import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 4*np.pi, 500)
y1 = np.sin(x)
y2 = np.cos(x)

plt.figure(figsize=(10,6))
plt.plot(x, y1, label='sin(x)', color='blue', linewidth=2)
plt.plot(x, y2, label='cos(x)', color='red', linestyle='--', linewidth=2)


plt.title("Signature Plot: Sinus & Cosinus", fontsize=16)
plt.xlabel("X values", fontsize=12)
plt.ylabel("Function value", fontsize=12)
plt.grid(True, linestyle=':', alpha=0.7)
plt.legend(fontsize=12)


plt.savefig("../figures/signature_plot.png", dpi=300)
plt.show()