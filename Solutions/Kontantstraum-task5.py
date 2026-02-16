# By Mateusz
# Simulering av Kontantstraum Task 5

import matplotlib.pyplot as plt
import numpy as np

years = np.arange(1, 21)
s = 10_000
r = 0.05

balance = 0
simulated_balance = []

for _ in years:
    balance += s
    balance += balance * r
    simulated_balance.append(balance)

formula_balance = []
for n in years:
    Sn = 0
    for i in range(1, n + 1):
        Sn += s * (1 + r) ** i
    formula_balance.append(Sn)

plt.figure(figsize=(10, 6))
plt.plot(years, simulated_balance, label="Simulation")
plt.plot(years, formula_balance, ls="--", label="Formula")
plt.legend()
plt.show()
