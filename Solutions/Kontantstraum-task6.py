# By Mateusz
# Simulering av Kontantstraum Task 6

import matplotlib.pyplot as plt
import numpy as np

years = np.arange(1, 21)
s = 10_000
r = 0.0225
income_tax = 0.22
wealth_tax = 0.01
inflation = 0.05
balance = 0
balance_over_time = []

for _ in years:
    balance += s
    interest = balance * r
    tax_on_interest = interest * income_tax
    interest_after_tax = interest - tax_on_interest
    balance += interest_after_tax
    wealth_tax_payment = balance * wealth_tax
    balance -= wealth_tax_payment
    balance = balance / (1 + inflation)
    balance_over_time.append(balance)

plt.figure(figsize=(10, 6))
plt.plot(years, balance_over_time, label="Balance after the income tax and inflation")
plt.legend()
plt.show()
