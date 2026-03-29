import numpy as np
import matplotlib.pyplot as plt

r = 3.7
x = 0.5

values = []

for i in range(100):
    x = r * x * (1 - x)
    values.append(x)

plt.plot(values)
plt.title("Logistic Map (Chaos)")
plt.xlabel("Iteration")
plt.ylabel("Population")
plt.show()
